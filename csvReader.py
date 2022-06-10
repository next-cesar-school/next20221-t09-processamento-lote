from flask import Flask
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('./csv/bancoColaboradores.csv')

# print para testar se o csv está sendo lido:
print(df)
