s1=int(input("enter angle"))
s2=int(input("enter angle"))
s3=int(input("enter angle"))
if s1==s2==s3:
    print("equilataral triangle")
elif s1==s2 or s2==s3 or s3==s1:
    print("isosceles")    
else:
    print("scalane")    
