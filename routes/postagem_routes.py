
from flask import Blueprint, request, jsonify, session
from controllers.postagem_controller import criar, listar

postagem_routes = Blueprint("postagens", __name__)


@postagem_routes.route("/postagens", methods=["GET"])
def listar_todas():
    postagens = listar()

    return jsonify(postagens), 200


@postagem_routes.route("/postagens", methods=["POST"])
def cadastrar():
    if "usuario_id" not in session:
        return jsonify({"erro": "Você precisa estar logado"}), 401

    dados = request.get_json(silent=True)

    if not dados:
        return jsonify({"erro": "Envie os dados em formato JSON"}), 400

    conteudo = dados.get("conteudo")

    if not conteudo or not conteudo.strip():
        return jsonify({"erro": "O conteúdo da postagem é obrigatório"}), 400

    usuario_id = session["usuario_id"]

    postagem_id = criar(conteudo.strip(), usuario_id)

    return jsonify({
        "mensagem": "Postagem criada com sucesso",
        "id": postagem_id
    }), 201
