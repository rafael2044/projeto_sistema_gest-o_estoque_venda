from DAO.fornecedorDAO import fornecedorDAO
from DAO.produtoDAO import produtoDAO
from DAO.estoqueDAO import estoqueDAO

def inserir_fornecedores():
    dados = [('C3tech', '(11) 3454-5584'), ('Mavint', '(11) 4859-4124'), ('Multilase', '(11) 1234-3312'), ('Hp', '(11) 2485-3123')]
    [fornecedorDAO().insert_fornecedor(x) for x in dados]

def inserir_estoque():
    produtos = [('Mouse Multilase', 5, 20, '1294854738294')]