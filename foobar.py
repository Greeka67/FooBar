def one(a,b):
    if a%3!=0:
        print(a,"foo")
    else:
        print(a,"bar")
    a+=1
    if a<=b:
        one(a,b)


x=input('Введите целое число больше 0 \n')
if x.isdigit() and int(x)>0:
    print("ввод верный")
    x=int(x)
    one(1,x)
else:
    print("неверный ввод")
