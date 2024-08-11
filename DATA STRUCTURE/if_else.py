'''x=int(input("Enter a number"))
if x%2==0 & x%3==0:
  if x==6 :
    print("your number is 6")
  else :
      print("your number is a multiple of 6")
elif x%2==0 : 
    print("your number is a multiple of 2")
else:
    print("your number is a multiple of 3")

print("your program is executed")'''
#ternary conditionals
# if else tek satırda olunca meydana gelene durumun ismi
cevap=input(" is the entering number 2 y/n ")
x=2 if cevap=="y" else 0
print(x)