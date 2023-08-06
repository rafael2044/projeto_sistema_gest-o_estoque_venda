from DAO.database import DataBase
class SetorDAO(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        self.inserir_setores()
    def insert_setor(self, id:int , nome:str):
        try:
            self.cursor()
            if nome:
                sql = '''INSERT INTO setor (id, nome) VALUES (?,?);'''
                self.cur.execute(sql, (id, nome))
                self.con.commit()
                return 1
        except Exception as e:
            print(f'Erro ao inserir setor: {e}')
        finally:
            self.desconectar()    
    
    def select_all_setor(self):
        try:
            self.cursor()
            sql = '''SELECT * FROM setor;'''
            return self.cur.execute(sql).fetchall()
        except Exception as e:
            print(f'Erro query select all setor: {e}')
        finally:
            self.desconectar()
    
    def select_id_setor(self, nome:str):
        try:
            self.cursor()
            sql = '''SELECT id FROM setor WHERE nome = ?'''
            return self.cur.execute(sql, (nome, )).fetchone()
        except Exception as e:
            print(f'Erro query select id setor: {e}')
            self.desconectar()  

    def inserir_setores(self):
        if not self.select_all_setor():
            self.insert_setor('1', 'ADM')
            self.insert_setor('2', 'Estoque')
            self.insert_setor('3', 'Venda')
