# Importando o pandas
import pandas as pd

# Lendo o arquivo csv
df = pd.read_csv('./csv/bancoColaboradores.csv', encoding="UTF-8")
# Exibindo o arquivo
print(df)
# Definindo ordem das colunas
col_order = ["data_fim", "id_usuario", "data_inicio", "hora_inicio", "hora_fim"]

# Ajustando a ordem das colunas

#Proposta 1
df_validado = df.reindex(columns=col_order, copy=False)
print(df_validado)

#Proposta 2
# df_validado = pd.DataFrame(df, columns=col_order)
# print(df_validado)

