#if we want to seperate our string to spesific bracket we use split method
s="hello world"
print(s.split(" "))
s2="hello,world"
print(s2.split(','))
#join add specific seperator
l=["lemon","orange","apple"]

print(",".join(l))
print("-".join(l))