
while True:
    def soma (n1,n2):
        som = n1 + n2
        print(som)
    def mult (n1,n2):
        multi = n1 * n2
        print(multi)
    def divisao (n1,n2):
        divi = n1 / n2
        print(divi)
    def subtracao (n1,n2):
        sub = n1 - n2
        print(sub)
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
    elif op != "1" and op != "2" and op != "3" and op != "4" and op != "5" :
        print("Erro!")
        continue
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    if op == "1":
        soma(n1 , n2)
    elif op == "2":
       subtracao(n1 , n2)
    elif op == "3":
       divisao(n1 ,n2)
    else: 
        mult(n1 , n2)
