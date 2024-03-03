def soma(*args):
    total = 0
    for numero in args:
        print('Numero Total',total,numero)
        total = total + numero
        print("Soma Total:",total)
    print(total)


soma(1,2,3,4,5,6,7)