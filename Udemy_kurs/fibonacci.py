print("Welcome to fibonacci calculator. Enter last number:")
s=int(input())
a,b=1,1
for i in range(3,s+1):
    toplam=a+b
    a=b
    b=toplam
    

print("The last number is {}".format(b))
