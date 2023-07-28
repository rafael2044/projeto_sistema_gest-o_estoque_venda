from modulos.DAO.database import DataBase
from hashlib import sha256

class usuarioDAO(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        
    @classmethod
    def insert_usuario(cls, usuario:str, senha:str, tipo:int):
        with cls.return_con(cls) as con:
            cur = con.cursor()
            if usuario and senha and not cls.usuario_existe(usuario):
                senha_sha256 = sha256(senha.encode()).hexdigest()
                sql = f'''INSERT INTO usuario (usuario, senha, tipo) VALUES (?,?,?);'''
                cur.execute(sql,(usuario, senha_sha256, tipo))
                con.commit()
                return True
            return False
        
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

                

