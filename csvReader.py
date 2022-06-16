import pandas
import pandas as pd
import sys
import os
import bancoDefs as bd
import validacao_colunas as vc
import validacao_datetime as vd


def validarCsv(dataframes):
    vc.validarColunas(dataframes)
    periodo_inicial = dataframes[["periodo_inicial"]]
    periodo_final = dataframes[["periodo_final"]]
    for i in range(periodo_inicial.size):
        vd.validarDatas(vd.formatarData(periodo_inicial.values[i]), vd.formatarData(periodo_final.values[i]))


def conversor_df(dataframes):
    bd.insertDataBase(dataframes.columns[0], dataframes.columns[1],
                      dataframes.columns[2], dataframes.columns[3]
                      )


def batchReading(arquivocsv):
    reader = pd.read_csv(arquivocsv, chunksize=5)
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
