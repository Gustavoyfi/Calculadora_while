while True:
    print("MENU CALCULADORA")
    print("1 - SOMA")
    print("2 - SUBTRAÇÃO")
    print("3 - DIVISÃO")
    print("4 - MULTIPLICAÇÃO")
    print("5 - SAIR")
    op = input("Digite a operação matemática desejada: ")
    if op == "5":
        print("Você saiu da calculadora! ")
        break

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if op == "1":
        resultado = num1 + num2
        print(f"O resultado é : {num1} + {num2} = {resultado}")
    elif op == "2":
        resultado = num1 - num2
        print(f"O resultado é : {num1} - {num2} = {resultado}")
    elif op == "3":
        resultado = num1 / num2
        print(f"O resultado é : {num1} / {num2} = {resultado}")
    elif op == "4":
        resultado = num1 * num2
        print(f"O resultado é : {num1} * {num2} = {resultado}")
    else:
        print("Operação Invalída")