total=0
while True:
    print("enter a number for exit enter 0")
    s=int(input())
    if(s!=0):
        total+=s
    else:
        break

print("Total: {}".format(total))