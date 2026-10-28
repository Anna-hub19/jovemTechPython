produtos = ["Teclado", "Monitor", "Mouse"]
print("====ESTOQUE FACIL====")
print("1- Listar produtos")
print("2- Cadastrar produto")
print("3- Atualizar produto")
print("4- Excluir produto")

opcao = input("escolha a opção:").capitalize()
while opcao != "0":
# ----------------------------------------------------------------------
# listar produto
    if opcao == "1":
        print("produtos cadastrados", produtos)

    #cadastrar produto
    elif opcao == "2":
        novo_produto = input("digite o nome do produto: ").capitalize()
        produtos.append(novo_produto)
        print("produto cadastrado")
        print(produtos)

    # atualizar produto
    elif opcao == "3":
        produto_antigo = input("qual produto deseja atualizar?")
        if produto_antigo in produtos:
            novo_produto = input("digite o nome:").capitalize()
            posicao = produtos.index(produto_antigo)
            produtos[posicao] = novo_produto
            print("produto atualizado")
            print(produtos)


    # excluir produto
    elif opcao == "4":
        produto_excluir = input("qual produto deseja excluir?").capitalize()
        if produto_excluir in produtos:
                produtos.remove(produto_excluir)
                print("produto excluido")
                print(produtos)

    else:
        print("opção invalida")

    opcao = input("escolha a opção:")
