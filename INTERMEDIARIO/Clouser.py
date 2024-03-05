def criar_saudacao(saudacao,nome):
    def saudar():
        return f'{saudacao},{nome}'
    return saudar


s1 = criar_saudacao('Bom Dia','Luana!!!')
s2 = criar_saudacao('Bom Dia','Yasmin!!!')

print(s1())
print(s2())