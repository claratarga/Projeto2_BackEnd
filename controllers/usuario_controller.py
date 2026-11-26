from models.usuario import (
    buscar_usuarios,
    buscar_usuario_por_id,
    buscar_usuario_por_username
)
from werkzeug.security import check_password_hash
from models.postagem import listar_postagens_por_usuario


def pesquisar(termo):
    return buscar_usuarios(termo)


def consultar_perfil(usuario_id):
    return buscar_usuario_por_id(usuario_id)


def autenticar(username, senha):
    usuario = buscar_usuario_por_username(username)

    if usuario is None:
        return None

    if not check_password_hash(usuario["senha"], senha):
        return None

    usuario.pop("senha")

    return usuario


def consultar_publicacoes(usuario_id):
    return listar_postagens_por_usuario(usuario_id)