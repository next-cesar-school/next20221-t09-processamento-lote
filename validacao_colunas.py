# Importando o pandas
import pandas as pd

#Definindo função de leitura

def lerArquivo(caminho):
    #caminho = input("Insira o caminho para o arquivo: \n")
    df = pd.read_csv(caminho, encoding="UTF-8")
    return df

def validarColunas(df):
    col_order = df[0:]
    df_validado = df.reindex(columns=col_order.columns, copy=False)
    for col1 in col_order:
        for col2 in df_validado:
            if col1 == col2:
                print("Colunas válidas!")
                return True
            else:
                print("Colunas inválidas!")
                return False

if __name__ == "__main__":
    caminho = "csv/bancoColaboradores.csv"
    arquivo = lerArquivo(caminho)
    validarColunas(arquivo)