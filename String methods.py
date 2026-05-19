Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #String methods
>>> #1]len()
>>> a="python"
>>> len(a)
6
>>> b="codegnan IT solutions"
>>> len(b)
21
>>> c=""
>>> len(c)
0
>>> d=" "
>>> len(d)
1
>>> 
>>> #2]count()
>>> a="Twinkel twinkel little star"
>>> count(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> a.count("twinkel")
1
>>> a.count("k")
2
>>> a.count(" ")
3
a.count("e")
3

#3]find a string
a="python"
a.find(2)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.find(2)
TypeError: find() argument 1 must be str, not int
a(2)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a(2)
TypeError: 'str' object is not callable
a.find("2")
-1
a.find("5")
-1
a.find("3")
-1
a[2:4]
'th'

#4replace()
#4]replace()
a="wait untill you scceed"
a.replace("wait","work")
'work untill you scceed'

#5]strip()
#There are two types
#lstrip()
#rstrip()
a="     Ismail      "
a.strip()
'Ismail'

a.lstrip()
'Ismail      '
a.rstrip()
'     Ismail'

#6]upper()
a="codegnan"
a.upper()
'CODEGNAN'

#7]lower()
b="PYTHON"
b.lower()
'python'

#8]capitalise()
c="python course"
c.capitalize()
'Python course'

#9]title()
c.title()
'Python Course'

#10]split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']

#11]join()
b="shaik","ismail","khajavali"
b.join()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    b.join()
AttributeError: 'tuple' object has no attribute 'join'
join(a)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    join(a)
NameError: name 'join' is not defined
join(b)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    join(b)
NameError: name 'join' is not defined
"".join(b)
'shaikismailkhajavali'
" ".join(b)
'shaik ismail khajavali'

#12]concatenation
a="python"
b="course"
print(a+b)
pythoncourse
