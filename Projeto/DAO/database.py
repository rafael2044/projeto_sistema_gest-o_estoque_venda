import sqlite3
from pathlib import Path
class DataBase:
    def __init__(self):
        self.create_tables()
        
    def conexao(self):
        try:
            db_path = Path(Path(__file__).parent.parent, 'DB','BancoDeDados.db')
            self.con = sqlite3.connect(db_path)
        except Exception as e:
            print(f'Erro ao realizar conexao com banco de dados!')
            self.desconectar()
    
    def cursor(self):
        self.conexao()
        self.cur = self.con.cursor()
        
    def desconectar(self):
        self.con.close()
        
    def create_tables(self):
        try:
            self.cursor()
            
            sql_nivel = '''CREATE TABLE IF NOT EXISTS nivel (
                          id INTEGER PRIMARY KEY,
                          nome VARCHAR(20) NOT NULL);'''
                          
            sql_setor = '''CREATE TABLE IF NOT EXISTS setor (
                          id INTEGER PRIMARY KEY,
                          nome VARCHAR(20) NOT NULL);'''
                          
            sql_user = '''CREATE TABLE IF NOT EXISTS usuario (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_usuario TEXT NOT NULL,
                        senha VARCHAR(68),
                        nivel INTEGER DEFAULT 0 NOT NULL,
                        setor INTEGER NOT NULL,
                        usuario_novo INTEGER DEFAULT 1 NOT NULL,
                        CHECK(usuario_novo = 0 OR usuario_novo = 1)
                        FOREIGN KEY (nivel) REFERENCES nivel (id)
                                           ON UPDATE CASCADE
                                           ON DELETE SET DEFAULT
                        FOREIGN KEY (setor) REFERENCES setor (id)
                                            ON UPDATE CASCADE
                                            ON DELETE SET DEFAULT
                    );'''
            
            sql_fornecedor = '''CREATE TABLE IF NOT EXISTS fornecedor (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT NOT NULL,
                                    contato TEXT,
                                    endereco TEXT
                                );'''
            
            sql_produto= '''CREATE TABLE IF NOT EXISTS produto (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                codigo_de_barra TEXT(13) CHECK(length(codigo_de_barra) = 13),
                                descricao TEXT NOT NULL,
                                id_fornecedor INTEGER DEFAULT 0 NOT NULL,
                                valor_venda REAL NOT NULL,
                                valor_custo REAL NOT NULL,
                                em_estoque INTEGER DEFAULT 0 NOT NULL,
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
            self.cur.execute(sql_nivel)
            self.cur.execute(sql_setor)
            self.cur.execute(sql_user)
            self.cur.execute(sql_fornecedor)
            self.cur.execute(sql_produto)
            self.cur.execute(sql_estoque)
            self.con.commit()
        except Exception as e:
            print(f'Erro ao criar tabelas: {e}')
        finally:
            self.desconectar()
            
DataBase()