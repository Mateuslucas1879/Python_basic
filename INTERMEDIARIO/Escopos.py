x= 1 

def escopo():
    x = 10

    def outro_escopo():
        x=11
        y=2
        print(x,y)

    outro_escopo()
    print(x)


print(x)
escopo()
print(x)