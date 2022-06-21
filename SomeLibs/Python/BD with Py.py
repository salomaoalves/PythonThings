import sqlite3
import os

os.remove("escola.db") if os.path.exists("escola.db") else None

con = sqlite3.connect('escola.db')
cur = con.cursor()

#CRIANDO TABELA
sql_create = 'create table cursos '\
'(id integer primary key, '\
'titulo varchar(100), '\
'categoria varchar(140),'\
'valor integer)'
cur.execute(sql_create)

#INSERINDO DADOS
sql_insert = 'insert into cursos values (?, ?, ?, ?)'
recset = [(1000, 'Ciencia de Dados', 'Data Science',1000),
          (1001, 'Big Data Fundamentos', 'Big Data',2500),
          (1002, 'Python Fundamentos', 'Analise de Dados',3200),
          (1003, 'Gestão de Dados com MongoDB', 'Big Data',1200),
          (1004, 'R Fundamentos', 'Análise de Dados',6000)]
for rec in recset:
    cur.execute(sql_insert, rec)
con.commit()

#LENDO DADOS
cur.execute('select * from cursos')
recset = cur.fetchall()
for rec in recset:
    print ('Curso Id: %d, Título: %s, Categoria: %s, Valor: %d ' % rec)

#ATUALIZANDO DADOS
sql_update = "update cursos set valor = 1000 where valor = 1500"
cur.execute(sql_update)
con.commit()

#DELETANDO DADOS    
sql_delete = "delete from cursos where valor = 6000"
cur.execute(sql_delete)
con.commit()

con.close()