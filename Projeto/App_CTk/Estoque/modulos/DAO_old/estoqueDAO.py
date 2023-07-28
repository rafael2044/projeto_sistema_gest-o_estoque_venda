from modulos.DAO.database import DataBase
from modulos.DAO.produtoDAO import produtoDAO
class estoqueDAO(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        
    @classmethod
    def insert_produto_estoque(cls, id_produto:int, quant_min:int, quant_atual:int, quant_max:int):
        '''1 - Cadastrado com sucesso
           2 - Produto já existe no estoque
           3 - Os campos nao foram preenchidos completamente
           '''
        with cls.return_con(cls) as con:
            cur = con.cursor()
            if id_produto and quant_min and quant_atual and quant_max:
                if not cls.produto_existe(id_produto):
                    sql = f'''INSERT INTO estoque (id_produto, quant_disp, quant_min, quant_max) VALUES (?,?,?,?);'''
                    cur.execute(sql,(id_produto, quant_atual, quant_min, quant_atual))
                    con.commit()
                    return 1
                return 2
            return 3
        
    @classmethod  
    def produto_existe(cls, id_produto:int):
        result = list(cls.select_produto_estoque(id_produto))
        if len(result) > 0:
            print(result)
            return True
        return False

    @classmethod
    def select_produto_estoque(cls, id_produto:int):
        with cls.return_con(cls) as con:
            cur = con.cursor()
            if id_produto:
                sql = '''SELECT * FROM estoque WHERE id_produto = ?;'''
                return cur.execute(sql, (id_produto, ))
    @classmethod
    def select_all_produto_estoque(cls):
        with cls.return_con(cls) as con:
            cur = con.cursor()
            sql = '''SELECT e.id, p.codigo_de_barra, p.descricao, p.preco_unitario, f.nome, e.quant_disp, e.quant_min, e.quant_max FROM estoque as e
            INNER JOIN produto as p ON p.id = e.id_produto
            INNER JOIN fornecedor as f ON f.id = p.id_fornecedor; '''
            return cur.execute(sql).fetchall()
    
    @classmethod
    def delete_produto_estoque(cls, id:str):
        with cls.return_con(cls) as con:
            cur = con.cursor()
            sql = "DELETE FROM estoque WHERE id = ?"
            cur.execute(sql, (id, ))
            con.commit()
            return True
