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
    resultado = 1
    for num in args:
        resultado *= num
    return print(resultado)


def div(*args):
    for cont in range(len(args)):
        if cont == 0:
            resultado = args[cont]
        elif args[cont] != 0:
            resultado /= args[cont]
        else:
            resultado = "Não é possível dividir por 0!"
            break
    return print(resultado)      


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
    resp2 = "s"
    nums = list()
    while resp2[0] == "s":
        num = float(input("Digite um número: "))
        nums.append(num)
        resp2 = input("Deseja continuar [s/n]? ").strip().lower()
        if resp2[0] not in ["s", "n"]:
            print("Resposta incorreta!")
            resp2 = input("Deseja continuar [s/n]? ").strip().lower()  
    if resp == 1:
        return soma(*nums)
    elif resp == 2:
        return sub(*nums)
    elif resp == 3:
        return mult(*nums)
    else:
        return div(*nums)


calc()
