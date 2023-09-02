class Produto:
    def __init__(self, id, cod_barra, descricao, fornecedor, valor_venda, valor_custo):
        self.id = id
        self.cod_barra = cod_barra
        self.descricao = descricao
        self.fornecedor = fornecedor
        self.valor_venda = valor_venda
        self.valor_custo = valor_custo
        
    def retornar_lista_produto(self):
        return [self.id, self.cod_barra, self.fornecedor, self.valor_venda, self.valor_custo]
    
        