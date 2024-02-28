class Jogo:
    def __init__(self):
        condicao = True
    def escolha_metodo(self):
        print("Escolha um metodo: \na)Soma\nb)Subtração\nc)Divisão\nd)Multiplicação")
        self.metodo = input("Digite a letra aqui:")
        if self.metodo not in {'a', 'b', 'c', 'd'}:
            print("Opção inválida. Escolha uma das letras a, b, c ou d.")
            return False
        self.x = float(input("Digite o primeiro número: "))
        self.y = float(input("Digite o segundo número: "))
        return True

    def soma(self):
        if self.metodo == "a":
            return self.x+self.y

    def diminui(self):
        if self.metodo == "b":
            return self.x - self.y
    def dividi(self):
        if self.metodo == "c":
            return self.x / self.y
    def multiplica(self):
        if self.metodo == "a":
            return self.x + self.y



jogo = Jogo()
jogo.escolha_metodo()
resultado =None

if jogo.metodo == "a":
    resultado = jogo.soma()

if jogo.metodo == "b":
    resultado =jogo.diminui()

if jogo.metodo == "c":
    resultado =jogo.dividi()

if jogo.metodo == "c":
    resultado =jogo.multiplica()

if resultado is not None:
    print("Resultado:",resultado)