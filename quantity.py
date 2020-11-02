quantity=int(input("enter the quqntity"))
if quantity%100>1000:
    print("cost is",(quqntity*100))-(.1*quantity*100)
else:
    print("cost is",quantity*100)    