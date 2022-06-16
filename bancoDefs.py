import mysql.connector
import datetime
now = datetime.datetime.utcnow()


# Função para inserir CSV em Banco de Dados:
def insertDataBase(id, periodo_inicial, periodo_final, horas_trabalhadas):
    conexao = mysql.connector.connect(host='localhost', port="3306", database='db_projects',
                                         user='root', password='bl12p3', auth_plugin='mysql_native_password')
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
    conexao = mysql.connector.connect(host='localhost', port="3306", database='db_projects',
                                         user='root', password='bl12p3', auth_plugin='mysql_native_password')
    cursor = conexao.cursor()
    cursor.execute(query)
    linhas = cursor.fetchall()
    cursor.close()
    conexao.close()
    return linhas

# Função para buscar um Colaborador Específico:
def buscarColaborador(id):
    conexao = mysql.connector.connect(host='localhost', port="3306", database='db_projects',
                                         user='root', password='bl12p3', auth_plugin='mysql_native_password')

    cursor = conexao.cursor()
    cursor.execute("""SELECT time_format(SEC_TO_TIME(SUM(TIME_TO_SEC(horas_trabalhadas))),'%H:%i:%S')
                AS horas_trabalhadas FROM registro_usuario where id = %d""", (id,))
    busca = cursor.fetchall()
    cursor.close()
    conexao.close()
    info = [id, busca]
    return info


# Função para exibir horas trabalhadas de um Colaborador específico do banco de dados:
def infoColaborador(id):
    conexao = mysql.connector.connect(host='localhost', port="3306", database='db_projects',
                                         user='root', password='bl12p3', auth_plugin='mysql_native_password')
    try:
        cursor = conexao.cursor()
        cursor.execute("""SELECT time_format(SEC_TO_TIME(SUM(TIME_TO_SEC(worked_hours))),'%H:%i:%S')
            AS horas_trabalhadas FROM registro_usuario where id = %d""", (id,))

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
