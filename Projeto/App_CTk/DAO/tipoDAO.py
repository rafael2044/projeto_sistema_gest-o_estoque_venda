from DAO.database import DataBase
class TipoDAO(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        self.inserir_tipos()
    def insert_tipo(self, id:int , nome:str):
        try:
            self.cursor()
            if nome:
                sql = '''INSERT INTO tipo (id, nome) VALUES (?,?);'''
                self.cur.execute(sql, (id, nome))
                self.con.commit()
                return 1
        except Exception as e:
            print(f'Erro ao inserir tipo: {e}')
        finally:
            self.desconectar()    
    
    def select_all_tipo(self):
        try:
            self.cursor()
            sql = '''SELECT * FROM tipo;'''
            return self.cur.execute(sql).fetchall()
        except Exception as e:
            print(f'Erro query select all tipo: {e}')
        finally:
            self.desconectar()
    
    def select_id_tipo(self, nome:str):
        try:
            self.cursor()
            sql = '''SELECT id FROM tipo WHERE nome = ?'''
            return self.cur.execute(sql, (nome, )).fetchone()
        except Exception as e:
            print(f'Erro query select id tipo: {e}')
            self.desconectar()  

    def inserir_tipos(self):
        if not self.select_all_tipo():
            self.insert_tipo('1', 'Administrador')
            self.insert_tipo('2', 'Padrao')
