from DAO.database import DataBase

class produtoDAO(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        
    @classmethod
    def insert_produto(cls, descricao:str, id_fornecedor:int, preco_uni:float, cod_barra:str):
        '''1 - Cadastrado com sucesso
           2 - Produto já cadastrado
           3 - Os campos nao foram preenchidos completamente
           '''
        with cls.return_con(cls) as con:
            cur = con.cursor()
            if descricao and id_fornecedor and preco_uni and cod_barra:
                if not cls.produto_existe(cod_barra):
                    sql = f'''INSERT INTO produto (descricao, id_fornecedor, preco_unitario, codigo_de_barra) VALUES (?,?,?,?);'''
                    cur.execute(sql,(descricao, id_fornecedor, preco_uni, cod_barra))
                    con.commit()
                    return 1
                return 2
            return 3
        
    @classmethod  
    def produto_existe(cls, cod_barra:str):
        result = list(cls.select_produto(cod_barra))
        if len(result) > 0:
            return True
        return False

    @classmethod
    def select_produto(cls, cod_barra:str):
        with cls.return_con(cls) as con:
            cur = con.cursor()
            if cod_barra:
                sql = '''SELECT * FROM produto WHERE codigo_de_barra = ?;'''
                return cur.execute(sql, (cod_barra, ))
    @classmethod
    def select_id_produto(cls, cod_barra:str):
        with cls.return_con(cls) as con:
            cur = con.cursor()
            if cod_barra:
                sql = '''SELECT id FROM produto WHERE codigo_de_barra = ?;'''
                return cur.execute(sql, (cod_barra, )).fetchone()
    @classmethod
    def delete_produto(cls, cod_barra:str):
        with cls.return_con(cls) as con:
            cur = con.cursor()
            sql = "DELETE FROM produto WHERE codigo_de_barra = ?"
            cur.execute(sql, (cod_barra, ))
            con.commit()
            return True
