import sqlite3
from pathlib import Path
class DataBase:
    def __init__(self):
        self.create_tables()
    
    def return_con(self):
        db_path = Path(Path(__file__).parent.parent.parent.parent, 'DB','BancoDeDados.db')
        return sqlite3.connect(db_path)
    
    def create_tables(self):
        with self.return_con() as con:
            cur = con.cursor()
            sql_user = '''CREATE TABLE IF NOT EXISTS usuario (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario TEXT NOT NULL,
                        senha VARCHAR(68) NOT NULL,
                        tipo INTEGER NOT NULL
                        
                    );'''
            
            sql_fornecedor = '''CREATE TABLE IF NOT EXISTS fornecedor (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT NOT NULL,
                                    contato TEXT,
                                    endereco TEXT
                                );'''
            
            sql_produto= '''CREATE TABLE IF NOT EXISTS produto (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                descricao TEXT NOT NULL,
                                id_fornecedor INTEGER DEFAULT 0 NOT NULL,
                                preco_unitario REAL NOT NULL,
                                codigo_de_barra TEXT(13) CHECK(length(codigo_de_barra) = 13),
                                FOREIGN KEY (id_fornecedor) REFERENCES fornecedor (id)
                                                            ON UPDATE CASCADE
                                                            ON DELETE SET DEFAULT
                            );'''
            sql_estoque='''CREATE TABLE IF NOT EXISTS estoque (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                id_produto INTEGER NOT NULL,
                                quant_disp INTEGER NOT NULL,
                                quant_min INTEGER NOT NULL,
                                quant_max INTEGER NOT NULL,
                                data_cadastro TEXT NOT NULL DEFAULT (strftime('%d/%m/%Y %H:%M:%S',datetime('now', 'localtime'))),
                                CHECK(quant_disp >= quant_min AND quant_disp <= quant_max),
                                FOREIGN KEY (id_produto) REFERENCES produto (id)
                            );'''
            cur.execute(sql_user)
            cur.execute(sql_fornecedor)
            cur.execute(sql_produto)
            cur.execute(sql_estoque)
            con.commit()
            
DataBase()