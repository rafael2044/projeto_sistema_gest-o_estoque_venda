from modulos.DAO.database import DataBase
from hashlib import sha256

class usuarioDAO(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        
    @classmethod
    def insert_usuario(cls, usuario:str, tipo:int):
        '''1 -  Cadastrado com sucesso
           2 - Usuario já existe
           3 - Dados incompletos'''
        with cls.return_con(cls) as con:
            cur = con.cursor()
            if usuario and tipo:
                if not cls.usuario_existe(usuario):
                    sql = f'''INSERT INTO usuario (usuario, tipo) VALUES (?,?);'''
                    cur.execute(sql,(usuario, tipo))
                    con.commit()
                    return 1
                return 2
            return 3
        
    @classmethod
    def insert_nova_senha(cls,usuario:str, senha:str):
        '''1 - Senha inserida com sucesso!
           2 - Usuario nao existe!'''
        if cls.usuario_existe(usuario):
            with cls.return_con(cls) as con:
                sql = '''UPDATE usuario SET senha = ? WHERE usuario = ?;'''
                con.cursor().execute(sql, (sha256(senha.encode()).hexdigest(), usuario))
                return 1
        return 2
            
    
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
        result = cls.select_usuario(usuario)
        if result:
            return True
        return False
    
    @classmethod
    def resetar_senha(cls, usuario):
        '''1 - Usuario resetado com sucesso!
           2 - Usuario nao existe!'''
        if cls.usuario_existe(usuario):
            with cls.return_con(cls) as con:
                cur = con.cursor()
                sql = '''UPDATE usuario SET usuario_novo = 1 WHERE usuario = ?'''
                cur.execute(sql, (usuario, ))
                return 1
        return 2
    
    @classmethod
    def select_usuario(cls, usuario:str):
        with cls.return_con(cls) as con:
            cur = con.cursor()
            if usuario:
                sql = '''SELECT usuario FROM usuario WHERE usuario = ?;'''
                return cur.execute(sql, (usuario, )).fetchone()
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

    def criar_admin(self):
        self.inserir_tipos()
        if not self.usuario_existe('admin'):
            with self.return_con() as con:
                cur = con.cursor()
                sql = '''INSERT INTO usuario (usuario, senha, tipo, usuario_novo) VALUES
                         (?,?,?,?)'''
                cur.execute(sql, ('admin', sha256('admin'.encode()).hexdigest(), 1, 0))
                return True
        return False
    
    def inserir_tipos(self):
        if not self.select_all_tipo():
            self.insert_tipo('1', 'Administrador')
            self.insert_tipo('2', 'Padrao')
            
            
print(usuarioDAO().criar_admin())