from DAO.database import DataBase

class produtoDAO(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        
    
    def insert_produto(self, descricao:str, id_fornecedor:int, preco_uni:float, cod_barra:str):
        '''1 - Cadastrado com sucesso
           2 - Produto já cadastrado
           3 - Os campos nao foram preenchidos completamente
           '''
        try:
            self.cursor()
            if descricao and id_fornecedor and preco_uni and cod_barra:
                if not self.produto_existe(cod_barra):
                    sql = f'''INSERT INTO produto (descricao, id_fornecedor, preco_unitario, codigo_de_barra) VALUES (?,?,?,?);'''
                    self.cur.execute(sql,(descricao, id_fornecedor, preco_uni, cod_barra))
                    self.con.commit()
                    return 1
                return 2
            return 3
        except:
            pass
        finally:
            self.desconectar()
      
    def produto_existe(self, cod_barra:str):
        if len(self.select_produto(cod_barra)) > 0:
            return True
        return False

    
    def select_produto(self, cod_barra:str):
        try:
            self.cursor()
            if cod_barra:
                sql = '''SELECT * FROM produto WHERE codigo_de_barra = ?;'''
                return self.cur.execute(sql, (cod_barra, )).fetchone()
        except:
            self.desconectar()
            
    def select_id_produto(self, cod_barra:str):
        try:
            self.cursor()
            if cod_barra:
                sql = '''SELECT id FROM produto WHERE codigo_de_barra = ?;'''
                return self.cur.execute(sql, (cod_barra, )).fetchone()
        except:
            self.desconectar()
            
    def delete_produto(self, cod_barra:str):
        try:
            self.cursor()
            sql = "DELETE FROM produto WHERE codigo_de_barra = ?"
            self.cur.execute(sql, (cod_barra, ))
            self.con.commit()
            return True
        except:
            pass
        finally:
            self.desconectar()