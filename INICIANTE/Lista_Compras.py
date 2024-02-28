lista_compras = []
salvar_lista = ''
condicao = True

while condicao:
    print("=+"*20)
    opcao = input("[1] ADICIONAR PRODUTO\n[2] REMOVER PRODUTO\n[3] LISTAR PRODUTOS\nDIGITE UMA OPÇÃO:")

    if opcao == "1":
        compra = input("ADCIONE PRODUTO: ")
        lista_compras.append(compra)
        print("Produto adicionado com sucesso!")

    if opcao == "2":
        if lista_compras:
            remover = input("DIGITE O NUMERO DO ITEM QUE DESEJA REMOVER:")
            if remover.isdigit():
                indice = int(remover)
                if 0 <= indice < len(lista_compras):
                    lista_compras.pop(indice)
                    print("Produto removido com sucesso!")

    if opcao == "3":
        for indice, compra in enumerate(lista_compras):
            print(indice, compra)


    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break

