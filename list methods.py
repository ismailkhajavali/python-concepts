Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #List method
>>> a=[33,23.56,"python",7+9j,True,False]
>>> print(a)
[33, 23.56, 'python', (7+9j), True, False]
>>> 
>>> #append()
>>> a=["python","java","c","c++"]
>>> a.append("kotlin")
>>> a
['python', 'java', 'c', 'c++', 'kotlin']
>>> 
>>> a.append("ds","ai")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.append("ds","ai")
TypeError: list.append() takes exactly one argument (2 given)
>>> a.append(["ds","dl"])
>>> a
['python', 'java', 'c', 'c++', 'kotlin', ['ds', 'dl']]
>>> 
>>> #extend()
>>> a=["ravi","raju","rahim"]
>>> a.extend("gethha","madhu")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.extend("gethha","madhu")
TypeError: list.extend() takes exactly one argument (2 given)
a.extend(["gethha","madhu

          
SyntaxError: unterminated string literal (detected at line 1)
a.extend(["gethha","madhu"])
          
a
          
['ravi', 'raju', 'rahim', 'gethha', 'madhu']

#insert()
          
a.insert(2,"ramu")
          
a.
          
SyntaxError: invalid syntax
a
          
['ravi', 'raju', 'ramu', 'rahim', 'gethha', 'madhu']


#index()
          
a=["html","css","js"]
          
a.index("css")
          
1

#copy()
          
b=a.copy()
          
b
          
['html', 'css', 'js']
#clear()
          
a.clear()
          
a
          
[]

#sort()
          
a=["papaya","apple","banana","mango"]
          
a.sort()
          
a
          
['apple', 'banana', 'mango', 'papaya']
b=[23,23,2,55,785,64455,222145563]
          
b.sort()
          
b
          
[2, 23, 23, 55, 785, 64455, 222145563]

#reverse()
          
a=["c","c++","java","python"]
          
a.reverse()
          
a
          
['python', 'java', 'c++', 'c']

b=[9,8,7,6,5,4,3,2,1]]
         
SyntaxError: unmatched ']'
b.reverse()
         
b
         
[222145563, 64455, 785, 55, 23, 23, 2]
z=[9,8,7,6,5,4,3,2,1]
         
z.reverse()
         
z
         
[1, 2, 3, 4, 5, 6, 7, 8, 9]

#pop()
         
a=[4,5,6,7,8,9]
         
a.pop()
         
9
a
         
[4, 5, 6, 7, 8]
a.pop(6)
         
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.pop(6)
IndexError: pop index out of range
a.remove(6)
         
a
         
[4, 5, 7, 8]

#count()
         
z=[11,23,34,45,67,23,45]
         
z.count(23)
         
2
