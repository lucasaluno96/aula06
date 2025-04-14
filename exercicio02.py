#receba 5 numeros e encontre a media aritmetrica
x = 1
soma = 0
while x <= 5:
    num = int(input("receba um numero"))
    soma = soma + num
    x=x+1
media = soma/5
print(media)