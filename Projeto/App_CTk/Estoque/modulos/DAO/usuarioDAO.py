from modulos.DAO.database import DataBase
from hashlib import sha256

class usuarioDAO(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        
    @classmethod
    def select_usuario(cls, usuario:str):
        with cls.return_con(cls) as con:
            cur = con.cursor()
            if usuario:
                sql = '''SELECT usuario FROM usuario WHERE usuario = ?;'''
                return cur.execute(sql, (usuario, ))
    
    @classmethod
    def validar_usuario(cls, usuario:str, senha :str):
        '''1 - Usuario e senha validos
           2 - Usuario ou Senha invalido
           3 - Usuario novo'''
        with cls.return_con(cls) as con:
            cur = con.cursor()
            if usuario:
                if cls.novo_usuario(usuario):
                    return 3
                senha_sha256 = sha256(senha.encode()).hexdigest()
                sql = '''SELECT * FROM usuario WHERE usuario = ? AND senha = ?;'''
                result = cur.execute(sql, (usuario, senha_sha256)).fetchone()
                if result:
                    return 1
            return 2            
        
    @classmethod  
    def usuario_existe(cls, usuario:str):
        result = cls.select_usuario(usuario)
        if result:
            return True
        return False
    
    @classmethod
    def novo_usuario(cls, usuario:str):
        with cls.return_con(cls) as con:
            sql = '''SELECT usuario_novo FROM usuario WHERE usuario = ?'''
            result = con.execute(sql, (usuario,)).fetchone()[0]
            if result:
                return True
            return False
        
    @classmethod
    def nova_senha(cls, usuario:str, senha:str):
        with cls.return_con(cls) as con:
            sql_senha = '''UPDATE usuario SET senha = ? WHERE usuario = ?'''
            sql_usuario_novo = '''UPDATE usuario SET usuario_novo = 0 WHERE usuario = ?'''
            con.cursor().execute(sql_senha, (sha256(senha.encode()).hexdigest(), usuario))
            con.cursor().execute(sql_usuario_novo, (usuario, ))
            con.commit()
            return 1