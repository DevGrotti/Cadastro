import sqlite3 as lite

con = lite.connect("dados.db")


# CRUD(create, read, update, delete)

# inserir valores dentro da tabela no banco de dados
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO cadastro(nome, data_nascimento, altura, peso, genero, naturalidade, hobbies, imagem) VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query,i)



# atualizar valores dentro da tabela cadastro
def atualizar_(i):
    with con:
        cur = con.cursor()
        query = "UPDATE cadastro SET nome=?, data_nascimento=?, altura=?, peso=?, genero=?, naturalidade=?, hobbies=?, imagem=? WHERE id=?"
        cur.execute(query,i)



# deletar valores de um certo id dentro do db
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM cadastro WHERE id=?"
        cur.execute(query,i)


# ver dados individualmente
def ver_form():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM cadastro"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados



# ver dados individuais
def ver_item(id):
    ver_dados_unicos = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM cadastro WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_unicos.append(row)

    return ver_dados_unicos