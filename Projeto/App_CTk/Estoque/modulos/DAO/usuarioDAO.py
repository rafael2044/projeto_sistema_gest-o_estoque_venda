from modulos.DAO.database import DataBase
from hashlib import sha256

class usuarioDAO(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        
    @classmethod
    def insert_usuario(cls, usuario:str, senha:str, tipo:int):
        '''1 -  Cadastrado com sucesso
           2 - Usuario já existe
           3 - Dados incompletos'''
        with cls.return_con(cls) as con:
            cur = con.cursor()
            if usuario and senha and tipo:
                if not cls.usuario_existe(usuario):
                    senha_sha256 = sha256(senha.encode()).hexdigest()
                    sql = f'''INSERT INTO usuario (usuario, senha, tipo) VALUES (?,?,?);'''
                    cur.execute(sql,(usuario, senha_sha256, tipo))
                    con.commit()
                    return 1
                return 2
            return 3
    @classmethod
    def insert_tipo(cls, id:int , nome:str):
        with cls.return_con(cls) as con:
            cur=con.cursor()
            if nome:
                sql = '''INSERT INTO tipo (id, nome) VALUES (?,?);'''
                cur.execute(sql, (id, nome))
                con.commit()
                return 1
        
    @classmethod
    def select_all_tipo(cls):
        with cls.return_con(cls) as con:
            cur = con.cursor()
            sql = '''SELECT * FROM tipo;'''
            return cur.execute(sql).fetchall()
            
    @classmethod  
    def usuario_existe(cls, usuario:str):
        result = list(cls.select_usuario(usuario))
        if len(result) > 0:
            return True
        return False
    @classmethod
    def select_usuario(cls, usuario:str):
        with cls.return_con(cls) as con:
            cur = con.cursor()
            if usuario:
                sql = '''SELECT usuario FROM usuario WHERE usuario = ?;'''
                return cur.execute(sql, (usuario, ))
    @classmethod
    def select_all_usuario(cls):
        with cls.return_con(cls) as con:
            cur = con.cursor()
            sql = '''SELECT u.id, u.usuario, t.nome FROM usuario as u
                     INNER JOIN tipo as t ON u.tipo = t.id;'''
            return cur.execute(sql).fetchall()
    
    @classmethod
    def select_id_tipo(cls, nome:str):
        with cls.return_con(cls) as con:
            cur = con.cursor()
            sql = '''SELECT id FROM tipo WHERE nome = ?'''
            return cur.execute(sql, (nome, )).fetchone()
    
    @classmethod
    def select_tipo_usuario(cls, usuario:str):
        with cls.return_con(cls) as con:
            cur = con.cursor()
            sql = '''SELECT t.nome FROM usuario
                     INNER JOIN tipo as t ON usuario.tipo = t.id
                     WHERE usuario = ?'''
            return cur.execute(sql, (usuario,)).fetchone()
    
    @classmethod
    def validar_usuario(cls, usuario:str, senha :str):
        with cls.return_con(cls) as con:
            cur = con.cursor()
            if usuario and senha:
                senha_sha256 = sha256(senha.encode()).hexdigest()
                sql = '''SELECT * FROM usuario WHERE usuario = ? AND senha = ?;'''
                result = list(cur.execute(sql, (usuario, senha_sha256)))
                if len(result) == 1:
                    return True
            return False            
