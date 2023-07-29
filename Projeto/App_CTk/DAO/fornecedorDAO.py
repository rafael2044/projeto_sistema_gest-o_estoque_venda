from DAO.database import DataBase

class fornecedorDAO(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        
    def insert_fornecedor(self, nome:str, contato:str, endereco:str):
        '''1 - Cadastrado com sucesso
           2 - Fornecedor já existe
           3 - Nome ou Contato invalidos
           '''
        try:
            self.cursor()
            if nome and contato:
                if not self.fornecedor_existe(nome):
                    sql = f'''INSERT INTO fornecedor (nome, contato, endereco) VALUES (?,?,?);'''
                    self.cur.execute(sql,(nome, contato, endereco))
                    self.con.commit()
                    return 1
                return 2
            return 3
        except:
            pass
        finally:
            self.desconectar()
    
    def delete_fornecedor(self, nome:str):
        try:
            self.cursor()
            sql = "DELETE FROM fornecedor WHERE nome = ?"
            self.cur.execute(sql, (nome, ))
            self.con.commit()
            return True
        except:
            pass
        finally:
            self.desconectar
  
    def atualizar_fornecedor(self, id:int, nome:str, contato:str, endereco:str):
        try:
            self.cursor()
            sql = "UPDATE fornecedor SET nome = ?, contato= ?, endereco = ? WHERE id = ?"
            self.cur.execute(sql, (nome, contato, endereco, id))
            self.con.commit()
            return True
        except:
            pass
        finally:
            self.desconectar
  
    def select_all_fornecedores(self):
        try:
            self.cursor()
            sql = '''SELECT * FROM fornecedor'''
            return self.cur.execute(sql).fetchall()
        except:
            pass
        finally:
            self.desconectar()
        
    def select_all_name_fornecedores(self):
        try:
            self.cursor()
            sql = '''SELECT nome FROM fornecedor'''
            return self.cur.execute(sql).fetchall()
        except:
            pass
        finally:
            self.desconectar()
            
    def select_fornecedor(self, nome:str):
        try:
            self.cursor()
            if nome:
                sql = '''SELECT nome, contato, endereco FROM fornecedor WHERE nome = ?;'''
                return self.cur.execute(sql, (nome, )).fetchone()
        except:
            pass
            self.desconectar()
            
    def select_id_fornecedor(self, nome:str):
        try:
            self.cursor()
            if nome:
                sql = '''SELECT id FROM fornecedor WHERE nome = ?;'''
                return self.cur.execute(sql, (nome, )).fetchone()
        except:
            self.desconectar()
 
    def select_like_fornecedor(self, nome:str):
        try:
            self.cursor()
            if nome:
                sql = '''SELECT id, nome, contato, endereco endereco FROM fornecedor WHERE nome LIKE ?;'''
                return self.cur.execute(sql, (nome+'%', )).fetchall()
        except:
            pass
        finally:
            self.desconectar    
    
    def fornecedor_existe(self, nome:str):
        if len(self.select_fornecedor(nome)) > 0:
            return True
        return False