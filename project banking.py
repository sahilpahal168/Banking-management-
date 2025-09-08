
import random



account={}


def newuser():
    name=input("Enter your name")
    address=input("Enter you address")
    pin=input("Set a 4 digit pin")
    
    account_no=str(random.randit(100000, 999999))
    while account_no  in account:
        account_no=str(random.randit(100000, 999999))

    account[account_no] = {"name": name, "address": address, "pin": pin, "balance": 0.0}

    print("Your account has been created")
    print("your account no is:", {account_no})
    print("you pin is:", {pin})


def existinguser():
    name=input("enter your name")
    account_no=input("enter your account no.")
    pin=input("enter your pin")

    if(account_no in account and account[account_no]["name"] == name and account[account_no]["pin"] == pin):
        print("Welcome {name}!")

        print("1. Credit")
        print("2. debit")
        print("3. check balance")
        print("4, delete account")

        choice=int(input("enter your choice"))

        if(choice==1):
            amount=int(input("enetr the amount you want to credit"))
            account[account_no]["balance"]= account[account_no]["balance"]+amount
            print("amount credit.your current balamce is.",{"balance"})

        elif(choice==2):
            amount=int(input("enter amount whihc you want to debit"))
            account[account_no]["balance"]=account[account_no]["balance"]-amount
            print("amount debit. you balance is: ", {account[account_no]["balance"]})

        elif(choice==3):
            print("you account balance is :", {account[account_no]["balance"]})

        elif(choice==4):
            confirm=input("do you want to delete your account, yes/no")
            if(confirm=="yes"):
                print("your account has been deleted")
            else:
                print("invalid choice")
        else:
            print("invalid choice")
    else:
        print("select the correct option")



def main():
    print("Weclometo bank")
    print("1. New User")
    print("2. Existing User")
    print("3. exit")
    option=int(input("Enter you option"))
    if(option==1):
        newuser()
    elif(option==2):
        existinguser()
    elif(option==3):
        print("Thank you")
    else:
        print("invalid choice")




main()
