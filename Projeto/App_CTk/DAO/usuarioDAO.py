from DAO.database import DataBase
from DAO.tipoDAO import TipoDAO

from hashlib import sha256

class usuarioDAO(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        self.criar_admin()
    
    def insert_usuario(self, usuario:str, tipo:int):
        '''1 -  Cadastrado com sucesso
           2 - Usuario já existe
           3 - Dados incompletos'''
        try:
            self.cursor()
            if usuario and tipo:
                if not self.usuario_existe(usuario):
                    sql = f'''INSERT INTO usuario (usuario, tipo) VALUES (?,?);'''
                    self.cur.execute(sql,(usuario, tipo))
                    self.con.commit()
                    return 1
                return 2
            return 3
        except:
            pass
        finally:
            self.desconectar()
    
    def deletar_usuario(self, id:int):
        try:
            self.cursor()
            sql = '''DELETE FROM usuario WHERE id = ?'''
            self.cur.execute(sql, (int(id), ))
            self.con.commit()
            return True
        except:
            pass
        finally:
            self.desconectar()
            
    def atualizar_usuario(self, id:int, usuario:str, tipo:int):
        '''1 - Alteracoes realizadas com sucesso!
           2 - Usuario ja existe!'''
        try:
            self.cursor()
            
            if not self.usuario_existe(usuario) or self.select_id_usuario(usuario)[0] == int(id):
                sql = "UPDATE usuario SET usuario = ?, tipo= ? WHERE id = ?"
                self.cur.execute(sql, (usuario, tipo, id))
                self.con.commit()
                return 1
            return 2
        except:
            pass
        finally:
            self.desconectar()        
            
    def select_usuario(self, usuario:str):
        try:
            self.cursor()
            if usuario:
                sql = '''SELECT usuario FROM usuario WHERE usuario = ?;'''
                return self.cur.execute(sql, (usuario, )).fetchall()
        except:
            self.desconectar()
    
    def select_id_usuario(self, usuario:str):
        try:
            self.cursor()
            sql = '''SELECT id FROM usuario WHERE usuario = ?'''
            return self.cur.execute(sql, (usuario, )).fetchone()
        except:
            self.desconectar()
            
    def select_all_usuario(self):
        try:
            self.cursor()
            sql = '''SELECT u.id, u.usuario, t.nome FROM usuario as u
                     INNER JOIN tipo as t ON u.tipo = t.id;'''
            return self.cur.execute(sql).fetchall()
        except:
            pass
        finally:
            self.desconectar()
      
    def select_tipo_usuario(self, usuario:str):
        try:
            self.cursor()
            sql = '''SELECT t.nome FROM usuario as u
                     INNER JOIN tipo as t ON u.tipo = t.id
                     WHERE usuario = ?'''
            return self.cur.execute(sql, (usuario, )).fetchone()
        except:
            self.desconectar()
        finally:
            self.desconectar()
      
    def usuario_existe(self, usuario:str):
        if len(self.select_usuario(usuario))>0:
            return True
        return False

    
    def novo_usuario(self, usuario:str):
        try:
            sql = '''SELECT usuario_novo FROM usuario WHERE usuario = ?'''
            if self.con.execute(sql, (usuario,)).fetchone()[0]:
                return True
            return False
        except:
            pass
    
    def validar_usuario(self, usuario:str, senha :str):
        '''1 - Usuario e senha validos
           2 - Usuario ou Senha invalido
           3 - Usuario novo'''
        try:
            self.cursor()
            if usuario:
                if self.novo_usuario(usuario):
                    return 3
                senha_sha256 = sha256(senha.encode()).hexdigest()
                sql = '''SELECT * FROM usuario WHERE usuario = ? AND senha = ?;'''

                if len(self.cur.execute(sql, (usuario, senha_sha256)).fetchone()):
                    return 1
            return 2            
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar()
    
    def nova_senha(self, usuario:str, senha:str):
        try:
            self.cursor()
            sql_senha = '''UPDATE usuario SET senha = ? WHERE usuario = ?'''
            sql_usuario_novo = '''UPDATE usuario SET usuario_novo = 0 WHERE usuario = ?'''
            self.cur.execute(sql_senha, (sha256(senha.encode()).hexdigest(), usuario))
            self.cur.execute(sql_usuario_novo, (usuario, ))
            self.con.commit()
            return 1
        except:
            pass
        finally:
            self.desconectar()
    
    def resetar_senha(self, usuario):
        '''1 - Usuario resetado com sucesso!
           2 - Usuario nao existe!'''
        try:
            if self.usuario_existe(usuario):
                self.cursor()
                sql = '''UPDATE usuario SET usuario_novo = 1 WHERE usuario = ?'''
                self.cur.execute(sql, (usuario, ))
                self.con.commit()
                return 1
            return 2  
        except:
            pass
        finally:
            self.desconectar()  
      
           
    def criar_admin(self):
        try:
            TipoDAO()
            if not self.usuario_existe('admin'):
                    self.cursor()
                    sql = '''INSERT INTO usuario (usuario, senha, tipo, usuario_novo) VALUES
                            (?,?,?,?)'''
                    self.cur.execute(sql, ('admin', sha256('admin'.encode()).hexdigest(), 1, 0))
                    return True
            return False
        except:
            pass
        finally:
            self.desconectar()