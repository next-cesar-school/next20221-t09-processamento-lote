import mysql.connector


# Função para inserir CSV em Banco de Dados:
def insertDataBase(id, data_inicial, hora_inicial, data_final, hora_final, horas_de_trabalho):
    conexao = mysql.connector.connect(host='localhost', database='mock_db',
                                         user='admin', password='admin', auth_plugin='mysql_native_password')
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
    conexao = mysql.connector.connect(host='localhost', database='mock_db',
                                         user='admin', password='admin', auth_plugin='mysql_native_password')
    cursor = conexao.cursor()
    cursor.execute(query)
    linhas = cursor.fetchall()
    cursor.close()
    conexao.close()
    return linhas

# Função para buscar um Colaborador Específico:
def buscarColaborador(id):
    conexao = mysql.connector.connect(host='localhost', database='mock_db',
                                         user='admin', password='admin', auth_plugin='mysql_native_password')

    cursor = conexao.cursor()
    cursor.execute("""SELECT time_format(SEC_TO_TIME(SUM(TIME_TO_SEC(horas_trabalhadas))),'%H:%i:%S')
                AS horas_trabalhadas FROM colaborador where id = %s""", (id,))
    busca = cursor.fetchall()
    cursor.close()
    conexao.close()
    info = [id, busca]
    return info


# Função para exibir horas trabalhadas de um Colaborador específico do banco de dados:
def infoColaborador(id):
    conexao = mysql.connector.connect(host='localhost', database='mock_db',
                                         user='admin', password='admin', auth_plugin='mysql_native_password')
    try:
        cursor = conexao.cursor()
        cursor.execute("""SELECT time_format(SEC_TO_TIME(SUM(TIME_TO_SEC(worked_hours))),'%H:%i:%S')
            AS horas_trabalhadas FROM colaborador where id = %s""", (id,))

        linhas = cursor.fetchall()
        if not linhas[0][0]:
            print('Registro não encontrado')
        else:
            print(f'O colaborador de id \033[4;36m{id}\033[m tem como horas trabalhadas: \033[4;36m{linhas[0][0]}\033[m')

    except Exception as excecao:
        print(excecao)

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
