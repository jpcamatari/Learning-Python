from shutil import ExecError
from sqlite3 import Cursor
import pymysql.cursors

con = pymysql.connect(
    host= "localhost",
    user= "root",
    password= "",
    db= "pythonfull",
    charset= "utf8mb4",
    cursorclass= pymysql.cursors.DictCursor)

def CriaTabela(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"Create table {nomeTabela}(nome varchar(50))")
        print("Tabela Criada")
    except Exception as e:
        print(f'Ocorreu o erro {e}')
def DeletaTabela(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"drop table {nomeTabela}")
        print("Tabela Deletada")
    except Exception as e:
        print(f'Ocorreu o erro: {e}')

def InserirNome(nome):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"INSERT INTO teste values ('{nome}')")
        print("Valor Inserido com Sucesso")
    except Exception as e:
        print(f'Ocorreu o erro {e}')

InserirNome('Pedro')


con.close()