print("""
*****************
Calculator 

1 - Addition operation

2 - Subtraction operation

3 - Multiplication operation

4 - Division operation

*****************

""")

a = int(input("First number:"))
b = int(input("Second number:"))

operation = input("operation number click:")

if (operation=="1"):
    print("{} + {} = {}".format(a,b ,a+b))

elif (operation=="2"):
    print("{} - {} = {}".format(a,b ,a-b))

elif (operation=="3"):
    print("{} * {} = {}".format(a,b ,a*b))

elif (operation=="4"):
    print("{} / {} = {}".format(a,b ,a/b))
else:
    print("not operation")