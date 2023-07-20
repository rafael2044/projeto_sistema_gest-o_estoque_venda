from modulos.DAO.database import DataBase

class fornecedorDAO(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        
    @classmethod
    def insert_fornecedor(cls, nome:str, contato:str, endereco:str):
        with cls.return_con(cls) as con:
            cur = con.cursor()
            if nome and contato and not cls.fornecedor_existe(nome):
                sql = f'''INSERT INTO fornecedor (nome, contato, endereco) VALUES (?,?,?);'''
                cur.execute(sql,(nome, contato, endereco))
                con.commit()
                return True
            return False
        
    @classmethod  
    def fornecedor_existe(cls, nome:str):
        result = list(cls.select_fornecedor(nome))
        if len(result) > 0:
            return True
        return False
    
    @classmethod
    def select_all_fornecedores(cls):
        with cls.return_con(cls) as con:
            cur =con.cursor()
            sql = '''SELECT * FROM fornecedor'''
            return list(cur.execute(sql).fetchall())
            
    @classmethod
    def select_fornecedor(cls, nome:str):
        with cls.return_con(cls) as con:
            cur = con.cursor()
            if nome:
                sql = '''SELECT nome, contato, endereco FROM fornecedor WHERE nome = ?;'''
                return cur.execute(sql, (nome, ))
            
                

