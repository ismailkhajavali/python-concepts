Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dict()
>>> a{"Name":"ismail","passing year":2026,"month":"may"}
SyntaxError: invalid syntax
>>> a={"Name":"ismail","passing year":2026,"month":"may"}
>>> a["ismail"]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a["ismail"]
KeyError: 'ismail'
>>> a["Name"]
'ismail'
>>> 
>>> #keys()
>>> a.keys()
dict_keys(['Name', 'passing year', 'month'])
>>> 
>>> #values()
>>> a.values()
dict_values(['ismail', 2026, 'may'])
>>> 
>>> #items()
>>> a,items()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a,items()
NameError: name 'items' is not defined. Did you mean: 'iter'?
>>> a.item()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.item()
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
a.items()
dict_items([('Name', 'ismail'), ('passing year', 2026), ('month', 'may')])

#update()
a.update({"course":"python"})
a
{'Name': 'ismail', 'passing year': 2026, 'month': 'may', 'course': 'python'}
a.update({"initial":"Shaik","college":"vignan"})
a
{'Name': 'ismail', 'passing year': 2026, 'month': 'may', 'course': 'python', 'initial': 'Shaik', 'college': 'vignan'}

#setdefault()
a.setdefault("name","ismail")
'ismail'
a
{'Name': 'ismail', 'passing year': 2026, 'month': 'may', 'course': 'python', 'initial': 'Shaik', 'college': 'vignan', 'name': 'ismail'}
b={"last name":"shaik"}
b.setdefault("name","ismail")
'ismail'
b
{'last name': 'shaik', 'name': 'ismail'}

#pop()
a={"Name":"ismail","passing year":2026,"month":"may"}
a.pop(name)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.pop(name)
NameError: name 'name' is not defined
a.pop(Name)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.pop(Name)
NameError: name 'Name' is not defined
a.pop("Name")
'ismail'
a
{'passing year': 2026, 'month': 'may'}

#popitem()
a={"Name":"ismail","gmail":"ismail@gmail.com"}
a.popitem()
('gmail', 'ismail@gmail.com')
a
{'Name': 'ismail'}
a.popitem()
('Name', 'ismail')
a
{}

#copy()
a={"city":"vja","state":"ap"}
a.copy()
{'city': 'vja', 'state': 'ap'}

#get()
a.get("city")
'vja'

a
{'city': 'vja', 'state': 'ap'}

#clear()
a.clear()
a
{}
b={}
b.update({"NAME":"KHAJAVALI"})
b
{'NAME': 'KHAJAVALI'}

