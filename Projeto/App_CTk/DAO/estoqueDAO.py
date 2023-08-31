from DAO.database import DataBase
from DAO.produtoDAO import produtoDAO
class estoqueDAO(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        
    def insert_produto_estoque(self, id_produto:int, quant_min:int, quant_atual:int, quant_max:int):
        '''DML que inseri um produto na tabela estoque.
           Possiveis retornos:
           1 - Cadastrado com sucesso
           2 - Produto já existe no estoque
           3 - Os campos nao foram preenchidos completamente
           '''
        try:
            self.cursor()
            if id_produto and quant_min and quant_atual and quant_max:
                if not self.produto_existe(id_produto):
                    sql = f'''INSERT INTO estoque (id_produto, quant_disp, quant_min, quant_max) VALUES (?,?,?,?);'''
                    self.cur.execute(sql,(id_produto, quant_atual, quant_min, quant_max))
                    self.con.commit()
                    produtoDAO().update_em_estoque(id_produto)
                    return 1
                return 2
            return 3
        except Exception as e:
            print(f'Erro ao inserir produto em estoque: {e}')
        finally:
            self.desconectar()

    def delete_produto_estoque(self, id:str):
        '''DML que deleta um produto em estoque de id passado como argumento'''
        try:
            self.cursor()
            sql = "DELETE FROM estoque WHERE id = ?"
            self.cur.execute(sql, (id, ))
            self.con.commit()
            return True
        except Exception as e:
            print(f'Erro ao deletar produto do estoque: {e}')
        finally:
            self.desconectar()


    def select_produto_estoque(self, id_produto:int):
        '''Query select que retorna os elementos no estoque com id_produto passado como argumento.
           O Retorno eh uma lista contendo a(s) linha(s) que possui o id_produto especificado.'''
        try:
            self.cursor()
            if id_produto:
                sql = '''SELECT * FROM estoque WHERE id_produto = ?;'''
                return self.cur.execute(sql, (id_produto, )).fetchone()
        except Exception as e:
            print(f'Erro query select produto em estoque: {e}')
            self.desconectar()
  
  
    def select_all_estoque(self):
        '''Query select formatado, mesclando elementos foreign key de outras tabelas.
           O retorno eh uma lista contendo cada um dos produtos cadastrados no estoque.'''
        try:
            self.cursor()
            sql = '''SELECT e.id, p.codigo_de_barra, p.descricao, p.valor_venda, p.valor_custo, f.nome, e.quant_min, e.quant_disp, e.quant_max FROM estoque as e
            INNER JOIN produto as p ON p.id = e.id_produto
            INNER JOIN fornecedor as f ON f.id = p.id_fornecedor; '''
            return self.cur.execute(sql).fetchall()
        except Exception as e:
            print(f'Erro query select all produto em estoque: {e}')
        finally:
            self.desconectar()


    def produto_existe(self, id_produto:int):
        '''Metodo que verifica se um produto existe no estoque.'''
        if self.select_produto_estoque(id_produto):
            return True
        return False