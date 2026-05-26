#Nested if
a=3
b=6
if a<b:
    print("less")
    if b>a:
        print("greater")
        
#example2        
a=3
b=6
if a<b:
    print("less")
    if b==a:
        print("greater")
    else:
        print("true")

#example3
a=9
b=10
if a==b:
    print("less")
    if b>a:
        print("Greater")
    else:
        print("True")
else:
    print("false")

#example4

a=12
b=14
if a<b:
    print("less")
    if a!=b:
        print("not equal")
    else:
         print("true")

#example5
a=int(input("a value: "))
b=int(input("b value: "))
if a>b:
    print("less")
    if b>a:
        print("greater")
    else:
        print("True")
else:
    print("flase")

