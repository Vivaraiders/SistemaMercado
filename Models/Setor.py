from Models.Produto import Produto

class Setor:
    def __init__(self,nome):
        self.nome = nome
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(f"nome do produto: {produto.nome}\n preço do produto: {produto.preco}\n quantidade de produtos: {produto.quantidade}")