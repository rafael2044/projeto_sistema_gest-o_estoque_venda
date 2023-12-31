from DAO.database import DataBase
from DAO.nivelDAO import NivelDAO
from DAO.setorDAO import SetorDAO

from hashlib import sha256

class usuarioDAO(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        self.criar_admin()
    
    def insert_usuario(self, nome_usuario:str, nivel:int, setor:int):
        '''DML que inseri um nome_usuario na tabela nome_usuario
           Possiveis retornos:
           1 - Cadastrado com sucesso
           2 - Usuario já existe
           3 - Dados incompletos'''
        try:
            self.cursor()
            if nome_usuario and nivel and setor:
                if not self.usuario_existe(nome_usuario):
                    sql = f'''INSERT INTO usuario (nome_usuario, nivel, setor) VALUES (?,?,?);'''
                    self.cur.execute(sql,(nome_usuario, nivel, setor))
                    self.con.commit()
                    return 1
                return 2
            return 3
        except Exception as e:
            print(f'Erro ao inserir usuario: {e}')
        finally:
            self.desconectar()
    
    def deletar_usuario(self, id:int):
        '''DML que deleta um usuario com o id que eh passado como argumento'''
        try:
            self.cursor()
            sql = '''DELETE FROM usuario WHERE id = ?'''
            self.cur.execute(sql, (int(id), ))
            self.con.commit()
            return True
        except Exception as e:
            print(f'Erro ao deletar usuario: {e}')
        finally:
            self.desconectar()
            
    def atualizar_usuario(self, id:int, nome_usuario:str, nivel:int, setor:int):
        '''DML que atualiza os dados: usuario e nivel; do id do usuario que foi passado como argumento.
           Possiveis retornos:
           1 - Alteracoes realizadas com sucesso!
           2 - Usuario ja existe!'''
        try:
            self.cursor()
            
            if not self.usuario_existe(nome_usuario) or self.select_id_usuario(nome_usuario)[0] == int(id):
                sql = "UPDATE usuario SET nome_usuario = ?, nivel= ?, setor = ? WHERE id = ?"
                self.cur.execute(sql, (nome_usuario, nivel,setor, id))
                self.con.commit()
                return 1
            return 2
        except Exception as e:
            print(f'Erro ao atualizar usuario: {e}')
        finally:
            self.desconectar()        
            
    def select_nome_usuario(self, nome_usuario:str):
        '''Query que retorna o usuario '''
        try:
            self.cursor()
            if nome_usuario:
                sql = '''SELECT nome_usuario FROM usuario WHERE nome_usuario = ?;'''
                return self.cur.execute(sql, (nome_usuario, )).fetchall()
        except Exception as e:
            print(f'Erro query select nome usuario: {e}')
            self.desconectar()
    
    def select_id_usuario(self, nome_usuario:str):
        try:
            self.cursor()
            sql = '''SELECT id FROM usuario WHERE nome_usuario = ?'''
            return self.cur.execute(sql, (nome_usuario, )).fetchone()
        except Exception as e:
            print(f'Erro query select id usuario: {e}')
            self.desconectar()
            
    def select_all_usuario(self):
        try:
            self.cursor()
            sql = '''SELECT u.id, u.nome_usuario, n.nome, s.nome FROM usuario as u
                     INNER JOIN nivel as n ON u.nivel = n.id
                     INNER JOIN setor as s ON u.setor = s.id;'''
            return self.cur.execute(sql).fetchall()
        except Exception as e:
            print(f'Erro query select all usuario: {e}')
        finally:
            self.desconectar()
      
    def select_nivel_usuario(self, nome_usuario:str):
        try:
            self.cursor()
            sql = '''SELECT n.nome FROM usuario as u
                     INNER JOIN nivel as n ON u.nivel = n.id
                     WHERE u.nome_usuario = ?'''
            return self.cur.execute(sql, (nome_usuario, )).fetchone()
        except Exception as e:
            print(f'Erro query select nivel usuario: {e}')
            self.desconectar()
        finally:
            self.desconectar()
            
    def select_setor_usuario(self, nome_usuario:str):
        try:
            self.cursor()
            sql = '''SELECT s.nome FROM usuario as u
                     INNER JOIN setor as s ON u.setor = s.id
                     WHERE u.nome_usuario = ?'''
            return self.cur.execute(sql, (nome_usuario, )).fetchone()
        except Exception as e:
            print(f'Erro query select nivel usuario: {e}')
            self.desconectar()
        finally:
            self.desconectar() 
      
    def usuario_existe(self, nome_usuario:str):
        if len(self.select_nome_usuario(nome_usuario))>0:
            return True
        return False

    
    def novo_usuario(self, nome_usuario:str):
        try:
            sql = '''SELECT usuario_novo FROM usuario WHERE nome_usuario = ?'''
            if self.con.execute(sql, (nome_usuario,)).fetchone()[0]:
                return True
            return False
        except Exception as e:
            print(f'Erro ao verificar se usuario eh novo: {e}')
            self.desconectar()
    
    def validar_usuario(self, nome_usuario:str, senha :str):
        '''1 - Login efetuado com sucesso
           2 - Usuario ou Senha invalido
           3 - Usuario novo'''
        try:
            self.cursor()
            if self.usuario_existe(nome_usuario):
                if self.novo_usuario(nome_usuario):
                    return 3
                senha_sha256 = sha256(senha.encode()).hexdigest()
                sql = '''SELECT * FROM usuario WHERE nome_usuario = ? AND senha = ?;'''
                
                if self.cur.execute(sql, (nome_usuario, senha_sha256)).fetchone():
                    return 1
            return 2            
        except Exception as e:
            print(f'Erro ao validar usuario: {e}')
        finally:
            self.desconectar()
    
    def nova_senha(self, nome_usuario:str, senha:str):
        try:
            self.cursor()
            sql_senha = '''UPDATE usuario SET senha = ? WHERE nome_usuario = ?'''
            sql_usuario_novo = '''UPDATE usuario SET usuario_novo = 0 WHERE nome_usuario = ?'''
            self.cur.execute(sql_senha, (sha256(senha.encode()).hexdigest(), nome_usuario))
            self.cur.execute(sql_usuario_novo, (nome_usuario, ))
            self.con.commit()
            return 1
        except Exception as e:
            print(f'Erro ao verificar ao alterar senha: {e}')
        finally:
            self.desconectar()
    
    def resetar_senha(self, nome_usuario):
        '''1 - Usuario resetado com sucesso!
           2 - Usuario nao existe!'''
        try:
            if self.usuario_existe(nome_usuario):
                self.cursor()
                sql = '''UPDATE usuario SET usuario_novo = 1 WHERE nome_usuario = ?'''
                self.cur.execute(sql, (nome_usuario, ))
                self.con.commit()
                return 1
            return 2  
        except Exception as e:
            print(f'Erro ao resetar senha de usuario: {e}')
        finally:
            self.desconectar()  
      
           
    def criar_admin(self):
        try:
            NivelDAO()
            SetorDAO()
            if not self.usuario_existe('admin'):
                    self.cursor()
                    sql = '''INSERT INTO usuario (nome_usuario, senha, nivel, setor, usuario_novo) VALUES
                            (?,?,?,?,?)'''
                    self.cur.execute(sql, ('admin', sha256('admin'.encode()).hexdigest(), 1,1,0))
                    self.con.commit()
                    return True
            return False
        except Exception as e:
            print(f'Erro ao criar usuario admin: {e}')
            
        finally:
            self.desconectar()
    
