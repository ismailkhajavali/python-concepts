Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets
a={1,2.4,"python",5+7j,True,False}
print(a)
{False, 1, 2.4, (5+7j), 'python'}
type(a)
<class 'set'>

#add()
a={4,5,6,7,8,9,10}
a.add(20)
a
{4, 5, 6, 7, 8, 9, 10, 20}

#issubset()
a={2,3,4,5,6,7,8,9,10}
b={6,7,8,9,10}
a.issubset(b)
False
b.issubset(a)
True

#issuperset

#issuperset()
x={7,8,9,4,5,6,1,2,3}
y={4,5,6,1,2,3}
x.issuperset(y)
True
y.issuperset(x)
False

#union()
a={4,5,6,7,8,9,1,2,3}
b={1,2,3,4,5,6}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a.
SyntaxError: invalid syntax
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}

#intersection()
a={6,7,8,9,10,11,12}
b={10,11,12,13,14,15,16}
a.intersection(b)
{10, 11, 12}
b.intersection(a)
{10, 11, 12}

#update()
a={2,3,4,5,6,7,8,9,10,11}
b={6,7,8,9,10,11,12,13}
a.update(b)
a
{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
b.update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

#difference()
a={100,200,300,400,500,600,700}
b={500,600,700,800,900,400,500}
a.difference(b)
{200, 100, 300}
b.difference(a)
{800, 900}

#symmetric_difference()
a={2,3,4,5,6,7,8,9,10,11,12,13}
b={6,7,8,9,10,11,12,13,14,15,16}
a.symmentric_difference(b)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.symmentric_difference(b)
AttributeError: 'set' object has no attribute 'symmentric_difference'. Did you mean: 'symmetric_difference'?
a.symmetric_difference(b)
{2, 3, 4, 5, 14, 15, 16}
b.symmetric_difference(a)
{2, 3, 4, 5, 14, 15, 16}

#difference_update()
a={1,2,3,4,5,6,7,8,9}
b={4,5,6,7,8,9,10}
a.difference_update(b)
a
{1, 2, 3}
b
{4, 5, 6, 7, 8, 9, 10}
b.difference_update(a)
>>> b
{4, 5, 6, 7, 8, 9, 10}
>>> 
>>> #intersection_update
>>> a={11,12,13,14,15,16}
>>> b={12,13,14,15,16,17,18}
>>> a.intersection_update(b)
>>> a
{12, 13, 14, 15, 16}
>>> b
{16, 17, 18, 12, 13, 14, 15}
>>> b.interection_update(a)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    b.interection_update(a)
AttributeError: 'set' object has no attribute 'interection_update'. Did you mean: 'intersection_update'?
>>> b.intersection_update(a)
>>> b
{12, 13, 14, 15, 16}
>>> 
>>> #symmetric_difference_update()
>>> a={11,12,13,14,15,16}
>>> b={12,13,14,15,16,17,18}
>>> a.symmetric_difference_update(b)
>>> a
{17, 18, 11}
>>> b.symmetric_difference_update(a)
>>> b
{16, 11, 12, 13, 14, 15}

#copy()
a={3,4,5,6,7,8}
a.copy()
{3, 4, 5, 6, 7, 8}
#clear()
a.clear()
a.
SyntaxError: invalid syntax
a
set()
#poop()
a.pop(6)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    a.pop(6)
TypeError: set.pop() takes no arguments (1 given)
a.pop(9)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a.pop(9)
TypeError: set.pop() takes no arguments (1 given)
a.opo(5)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a.opo(5)
AttributeError: 'set' object has no attribute 'opo'
a.pop()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a.pop()
KeyError: 'pop from an empty set'
a
set()

#remove()
a
set()

#add()
a.add(1,2,3,4,5,6)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    a.add(1,2,3,4,5,6)
TypeError: set.add() takes exactly one argument (6 given)

#discard()
a={3,4,5,6,7,8}
a.discard(8)
a
{3, 4, 5, 6, 7}

#dijoint(
#disjoint()
a={1,2,3,4,5,6,7}
b={6,7,8,9,10,11,12}
a.isdisjoint(b)
False

#length()
a={3,4,5,6,7,8}
a.len(6)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    a.len(6)
AttributeError: 'set' object has no attribute 'len'
len(a)
6
