#Importando o módulo datetime
from datetime import datetime

#Criando função formatadora e conversora de string em data
def formatarData(data):
    data_formatada = datetime.strptime(data, "%d/%m/%Y %H:%M:%S")
    return data_formatada

d_inicio = "14/06/2022 14:37:55"

d_fim = "14/06/2022 14:40:12"

#Verificando tamanho da string de data
print(len(d_inicio))

#Criando função validadora
def validarDatas(dinicio, dfim):
    if dinicio < dfim and dinicio != dfim and len(d_inicio) == 19:
        return True
    else:
        return False
