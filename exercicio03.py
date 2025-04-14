#receba a quantidade de alunos e as notas, e descubra a media aritmetrica
na = int(input("receba numero de alunos"))
x=1
soma = 0
while x <= na:
    nn = int(input("receba numero da nota"))
    soma = soma + nn
    x=x+1
media = soma/na
print(media)