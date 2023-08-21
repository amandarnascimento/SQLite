#1
import sqlite3 as sql 

#2 variavel para fazer a conexao com o banco de dados
conexao = sql.connect('bancodedados.db')

#4 variavel, Apontador do banco de dados. Cursor 
cursor = conexao.cursor()

#5 Colocar informações no banco de dados (ativar commit)
cursor.execute("INSERT INTO tabela (nome, idade, telefone) VALUES ('Maria', 52, 31999999999)")

#Deletar  DELETE FROM nometabela (WHERE (filtro se houver))
#cursor.execute("DELETE FROM tabela WHERE ID = 4")

#6 Alterar dados (ativar commit)
#cursor.execute("UPDATE tabela SET nome = 'Joana' WHERE nome = 'Amanda'")

#Consultar dados de nome e idade
#dados = cursor.execute("SELECT nome, idade FROM tabela").fetchall()
#for dado in dados:
#    print(f"Nome: {dado[0]}")
#    print(f"Idade: {dado[1]}\n") 

7 Commitar/Enviar as informações ao banco de dados
#conexao.commit()

#3 fechar a conexao com o banco de dados
conexao.close




