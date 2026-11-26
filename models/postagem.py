from database import conectar


def listar_postagens_por_usuario(usuario_id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = """
            SELECT
                postagens.id,
                postagens.conteudo,
                postagens.data_criacao,
                usuarios.username,
                usuarios.nome
            FROM postagens
            INNER JOIN usuarios
            ON postagens.usuario_id = usuarios.id
            WHERE usuarios.id = %s
            ORDER BY postagens.data_criacao DESC
        """

        cursor.execute(sql, (usuario_id,))

        return cursor.fetchall()

    finally:
        cursor.close()
        conexao.close()