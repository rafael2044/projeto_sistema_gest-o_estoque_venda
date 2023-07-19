import pymysql
import pymysql.cursors
from hashlib import sha256


def db_conectar():
    con = pymysql.connect(host='localhost', port=3306, 
                          database='sistema_estoque', user='root',
                          password='', cursorclass=pymysql.cursors.DictCursor)
    
    return con


#table.usuario
def insert_usuario(user:str, password : str):
    with db_conectar() as con:
        with con.cursor() as cur:
            sql = "INSERT INTO usuarios (user, password) VALUES (%s, %s)"
            if user_exists(user):
                return False
            cur.execute(sql, (user, sha256(password.encode()).hexdigest()))
        con.commit()
        return True
    
def select_usuario(user:str):
    with db_conectar() as con:
        with con.cursor() as cur:
            sql = 'SELECT user, password FROM usuarios WHERE user = %s'
            cur.execute(sql,(user, ))
            result = cur.fetchone()
            return result
    
def validate_usuario(user:str, password:str):
    result = select_usuario(user)
    if result:
        if user == result.get('user') and sha256(password.encode()).hexdigest()==result.get('password'):
            return True
    return False

def user_exists(user:str):
    if select_usuario(user):
        return True
    return False

#table.categoria
def insert_categoria(nome:str):
    with db_conectar() as con:
        with con.cursor() as cur:
            sql = "INSERT INTO categoria (nome) VALUES (%s)"
            if categoria_exists(nome):
                return False
            cur.execute(sql, (nome,))
        con.commit()
        return True
    
def select_categoria(nome:str):
    with db_conectar() as con:
        with con.cursor() as cur:
            sql = 'SELECT id, nome FROM categoria WHERE nome = %s'
            cur.execute(sql,(nome, ))
            result = cur.fetchall()
            return result

def select_all_categoria():
    with db_conectar() as con:
        with con.cursor() as cur:
            sql = 'SELECT * FROM categoria'
            cur.execute(sql)
            result = cur.fetchall()
            return result

def categoria_exists(nome:str):
    if select_categoria(nome):
        return True
    return False


#table.unidades
def insert_medida(nome:str, unidade : str):
    with db_conectar() as con:
        with con.cursor() as cur:
            sql = "INSERT INTO medida (nome, unidade) VALUES (%s, %s)"
            if medida_exists(nome):
                return False
            cur.execute(sql, (nome, unidade))
        con.commit()
        return True
    
def select_medida_por_nome(nome:str):
    with db_conectar() as con:
        with con.cursor() as cur:
            sql = 'SELECT id, nome, unidade FROM medida WHERE nome = %s'
            cur.execute(sql,(nome, ))
            result = cur.fetchall()
            return result

def select_medida_nome_por_un(un:str):
    with db_conectar() as con:
        with con.cursor() as cur:
            sql = 'SELECT nome FROM medida WHERE unidade = %s'
            cur.execute(sql,(un, ))
            result = cur.fetchall()
            return result

def select_all_medida():
    with db_conectar() as con:
        with con.cursor() as cur:
            sql = 'SELECT * FROM medida'
            cur.execute(sql)
            result = cur.fetchall()
            return result

def medida_exists(nome:str):
    if select_categoria(nome):
        return True
    return False
