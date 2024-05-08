def soma(n1,n2):
    return n1 + n2 
def subtracao(n1,n2):
    return n1 - n2
def mulriplicacao(n1,n2):
    return n1 * n2
def divisao(n1,n2):
    return n1/n2
def menu():
    print("MENU CALCULADORA\n" "1 - SOMA\n" "2 - SUBTRAÇÃO\n" "3 - DIVISÃO\n" "4 - MULTIPLICAÇÃO\n" "5 - SAIR")
    op = input("Digite a operação matemática desejada: ")
    return op
    

while True:
    op = menu()
    if op == "5":
        print("Você saiu da calculadora! ")
        break
    elif op != "1" and op != "2" and op != "3" and op != "4" and op != "5" :
        print("Erro!")
        continue
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    if op == "1":
        print(f"O valor da soma é: {soma(n1,n2)}")
    elif op == "2":
       print(f"O valor da subtração é: {subtracao(n1,n2)}")
    elif op == "3":
       while n2 == 0:
           print("Opção inválida")
           n1 = int(input("Digite o primeiro número: "))
           n2 = int(input("Digite o segundo número: "))
       print(f"O valor da divisão é: {divisao(n1,n2)}")
    else: 
        print(f"O valor da multiplicação é: {mulriplicacao(n1,n2)}")
