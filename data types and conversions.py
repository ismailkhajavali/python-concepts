Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Data Types in python
>>> #There are 5 different types
>>> #1]Integer->1,2,33,222
>>> #2]float->2.3,0.6,8.7
>>> #3]string->'python',"code",'''codegnan'''
>>> #4]complex->real+imaginary part
>>> #example->5+9j,3j+4,
>>> #boolean->True,False
>>> 
>>> #datatype conversions
>>> #integer[int]
>>> int(9)
9
>>> int(4.6)
4
>>> int('hello')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    int('hello')
ValueError: invalid literal for int() with base 10: 'hello'
>>> int(4+9j)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    int(4+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
int(False)
0

#float converion
float(6)
6.0
float(2.6)
2.6
float('hello')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    float('hello')
ValueError: could not convert string to float: 'hello'
float(6+7j)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(6+7j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0

#string conversion[str]
str(1)
'1'
str(1.5)
'1.5'
str('hello')
'hello'
str(8+5j)
'(8+5j)'
str(True)
'True'
str(False)
'False'

#complex conversion
complex(22)
(22+0j)
complex(1.6)
(1.6+0j)
complex('good')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    complex('good')
ValueError: complex() arg is a malformed string
complex(8+5j)
(8+5j)
complex(True)
(1+0j)
complex(False)
0j

#boolean conversion[bool]
bool(23)
True
bool(1.7)
True
bool('hello')
True
bool(3+7j)
True
bool(True)
True
bool(False)
False
