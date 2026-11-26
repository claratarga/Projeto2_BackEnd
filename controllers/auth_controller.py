from flask import session
from controllers.usuario_controller import autenticar


def fazer_login(username, senha):
    usuario = autenticar(username, senha)

    if usuario is None:
        return None

    session.clear()
    session["user_id"] = usuario["id"]

    return usuario


def consultar_sessao():
    usuario_id = session.get("user_id")

    if usuario_id is None:
        return None

    from controllers.usuario_controller import consultar_perfil

    return consultar_perfil(usuario_id)


def fazer_logout():
    session.clear()