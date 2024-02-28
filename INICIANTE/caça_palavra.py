palavra = "perfume"
nome_palavra = ''

while True:
    nome = input("Digite uma letra: ")
    if len(nome) > 1:
        print("Digite apenas uma letra: ")

    if nome in palavra:
        nome_palavra += nome

    palavra_formada = ''
    for letra in palavra:
        if letra in nome_palavra:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    print("Palavra formada: ",palavra_formada)
    if palavra_formada == palavra:
        print("Voce Ganhou!!")

