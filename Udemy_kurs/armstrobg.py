print("enter number:")
s=int(input())
b=0
temp=s
while (temp!=0):
    temp //=10
    b+=1
total=0
temp=s
while (s!=0):
    digit=s%10
    total+= (digit)**b
    s//=10

if(total==temp):
    print("this number is armstrong")
else:
    print("this number is not a armstrong")