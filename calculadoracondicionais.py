n1 = float(input("Digite um número X: "))
op = input("Digite uma operação: ")
n2 = float(input("Digite um número Y: "))
resposta = input("Se deseja sair escvreva [S] para sim e [N] para não: ")
if resposta == "N":
    if op == "+" :
        resultado = n1 + n2 
    elif op == "-" :
        resultado = n1 - n2
    elif op == "/" :
        resultado = n1 / n2
    elif op == "*" :
        resultado = n1 * n2
        print(str(n1) + " " + str(op) + " " + str(n2) + " = " + str(resultado))
    elif op != "-"  and op != "+"  and op != "*" and op != "/":
        print ("Operação Invalída!")
    print(str(n1) + " " + str(op) + " " + str(n2) + " = " + str(resultado))
else:
    print("Você saiu da calculadora!")
