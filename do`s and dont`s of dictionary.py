Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a={"idnos":[10,20,30],"names":["ismail","subhani","khaja"],"marks":[100,50,60]}
>>> type(a)
<class 'dict'>
>>> print(a)
{'idnos': [10, 20, 30], 'names': ['ismail', 'subhani', 'khaja'], 'marks': [100, 50, 60]}
>>> a.keys()
dict_keys(['idnos', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['ismail', 'subhani', 'khaja'], [100, 50, 60]])
>>> a,items()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a,items()
NameError: name 'items' is not defined. Did you mean: 'iter'?
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['ismail', 'subhani', 'khaja']), ('marks', [100, 50, 60])])
>>> 
>>> #duplicates doesn`t allow
>>> a={"name":"ismail","citty":"vja","name":"ismail"}
>>> type(a)
<class 'dict'>
>>> print(a)
{'name': 'ismail', 'citty': 'vja'}
>>> a
{'name': 'ismail', 'citty': 'vja'}
>>> {'name': 'ismail', 'citty': 'vja'}
{'name': 'ismail', 'citty': 'vja'}

#values may be same but  the keys must be different
KeyboardInterrupt
a={"name":"ismail","citty":"vja","name1":"ismail"}
print(a)
{'name': 'ismail', 'citty': 'vja', 'name1': 'ismail'}
len(a)
3
a.count("name")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'
a.index("name")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.index("name")
AttributeError: 'dict' object has no attribute 'index'
