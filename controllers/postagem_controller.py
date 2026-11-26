from models.postagem import cadastrar_postagem, listar_postagens


def criar(conteudo, usuario_id):
    return cadastrar_postagem(conteudo, usuario_id)


def listar():
    return listar_postagens()
