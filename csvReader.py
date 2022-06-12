from flask import Flask
import pandas as pd
import sys
import os

app = Flask(__name__)

def batchReading(df):
    for minidf in df:
        print(minidf)
        break

def main():
    if len(sys.argv) < 2:
        print('Você não inseriu um argumento. Tente novamente com o caminho de um arquivo CSV existente')
    elif len(sys.argv) == 2:
        arquivoCsv = sys.argv[1]
        if not os.path.isfile(arquivoCsv):
            print('Arquivo não encontrado, insira caminho do arquivo CSV corretamente.')
        else:
            df = pd.read_csv(arquivoCsv, chunksize=5)
            batchReading(df)



if __name__ == "__main__":
    main()
