#Condition statements
'''basically there are 3 types
        1]if
        2]elif
        3]else'''
#These are used in different ways
''' 1]if
    2]if-else
    3]if-elif
    4]if-elif-else
    5]multiple elif
    6]multiple if
    7]nested if'''

#if condition by using comparision operators
#<,>,<=,>=<!=,==

#example1
a=10
b=29
if a<b:
    print("true")

#example2
a=3
b=5
if a<=b:
    print("less")

#example3
a=2
b=5
if b>=a:
    print("greater")

#example4
x=7
y=10
if x!=y:
    print("not equal")

#example5
k=10
j=10
if k==j:
    print("equal")

#example6
a=int(input("a value"))
b=int(input("b value"))
if a>b:
    print("a is bigger than b")

#example7
a=int(input("a value = "))
if a>30:
    print("a is biggest")

#example8
a=input("data")
if a=="java":
    print("true")

#if condition by using logical operations
#and,or,not
#example1
a=3
b=9
if a<b and b>a:
    print("true")

#example2
a=5
b=8
if a<=b and b>=a:
    print("b is big")

#example3
a=9
b=12
if a!=b and b!=a:
    print("flase")

#example4
a=3
b=9
if a<b or b>a:
    print("true")

#example5
a=5
b=8
if a<=b or b>=a:
    print("b is big")

#example6
a=9
b=12
if a!=b or b!=a:
    print("flase")
#example 7
a=3
b=9
if not a<b and  b>a:
    print("True")

#example8
a=5
b=8
if not a<=b and b>=a:
    print("b is big")

#example9
a=9
b=12
if  not a!=b and b!=a:
    print("flase")

#if condition by using identity operators
#is, is not
#example1
a=5
if type(a) is int:
    print("if is integer")

#example2
b=6.7
if type(b) is float:
    print("it is float")
#example3
c=input("data")
if type(c) is str:
    print("it is string")

#example4
d=9+7j
if type(d) is complex:
    print("it is complex")

#example5
x=True
if type(x) is bool:
    print("it is boolean")

#if condition by using membership operators
#in, not in
#example1
a=[10,20,30,40,50,60]
if 60 in a:
    print("true")
    
#example2
b=[10,20,30,40,50,60]
if 60 not in b:
    print("true")

#example3
b=[10,20,30,40,50,60]
if 80 not in b:
    print("true")

#example4
g=int(input("enter the number"))
if 60 not in g:
    print("true")

#example5
a=[10,20,30,40,50,60,70]
b=int(input("enter the number"))
if b in a:
    print("True")

#example6
a=complex(input("data"))
if type(a) is complex:
    print("it is complex")


    



