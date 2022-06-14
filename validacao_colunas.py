# Importando o pandas
import pandas as pd

# Lendo e exibindo o arquivo csv
df = pd.read_csv('./csv/bancoColaboradores.csv', encoding="UTF-8")
print(df)

# Definindo a ordem das colunas

# Proposta 1
# col_order = ["data_fim", "id_usuario", "data_inicio", "hora_inicio", "hora_fim"]

# Proposta 2
col_order = df[0:]

# Ajustando a ordem das colunas

# Proposta 1
# df_validado = df.reindex(columns=col_order, copy=False)

# Proposta 2
df_validado = df.reindex(columns=col_order.columns, copy=False)

print(df_validado)

