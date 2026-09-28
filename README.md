# 📊 Gestão de Vendas - Pipeline ETL com Python e PostgreSQL

Projeto prático desenvolvido para automatizar a criação de estruturas relacionais e a ingestão de dados de vendas a partir de ficheiros CSV para um banco de dados PostgreSQL.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Linguagem:** Python 3
* **Banco de Dados:** PostgreSQL
* **Interface de Gestão:** pgAdmin 4
* **Bibliotecas Python:** `psycopg2-binary`, `csv`
* **Controlo de Versão:** Git & GitHub
* **Ambiente de Desenvolvimento:** VS Code

---

## 🚀 Estrutura do Projeto

* `gerar_dados.py`: Script responsável por gerar a base fictícia de vendas e exportá-la no arquivo `vendas.csv`.
* `criar_banco.py`: Script responsável por estabelecer a conexão com o PostgreSQL e criar a tabela `vendas` com tipos de dados SQL profissionais (`SERIAL`, `NUMERIC`, `VARCHAR`, `DATE`).
* `inserir_dados.py`: Script que lê o arquivo `vendas.csv`, trata o cabeçalho e realiza a inserção dos registros no banco de dados via transações (`commit`).
* `vendas.csv`: Arquivo de dados brutos utilizado para a carga inicial no banco.

---

## ⚙️ Como Executar o Projeto

1. **Clonar o repositório:**
```bash
git clone https://github.com/Hudson-hag/gestao-vendas-sql.git
cd gestao-vendas-sql
```

2. **Instalar a biblioteca de conexão:**
python -m pip install psycopg2-binary

3. **Configurar o banco de dados:**
Certifique-se de que o PostgreSQL está rodando localmente e ajuste as credenciais de acesso nos scripts, se necessário.

4. **Executar o pipeline completo:**
python gerar_dados.py
python criar_banco.py
python inserir_dados.py

---

## 📌 Próximos Passos
* Extração dos dados salvos no PostgreSQL para análise exploratória com **Pandas**.
* Criação de consultas SQL para geração de KPIs de negócio (faturamento, ticket médio, produtos mais vendidos).