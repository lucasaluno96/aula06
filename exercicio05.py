pin=123
tentativa= 3
su=int(input("digite a senha: "))
while su != pin:
    su=int(input("digite a senha: "))
    tentativa-=1
    if tentativa ==1:
        print("acesso negado")
        break
if su == pin:
    print("acesso liberado")
