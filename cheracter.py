ch=input("enter a cheracter")
ch=ch.lower()
if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
    print("it is vowel")
elif ch>="a" and ch<="z":
    print("it is consnent")
elif ch>="0" and ch>="9":
    print("it is number")
else:
    print("it is special character")        