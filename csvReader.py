import pandas as pd
import sys
import os
import bancoDefs as bd
import validacao_colunas as vc
import validacao_datetime as vd
from datetime import datetime

CHUNK = 5

def validarCsv(dataframes):
    vc.validarColunas(dataframes)
    periodo_inicial = dataframes[["periodo_inicial"]]
    periodo_final = dataframes[["periodo_final"]]
    for i in range(periodo_inicial.size):
        vd.validarDatas(vd.formatarData(periodo_inicial.values[i]), vd.formatarData(periodo_final.values[i]))


def conversor_df(df):
    for i in range(0, len(df)):
        print(df.values[i])
        data_periodo_inicio = datetime.strptime(df.values[i][1], "%d/%m/%Y %H:%M:%S")
        data_periodo_fim = datetime.strptime(df.values[i][2], "%d/%m/%Y %H:%M:%S")
        print("inserting line: ", df.values[i])
        bd.insertDataBase(df.values[i][0], data_periodo_inicio, data_periodo_fim, df.values[i][3])


def batchReading(arquivocsv):
    reader = pd.read_csv(arquivocsv, chunksize=CHUNK)
    for dataframes in reader:
        print(dataframes)
        validarCsv(dataframes)
        conversor_df(dataframes)


def main():
    if len(sys.argv) < 2:
        print('Você não inseriu um argumento. Tente novamente com o caminho de um arquivo CSV existente')
    elif len(sys.argv) == 2:
        arquivoCsv = sys.argv[1]
        if not os.path.isfile(arquivoCsv):
            print('Arquivo não encontrado, insira caminho do arquivo CSV corretamente.')
        else:
            batchReading(arquivoCsv)


if __name__ == "__main__":
    main()