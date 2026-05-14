Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Slicing in python
>>> #two types
>>> #1) positive Slicing
>>> a='work hard until you succeed'
>>> a[20:27]
'succeed'
>>> a[10:15]
'until'
>>> a[8:4]
''
>>> a[6:9]
'ard'
>>> a[5:9]
'hard'
>>> 
>>> #Negative scling
>>> z='The art of code'
>>> z[-15:-11]
'The '
>>> z[-15:-13]
'Th'
>>> z[-15:-12]
'The'
>>> a[-11:-8]
'you'
>>> z[-11:-8]
'art'
z=[-7:-5]
SyntaxError: invalid syntax
z[-7:-5]
'of'
'of'
'of'
z[-4]
'c'
z[-4:]
'code'

#example 2



#example 2
x='Time is very precious'
x[-13:-9]
'very'
x=[-21:-17]
SyntaxError: invalid syntax
x=[-21:-17]
SyntaxError: invalid syntax
x[-21:-17]
'Time'
