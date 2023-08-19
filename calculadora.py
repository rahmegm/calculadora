def soma(*args):
    resultado = 0
    for num in args:
        resultado += num
    return print(resultado)


def sub(*args):
    for cont in range(len(args)):
        if cont == 0:
            resultado = args[cont]
        else:
            resultado -= args[cont]
    return print(resultado)


def mult(*args):


def div(*args):


def calc():
    print("Seja bem vindo a calculadora estudantil!")
    print("As operações possiveis são:")
    print("1: Adição")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    resp = int(input("Escolha a operação a ser usada (1 a 4): "))
    if resp not in [1, 2, 3, 4]:
        print("Opção não encontrada!")
        resp = int(input("Escolha a operação a ser usada (1 a 4): "))
    