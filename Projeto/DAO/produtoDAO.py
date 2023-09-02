from DAO.database import DataBase
from Geral.Classes.Produto import Produto
class produtoDAO(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        
    
    def insert_produto(self, cod_barra:str, descricao:str, valor_venda:float,valor_custo:float, id_fornecedor:int):
        '''1 - Cadastrado com sucesso
           2 - Produto já cadastrado
           3 - Os campos nao foram preenchidos completamente
           '''
        try:
            self.cursor()
            if descricao and id_fornecedor and valor_venda and valor_custo and cod_barra:
                if not self.produto_existe_cod_barra(cod_barra):
                    sql = f'''INSERT INTO produto (codigo_de_barra ,descricao, id_fornecedor, valor_venda, valor_custo) VALUES (?,?,?,?,?);'''
                    self.cur.execute(sql,(cod_barra, descricao,id_fornecedor,valor_venda, valor_custo))
                    self.con.commit()
                    return 1
                return 2
            return 3
        except Exception as e:
            print(f'Erro ao inserir produto: {e}')
        finally:
            self.desconectar()
      
    def produto_existe_cod_barra(self, cod_barra:str):
        if self.select_produto_cod_barra(cod_barra):
            return True
        return False

    def atualizar_produto(self, id:int, descricao:str, valor_venda:float,valor_custo:float, id_fornecedor:int):
        try:
            self.cursor()
            sql = "UPDATE produto SET descricao = ?, valor_venda = ?, valor_custo = ?, id_fornecedor = ? WHERE id = ?"
            self.cur.execute(sql, (descricao, valor_venda, valor_custo, id_fornecedor, id))
            self.con.commit()
            return True
        except Exception as e:
            print(f'Erro ao atualizar produto: {e}')
        finally:
            self.desconectar

    def update_em_estoque(self, id:int):
        try:
            self.cursor()
            if self.select_produto_id(id):
                sql = '''UPDATE produto SET em_estoque=1 WHERE id = ?;'''
                self.cur.execute(sql, (id,))
                self.con.commit()
        except Exception as e:
            print(f'Erro update produto em estoque: {e}')
            self.desconectar()
    
    def select_produto_cod_barra(self, cod_barra:str):
        try:
            self.cursor()
            if cod_barra:
                sql = '''SELECT * FROM produto WHERE codigo_de_barra = ?;'''
                return self.cur.execute(sql, (cod_barra, )).fetchone()
        except Exception as e:
            print(f'Erro query select produto: {e}')
            self.desconectar()
    
    def select_produto_id(self, id:int):
        try:
            self.cursor()
            if id:
                sql = '''SELECT * FROM produto WHERE id = ?;'''
                return self.cur.execute(sql, (id, )).fetchone()
        except Exception as e:
            print(f'Erro query select produto id: {e}')
            self.desconectar()
    
    def select_all_produto(self):
        try:
            self.cursor()
            sql = '''SELECT p.id, p.codigo_de_barra, p.descricao, f.nome, p.valor_venda, p.valor_custo FROM produto as p 
                     INNER JOIN fornecedor as f ON p.id_fornecedor = f.id'''
            produtos = []
            for x in self.cur.execute(sql,).fetchall():
                produtos.append(Produto(*x))
            return produtos
        except Exception as e:
            print(f'Erro query select produto n cad em estoque: {e}')
            self.desconectar()
    
    def select_produto_n_cad_em_estoque(self):
        try:
            self.cursor()
            sql = '''SELECT p.id, p.codigo_de_barra, p.descricao, f.nome, p.valor_venda, p.valor_custo FROM produto as p 
                     INNER JOIN fornecedor as f ON p.id_fornecedor = f.id
                     WHERE p.em_estoque = 0;'''
            produtos = []
            for x in self.cur.execute(sql,).fetchall():
                produtos.append(Produto(*x))
            return produtos
        
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