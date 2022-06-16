# Importando o módulo datetime
from datetime import datetime


# Criando função formatadora e conversora de string em data
def formatarData(coluna):
    for data in coluna:
        data_formatada = datetime.strptime(data, "%d/%m/%Y %H:%M:%S")
        return data_formatada


# Criando função validadora
def validarDatas(dinicio, dfim):
    if dinicio < dfim and dinicio != dfim:
        print("Datas válidas!")
        return True
    else:
        print("Algo errado nas datas")
        return False


if __name__ == "__main__":
    # Criando string de datas de exemplo
    d_inicio = "14/06/2022 14:37:55"
    d_fim = "14/06/2022 14:40:12"

    # Verificando tamanho da string de data
    print(len(d_inicio))

    # formatarData(validarDatas())
