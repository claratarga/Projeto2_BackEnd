from database import conectar


def buscar_usuarios(termo):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = """
            SELECT id, nome, username
            FROM usuarios
            WHERE username LIKE %s OR nome LIKE %s
        """

        valor = f"%{termo}%"
        cursor.execute(sql, (valor, valor))

        return cursor.fetchall()

    finally:
        cursor.close()
        conexao.close()


def buscar_usuario_por_id(usuario_id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = """
            SELECT id, nome, username
            FROM usuarios
            WHERE id = %s
        """

        cursor.execute(sql, (usuario_id,))

        return cursor.fetchone()

    finally:
        cursor.close()
        conexao.close()


def buscar_usuario_por_username(username):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = """
            SELECT id, nome, username, senha
            FROM usuarios
            WHERE username = %s
        """

        cursor.execute(sql, (username,))

        return cursor.fetchone()

    finally:
        cursor.close()
        conexao.close()