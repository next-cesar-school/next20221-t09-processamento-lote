import mysql.connector


# Função para inserir CSV em Banco de Dados:
def insertDataBase(id, periodo_inicial, periodo_final, horas_trabalhadas):
    conexao = mysql.connector.connect(host='localhost:3306', database='db_projects',
                                      user='root', password='', auth_plugin='mysql_native_password')
    try:
        if conexao.is_connected():
            cursor = conexao.cursor()
            sql = "INSERT INTO registro_usuario (id, periodo_inicial, periodo_final, horas_trabalhadas)" \
                  "VALUES (%s, %s, %s, %s)"
            valores = (id, periodo_inicial, periodo_final, horas_trabalhadas)
            cursor.execute(sql, valores)
            conexao.commit()

    except Exception as excecao:
        print(excecao)

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()


# Função para Listar todos os Colaboradores do Banco de Dados:
def todosOsColaboradores(query):
    conexao = mysql.connector.connect(host='localhost:3306', database='db_projects',
                                      user='root', password='', auth_plugin='mysql_native_password')
    cursor = conexao.cursor()
    cursor.execute(query)
    linhas = cursor.fetchall()
    cursor.close()
    conexao.close()
    return linhas
