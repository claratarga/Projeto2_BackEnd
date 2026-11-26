from flask import Blueprint, request, jsonify, session
from controllers.auth_controller import (
    fazer_login,
    consultar_sessao,
    fazer_logout
)
import secrets
import hmac

auth_routes = Blueprint("autenticacao", __name__)


def validar_csrf():
    token = request.headers.get("X-CSRF-Token")
    token_sessao = session.get("csrf_token")

    return (
        token
        and token_sessao
        and hmac.compare_digest(token, token_sessao)
    )


@auth_routes.route("/api/session", methods=["POST"])
def login():
    if not validar_csrf():
        return jsonify({"erro": "Token CSRF inválido"}), 403

    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "Envie os dados em formato JSON"}), 400

    username = dados.get("username")
    senha = dados.get("password")

    if not isinstance(username, str) or not isinstance(senha, str):
        return jsonify({"erro": "Username e senha são obrigatórios"}), 400

    if not username.strip() or not senha:
        return jsonify({"erro": "Username e senha são obrigatórios"}), 400

    usuario = fazer_login(username.strip(), senha)

    if usuario is None:
        return jsonify({"erro": "Usuário ou senha incorretos"}), 401

    token = secrets.token_urlsafe(32)
    session["csrf_token"] = token

    return jsonify({
        "mensagem": "Login realizado com sucesso",
        "usuario": usuario,
        "csrf_token": token
    }), 200


@auth_routes.route("/api/session", methods=["GET"])
def estado_sessao():
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_urlsafe(32)

    usuario = consultar_sessao()

    return jsonify({
        "autenticado": usuario is not None,
        "usuario": usuario,
        "csrf_token": session["csrf_token"]
    }), 200


@auth_routes.route("/api/session", methods=["DELETE"])
def logout():
    if not validar_csrf():
        return jsonify({"erro": "Token CSRF inválido"}), 403

    fazer_logout()

    token = secrets.token_urlsafe(32)
    session["csrf_token"] = token

    return jsonify({
        "mensagem": "Logout realizado com sucesso",
        "csrf_token": token
    }), 200