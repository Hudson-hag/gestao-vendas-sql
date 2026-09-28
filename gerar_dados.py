import csv
import random
from datetime import datetime, timedelta

# Listas de dados fictícios para combinar aleatoriamente
produtos = [
    {"nome": "Teclado Mecânico", "categoria": "Periféricos", "preco": 250.00},
    {"nome": "Mouse Gamer", "categoria": "Periféricos", "preco": 120.00},
    {"nome": "Monitor 24", "categoria": "Monitores", "preco": 850.00},
    {"nome": "Cadeira Ergonômica", "categoria": "Móveis", "preco": 1100.00},
    {"nome": "Headset USB", "categoria": "Áudio", "preco": 200.00},
    {"nome": "Webcam HD", "categoria": "Periféricos", "preco": 180.00}
]

canais_venda = ["Online", "Loja Física", "E-commerce"]

# Criar e escrever o arquivo CSV
nome_arquivo = "vendas.csv"

with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    
    # Cabeçalho do CSV
    escritor.writerow(["id_venda", "data", "produto", "categoria", "quantidade", "preco_unitario", "canal_venda"])
    
    data_inicial = datetime(2026, 1, 1)
    
    # Gerar 50 vendas aleatórias
    for i in range(1, 51):
        prod = random.choice(produtos)
        data_venda = data_inicial + timedelta(days=random.randint(0, 200))
        quantidade = random.randint(1, 5)
        canal = random.choice(canais_venda)
        
        escritor.writerow([
            i,
            data_venda.strftime("%Y-%m-%d"),
            prod["nome"],
            prod["categoria"],
            quantidade,
            prod["preco"],
            canal
        ])

print(f"Arquivo '{nome_arquivo}' gerado com sucesso com 50 vendas fictícias!")