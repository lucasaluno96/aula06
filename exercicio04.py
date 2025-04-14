#receba 2 numeros, o segundo nao pode ser zero se nao peça novamente e divida
n1 = int(input("receba primeiro numero"))
n2 = int(input("receba segundo numero"))
divisao=0
while n2 == 0:
    n2 = int(input("receba segundo numero"))
divisao=n1/n2
print(divisao)