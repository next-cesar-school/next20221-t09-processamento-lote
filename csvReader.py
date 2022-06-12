from flask import Flask
import pandas as pd
import sys

app = Flask(__name__)


def main():
    if len(sys.argv) < 2:
        print('Você não inseriu um argumento. Insira o caminho do arquivo CSV corretamente:')
        sys.argv.insert(1, '')
        sys.argv[1] = input()
        while sys.argv[1] != './csv/bancoColaboradores.csv':
            print('Argumento inválido, insira caminho do arquivo CSV corretamente.')
            sys.argv[1] = input()
        else:
            if sys.argv[1] == './csv/bancoColaboradores.csv':
                df = pd.read_csv(sys.argv[1], chunksize=5)
                for minidf in df:
                    print(minidf)
                    break


if __name__ == "__main__":
    main()
