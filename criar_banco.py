# Serve para conectar com o banco local
import psycopg2
conexao = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres",
    port=5432
)
# Serve parar criar quem executa os comandos sql
cursor = conexao.cursor()

# variavel responsável pelos comandos sql para a criação de tabela que precisamos

comando_sql = """

CREATE TABLE IF NOT EXISTS vendas (

id_venda SERIAL PRIMARY KEY,

data DATE,

produto VARCHAR(100),

categoria VARCHAR(50),

quantidade INTEGER,

preco_unitario NUMERIC(10, 2),

canal_venda VARCHAR(50));

"""

#comando da biblioteca psycopg2 para executar e salvar o comando sql

cursor.execute(comando_sql)
conexao.commit()

# Fechando a conexão com o sql via rede
cursor.close()
conexao.close()

print("Tabela criada com sucesso no PostgreSQL")