import csv
import psycopg2

# se conectancdo com o banco

conexao = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres",
    port=5432
)
cursor = conexao.cursor()

# abrir o ler o arquivo

with open('vendas.csv', mode= 'r', encoding='utf-8') as arquivo: 
    leitor = csv.reader(arquivo)
    next(leitor) # pula a primeira linha com o cabeçalho

# processar cada linha do csv e fazer o insert na tabela

    for linha in leitor:
        comando_insert = """
INSERT INTO vendas (id_venda, data, produto, categoria, quantidade, preco_unitario, canal_venda)
values (%s, %s, %s, %s, %s, %s, %s);
"""
        cursor.execute(comando_insert, linha)

# salvar as alterações e fechar conecão
conexao.commit()
cursor.close()
conexao.close()

print("Dados inseridos com sucesso na tabela vendas")