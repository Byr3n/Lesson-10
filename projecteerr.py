n=int(input("Enter a number"))
e=int(input("Enter a exponent "))
f=0
for i in range(0,n,n):
    f=f+i
    a=n**e+i
print(a)