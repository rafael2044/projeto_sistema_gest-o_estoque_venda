from DAO.database import DataBase
from DAO.produtoDAO import produtoDAO
class estoqueDAO(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        
    def insert_produto_estoque(self, id_produto:int, quant_min:int, quant_atual:int, quant_max:int):
        '''1 - Cadastrado com sucesso
           2 - Produto já existe no estoque
           3 - Os campos nao foram preenchidos completamente
           '''
        try:
            self.cursor()
            if id_produto and quant_min and quant_atual and quant_max:
                if not self.produto_existe(id_produto):
                    sql = f'''INSERT INTO estoque (id_produto, quant_disp, quant_min, quant_max) VALUES (?,?,?,?);'''
                    self.cur.execute(sql,(id_produto, quant_atual, quant_min, quant_atual))
                    self.con.commit()
                    return 1
                return 2
            return 3
        except:
            pass
        finally:
            self.desconectar()

    def delete_produto_estoque(self, id:str):
        try:
            self.cursor()
            sql = "DELETE FROM estoque WHERE id = ?"
            self.cur.execute(sql, (id, ))
            self.con.commit()
            return True
        except:
            pass
        finally:
            self.desconectar()


    def select_produto_estoque(self, id_produto:int):
        try:
            self.cursor()
            if id_produto:
                sql = '''SELECT * FROM estoque WHERE id_produto = ?;'''
                return self.cur.execute(sql, (id_produto, )).fetchone()
        except:
            self.desconectar()
  
  
    def select_all_estoque(self):
        try:
            self.cursor()
            sql = '''SELECT e.id, p.codigo_de_barra, p.descricao, p.preco_unitario, f.nome, e.quant_disp, e.quant_min, e.quant_max FROM estoque as e
            INNER JOIN produto as p ON p.id = e.id_produto
            INNER JOIN fornecedor as f ON f.id = p.id_fornecedor; '''
            return self.cur.execute(sql).fetchall()
        except:
            pass
        finally:
            self.desconectar()


    def produto_existe(self, id_produto:int):
        if len(self.select_produto_estoque(id_produto)) > 0:
            return True
        return False