language=input("enter language")
account=input("enter account type")
pincode=int(input("enter pincode"))
balance=int(input("enter the balnce"))
if language=="hindi" or language=="english" or language=="tamil" or language=="malyalam":
    print("print language accepted")
    if account=="saving" or account=="current":
        print("saving account")
        if pincode==9955:
            print("correct password")
            if balance>15000:
                print("you can not withdrow")
            else:
                print("you can  withdrow")       
        else:
            print("incorrect password")
    else:
        print("current account")
else:
    print("language not accepted")                                