# Processamento em Lote

Construir um sistema (backend - API-only) que permite ler um arquivo CSV através da linha de comando (terminal), validar os dados e inserir no banco de dados.

Como sugestão, pode-se implementar a funcionalidade de ler os dados de horas trabalhadas pelos colaboradores da organização. O arquivo pode seguir o formato abaixo para ler esses dados e injetar no banco. Os dados precisam ser validados, como por exemplo, verificar se a data/hora final é maior que a data/hora inicial, verificar se, para aquele usuário, já não foi reportado um período anterior que conflite com o período sendo reportado atualmente, se o usuário realmente existe no banco de dados, se os dados respeitam a ordem de colunas do arquivo no formato definido (ou se vão inferir a leitura do cabeçalho e ajustar os dados adequadamente), entre outras possíveis validações.

Formato sugerido:

id do usuário | data início | hora início | data fim | hora fim 

Os dados acima foram apenas uma sugestão mínima, mas pode-se pensar em definir outros dados que façam sentido no contexto explicado, como talvez: tipo de operação realizada pelo colaborador naquele período.

Opção: definir se a transação poderá ser desfeita (rollback dos dados) caso alguma validação falhe durante o processamento ou se as operações que não falharem serão salvas no banco e os que falharam serão reportados para posterior processamento.

## Autores

- Hugo Roberto
- Igor Matheus
- João Gabriel
- Victor Amorim (Harry)
