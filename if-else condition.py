#if-else condition using comparision
#example1
a=3
b=7
if b>a:
    print("true")
else:
    print("false")

#example2
a=3
b=7
if b<=a:
    print("true")
else:
    print("false")

#example3
a=3
b=7
if b>=a:
    print("true")
else:
    print("false")

#example4
a=3
b=7
if b!=a:
    print("true")
else:
    print("false")

#example5
a=3
b=6
if b==a:
    print("true")
else:
    print("false")

#if-else using logical opeerators
#example1
a=10
b=15
if a<b and b>a:
    print("true")
else:
    print("false")


#example2
a=10
b=15
if a<=b and b>=a:
    print("true")
else:
    print("false")


#example3
a=10
b=15
if a!=b or b==a:
    print("true")
else:
    print("false")


#example4
a=10
b=15
if not a<=b and b>=a:
    print("true")
else:
    print("false")

#if-else using identity operators

#example1
a=10
if type(a) is int:
    print("true")
else:
    print("false")

#example1
a=10
if type(a) is not int:
    print("true")
else:
    print("false")

#if-else using membership operator
#example1
a=[2,3,4,5,6,7,8]
b=int(input("a value"))
if b in a:
    print("true")
else:
    print("false")

#example2
a=[2,3,4,5,6,7,8]
b=int(input("a value"))
if b  not in a:
    print("true")
else:
    print("false")














