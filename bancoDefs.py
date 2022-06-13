import mysql.connector


# Função para inserir CSV em Banco de Dados:
def insertDataBase(id, data_inicial, hora_inicial, data_final, hora_final, horas_de_trabalho):
    conexao = mysql.connector.connect(host='localhost', database='db_projects',
                                         user='root', password='', auth_plugin='mysql_native_password')
    try:
        if conexao.is_connected():
            cursor = conexao.cursor()
            sql = "INSERT INTO colaborador (id, data_inicial, hora_inicial, data_final, hora_final, horas_trabalhadas)" \
                  "VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (id, data_inicial, hora_inicial, data_final, hora_final, horas_de_trabalho)
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
    conexao = mysql.connector.connect(host='localhost', database='db_projects',
                                         user='root', password='', auth_plugin='mysql_native_password')
    cursor = conexao.cursor()
    cursor.execute(query)
    linhas = cursor.fetchall()
    cursor.close()
    conexao.close()
    return linhas