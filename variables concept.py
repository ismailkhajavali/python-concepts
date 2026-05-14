Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variable Rules
#1
#variabler start with a letteror underscore
a=12
print(a)
12
_a=11
print(_a)
11
#variable cannot start with numbers
3=4
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
23=23
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a6=12
print(a6)
12
#keywords should not use in variable names
a12345678=100
print(a12345678)
100
if=10
SyntaxError: invalid syntax
#if is a keyword
while=12
SyntaxError: invalid syntax
#here while is a keyword
for=23
SyntaxError: invalid syntax
#for is a keyword

#variable can start with any alphabet name
city="vij"
print(city)
vij
mobileno=8019807297
print(mobileno)
8019807297

fname="ismail"
\
lname="khajavali"
print(fnamme+lname)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(fnamme+lname)
NameError: name 'fnamme' is not defined. Did you mean: 'fname'?
print(fname+lname)
ismailkhajavali
print(fname+" "+lname)
ismail khajavali
print(fname,lname)
ismail khajavali
#The above is example to pass 2 variables in a single line
# Here are the example for assigning same value to 3 different variables
a,b,c=5
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a,b,c=5
TypeError: cannot unpack non-iterable int object
a=b=c=5
print(a,b,c)
5 5 5

#here is the example to assign 3values to 3variables
a,b,c=2,3,4
print(a,b,c)
2 3 4

# here is the example for assigning multiple values to single variable
a=1,2,3,4,5
print(a)
(1, 2, 3, 4, 5)
>>> 
>>> #delete keyword
>>> z=100
>>> print(z)
100
>>> del(z)
>>> print(z)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print(z)
NameError: name 'z' is not defined
>>> #cannot use any special characters
>>> @=1100
SyntaxError: invalid syntax
>>> $=123
SyntaxError: invalid syntax
>>> #use only underscore
>>> _=10
>>> print(_)
10
>>> 
>>> #dont give spaces between words,insteed give underscore
>>> first name="ismail"
SyntaxError: invalid syntax
>>> first_name="ismail"
>>> print(first_name)
ismail
