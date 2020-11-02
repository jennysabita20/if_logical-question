age1=int(input("enter the number"))
age2=int(input("enter the number"))
age3=int(input("enter the number"))
if age1>age2 and age1>age3:
    print("age1 greater than" "age2,age3")
elif age2>age1 and age2>age3:   
    print("age2 is greater than" "age1,age3")
else:
    print("age3 is greater than" "age1,age2")     