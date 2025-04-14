#recebe 2 notas e descubra a media, caso a nota nao esteja entre 0 e 10 peça para digitar novamente
nota1 = float(input("receba primeira nota: "))
while nota1 < 0 or nota1 > 10:
    print("numero invalido")
    nota1 = float(input("receba primeira nota: "))
nota2 = float(input("receba segunda nota: "))
while nota2 < 0 or nota2 > 10:
    print("numero invalido")
    nota2 = float(input("receba segunda nota: "))

media=(nota1+nota2)/2
print(media)


