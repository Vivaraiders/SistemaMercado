from Models.Setor import Setor
from Models.Produto import Produto

class Mercado:

    def __init__(self, nome):
        self.nome = nome
        self.setores = {}

    def cadastra_produto(self, nome_produto, preco, quantidade, nome_setor):

        # Verifica se o setor existe
        if nome_setor in self.setores:
            setor_obj = self.setores[nome_setor]
        else:
            setor_obj = Setor(nome_setor)
            self.setores[nome_setor] = setor_obj
            print(f"Setor '{nome_setor}' criado.")

        # Cria o objeto Produto
        produto_obj = Produto(nome_produto, preco, quantidade)

        # Adiciona no setor
        setor_obj.adicionar_produto(produto_obj)

        print(f"Produto '{nome_produto}' adicionado ao setor '{nome_setor}'.")

    def deletar_produto(self, nome_setor, nome_produto):
        if nome_setor in self.setores:
            setor = self.setores[nome_setor]

            for produto in setor.produtos:
                if produto.nome == nome_produto:
                    setor.produtos.remove(produto)
                    print("Produto deletado com sucesso!")
                    return

            print("Produto não encontrado.")
        else:
            print("Setor não encontrado.")   

    def criar_setor(self, nome_setor):
        if nome_setor not in self.setores:
            self.setores[nome_setor] = Setor(nome_setor)
            print(f"Setor '{nome_setor}' Criado")

    def deletar_setor(self, nome_setor):
        if nome_setor in self.setores:
            del self.setores[nome_setor]
            print("Setor deletado com sucesso!")
        else:
            print("Setor não encontrado.")

    def listar(self):
        if not self.setores:
            print("Nenhum setor cadastrado.")
            return

        for nome_setor, setor in self.setores.items():
            print(f"\n=== Setor: {nome_setor} ===")
            setor.listar_produtos()