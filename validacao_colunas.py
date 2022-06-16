def validarColunas(df):
    col_order = df.columns
    col_model = ["id", "periodo_inicial", "periodo_final", "horas_trabalhadas"]

    if (col_order == col_model).all():
        print("Colunas válidas!")
        return True
    else:
        print("Colunas inválidas!")
        return False


if __name__ == "__main__":
    caminho = "csv/bancoColaboradores.csv"
    # arquivo = lerArquivo(caminho)
    # validarColunas(arquivo)
