from random import randint

n=int(input("enter n:"))
a=[]
for i in range (n):
    x=randint(0,100)
    if x not in a:
        a.append(x)

print(a)