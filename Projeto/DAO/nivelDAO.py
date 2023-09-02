from DAO.database import DataBase
class NivelDAO(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        self.inserir_nivels()
    def insert_nivel(self, id:int , nome:str):
        try:
            self.cursor()
            if nome:
                sql = '''INSERT INTO nivel (id, nome) VALUES (?,?);'''
                self.cur.execute(sql, (id, nome))
                self.con.commit()
                return 1
        except Exception as e:
            print(f'Erro ao inserir nivel: {e}')
        finally:
            self.desconectar()    
    
    def select_all_nivel(self):
        try:
            self.cursor()
            sql = '''SELECT * FROM nivel;'''
            return self.cur.execute(sql).fetchall()
        except Exception as e:
            print(f'Erro query select all nivel: {e}')
        finally:
            self.desconectar()
    
    def select_id_nivel(self, nome:str):
        try:
            self.cursor()
            sql = '''SELECT id FROM nivel WHERE nome = ?'''
            return self.cur.execute(sql, (nome, )).fetchone()
        except Exception as e:
            print(f'Erro query select id nivel: {e}')
            self.desconectar()  

    def inserir_nivels(self):
        if not self.select_all_nivel():
            self.insert_nivel('1', 'Administrador')
            self.insert_nivel('2', 'Padrao')
