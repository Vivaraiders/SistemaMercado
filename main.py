from Models.Mercado import Mercado

def menu():
    print("\n==== MERCADO ====")
    print("1 - Criar setor")
    print("2 - Deletar setor")
    print("3 - Criar produto")
    print("4 - Deletar produto")
    print("5 - Listar tudo")
    print("0 - Sair")


mercado = Mercado("Mercado do Samuel")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do setor: ")
        mercado.criar_setor(nome)

    elif opcao == "2":
        nome = input("Nome do setor: ")
        mercado.deletar_setor(nome)

    elif opcao == "3":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        setor = input("Nome do setor: ")

        mercado.cadastra_produto(nome, preco, quantidade, setor)

    elif opcao == "4":
        setor = input("Nome do setor: ")
        produto = input("Nome do produto: ")
        mercado.deletar_produto(setor, produto)

    elif opcao == "5":
        mercado.listar()

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")