from flask import Blueprint, jsonify
from controllers.usuario_controller import pesquisar, consultar_perfil, consultar_publicacoes

usuario_routes = Blueprint("usuarios", __name__)


@usuario_routes.route("/api/users/search/<termo>", methods=["GET"])
def buscar(termo):
    usuarios = pesquisar(termo)

    return jsonify(usuarios), 200


@usuario_routes.route("/api/users/<int:usuario_id>", methods=["GET"])
def perfil(usuario_id):
    usuario = consultar_perfil(usuario_id)

    if usuario is None:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    return jsonify(usuario), 200

@usuario_routes.route("/api/users/<int:usuario_id>/posts", methods=["GET"])
def publicacoes(usuario_id):
    usuario = consultar_perfil(usuario_id)

    if usuario is None:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    postagens = consultar_publicacoes(usuario_id)

    return jsonify(postagens), 200