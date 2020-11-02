ch=input("entert alphabet")
ch=ch.lower()
if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
    print("is a vowel")
elif ch>="a" and ch<="z":
    print("is a consonent")
elif ch>="0" and ch<="9":
    print("is a zero")   
else:
    print("is a special character")    
