vez=0
num=int(input("receba um numero: "))
for x in range(1,num+1):
    for num in range(1,x+1,1):
        print(x, end=" ")
    print()