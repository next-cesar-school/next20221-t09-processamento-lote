from flask import Flask
import pandas as pd

app = Flask(__name__)


def main():
    df = pd.read_csv('./csv/bancoColaboradores.csv', chunksize=5)
    for mini_df in df:
        print(mini_df)
        break


if __name__ == "__main__":
    main()
