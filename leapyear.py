# year=int(input("enter the year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(" it is leap year")
        else:
            print('it is not leap year')
    else:
        print("it is leap year")
else:
    print("it is not leap year")  


if and nested if


year=int(input("enter the year"))
if year%4==0 and year%100!=0:
    print(year,"is leap year")
elif year%100==0:
    print(year,"is not leap year")
elif year%400==0:
    print(year,"is leap year")
else:
    print("rest of the code")             
