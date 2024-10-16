print("*************WElcome to the Bankatar*************")
balance=2000
print("1-Look your balance\n2-Deposit money\n3-Withdrawal money\nFor exit enter 'q'")

while True:
    selection=input()
    if(selection=='q'):
        print("Thanks your using our bank.....")
        break

    elif(selection=='1'):
        print("Your balance is {} .".format(balance))
    elif(selection=='2'):
        print("enter deposit money:")
        deposit=int(input())
        balance+=deposit
        print("New balance is {}".format(balance))
    elif(selection=='3'):
        print("enter the money which withdrawal:")
        w=int(input())
        if(w>balance):
           print("You don't have enough money")
        else:
            balance-=w
            print("New balance is {}".format(balance))
         
    else:
        print("you entered wrong selection...")