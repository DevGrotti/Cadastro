# importando SQLite
import sqlite3 as lite

# criando conexão

con = lite.connect("dados.db")

# criando tabela dentro do banco de dados
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE cadastro(ID INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, naturalidade TEXT, data_nascimento DATE, genero TEXT, altura DECIMAL, peso DECIMAL, hobbies TEXT, imagem TEXT)")
