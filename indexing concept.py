Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing in python
# Two types
#1)Positive indexing
a='vijayawada'
a[5]
'a'
a[0]+a[1]+a[2]+a[3]+a[4]
'vijay'

#positive  indexing on line
a='I am in class'
a[2]
'a'
a[1]
' '
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
#example1
b='simple is better than complex'
b[0]+b[1]+b[2]+b[3]+b[4]+b[5]
'simple'
b[22]+b[23]+b[24]+b[25]+b[26]+b[27]+b[28]
'complex'
b[10]+b[11]+b[12]+b[13]+b[14]+b[15]+
SyntaxError: invalid syntax
b[10]+b[11]+b[12]+b[13]+b[14]+b[15]
'better'
#Example 2
z='vijayawada is a royal city'
z=[22]+z[23]+z[24]+z[25]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    z=[22]+z[23]+z[24]+z[25]
TypeError: can only concatenate list (not "str") to list
>>> z[22]+z[23]+z[24]+z[25]
'city'
>>> 
>>> #2)Negative indexing
>>> x='guntur'
>>> x[-1]+x[-2]
'ru'
>>> 
>>> #Negatuve indexing on line
>>> #example 1
>>> a='codegnan IT solutions'
>>> a[-9]+a[-8]+a[-7]+a[-6]
'solu'
>>> a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+
SyntaxError: invalid syntax
>>> a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'solutions'
>>> a[-21]+a[-20]+a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'codegnan'
>>> 
>>> #example2
>>> b='vizag is a city of destiny'
>>> b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'destiny'
>>> b[-15]+b[-14]+b[-13]+b[-12]
'city'
