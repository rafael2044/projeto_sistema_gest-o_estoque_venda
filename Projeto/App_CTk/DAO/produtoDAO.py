from DAO.database import DataBase

class produtoDAO(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        
    
    def insert_produto(self, cod_barra:str, descricao:str, preco_uni:float, id_fornecedor:int):
        '''1 - Cadastrado com sucesso
           2 - Produto já cadastrado
           3 - Os campos nao foram preenchidos completamente
           '''
        try:
            self.cursor()
            if descricao and id_fornecedor and preco_uni and cod_barra:
                if not self.produto_existe(cod_barra):
                    sql = f'''INSERT INTO produto (codigo_de_barra ,descricao, id_fornecedor, preco_unitario) VALUES (?,?,?,?);'''
                    self.cur.execute(sql,(cod_barra, descricao,id_fornecedor,preco_uni))
                    self.con.commit()
                    return 1
                return 2
            return 3
        except Exception as e:
            print(f'Erro ao inserir produto: {e}')
        finally:
            self.desconectar()
      
    def produto_existe(self, cod_barra:str):
        if self.select_produto(cod_barra):
            return True
        return False

    
    def select_produto(self, cod_barra:str):
        try:
            self.cursor()
            if cod_barra:
                sql = '''SELECT * FROM produto WHERE codigo_de_barra = ?;'''
                return self.cur.execute(sql, (cod_barra, )).fetchone()
        except Exception as e:
            print(f'Erro query select produto: {e}')
            self.desconectar()
    
    def select_all_produto(self):
        try:
            self.cursor()
            sql = '''SELECT p.id, p.codigo_de_barra, p.descricao, f.nome, p.preco_unitario FROM produto as p 
                     INNER JOIN fornecedor as f ON p.id_fornecedor = f.id'''
            return self.cur.execute(sql,).fetchall()
        except Exception as e:
            print(f'Erro query select produto n cad em estoque: {e}')
            self.desconectar()
    
    def select_produto_n_cad_em_estoque(self):
        try:
            self.cursor()
            sql = '''SELECT p.id, p.codigo_de_barra, p.descricao, f.nome, p.preco_unitario FROM produto as p 
                     INNER JOIN fornecedor as f ON p.id_fornecedor = f.id
                     WHERE p.em_estoque = 0;'''
            return self.cur.execute(sql,).fetchall()
        except Exception as e:
            print(f'Erro query select produto n cad em estoque: {e}')
            self.desconectar()
            
    def select_id_produto(self, cod_barra:str):
        try:
            self.cursor()
            if cod_barra:
                sql = '''SELECT id FROM produto WHERE codigo_de_barra = ?;'''
                return self.cur.execute(sql, (cod_barra, )).fetchone()
        except Exception as e:
            print(f'Erro query select id produto: {e}')
            self.desconectar()
            
    def delete_produto(self, cod_barra:str):
        try:
            self.cursor()
            sql = "DELETE FROM produto WHERE codigo_de_barra = ?"
            self.cur.execute(sql, (cod_barra, ))
            self.con.commit()
            return True
        except Exception as e:
            print(f'Erro ao deletar produto: {e}')
        finally:
            self.desconectar()