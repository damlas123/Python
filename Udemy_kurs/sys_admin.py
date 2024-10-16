print("******************Welcome the system******************"),
sys_user_name="Damla"
sys_password= "12345"
enter_number=3
while enter_number!=0:
    admin_name=input("enter your user name:")
    ad_pas=input("enter password")
    if(sys_user_name!=admin_name and ad_pas==sys_password):
        print("You enter wrong user name")
        enter_number -=1
    elif (sys_password != ad_pas and sys_user_name==admin_name):
        print("You enter wrong password")  
        enter_number-=1

    elif (sys_password!=ad_pas and sys_user_name!=admin):
        print("You enter wrong information....")
        enter_number-=1
    
    else:
        print("Logging system.........")
        break
    if(enter_number==0):
       print("The limit is finishedokıjuhygtf")
    