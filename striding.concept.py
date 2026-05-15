Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Striding
#[a]-> Indexing
#[a:b]->slicing
#[a:b:c]->Striding
#There will be 2 types
#1]positive striding
a="data science"
a[::]
'data science'
a[::1]
'data science'
a[::2]
'dt cec'
#example 1
x="Machine learning"
x[::3]
'Mheeng'
x[::5]
'Mnag'
x[3:11]
'hine lea'
x[:7]
'Machine'
x[9:]
'earning'
x[::6]
'Men'

#using positioning
a="cloud computing"
a[1:9:2]
'lu o'
a[1:10:3]
'ldo'
a[2:14:4]
'ocu'
a[3:13:5]
'um'
a[3:9:1]
'ud com'
a[5:14:2]
' optn'
a[1:8:]
'loud co'
>>> a[1:8:3]
'ldo'
>>> a[0:14:6]
'cci'
>>> 
>>> #2]Negative striding
>>> a="Python Course"
8
>>> a[-1:-6:-2]
'ero'
>>> a[-2:-12:-4]
'sCh'
>>> a[-3:-13:-2]
'ro ot'
>>> a[-4:-10:-5]
'uo'
>>> a[-1:-9:-3]
'eu '
>>> 
>>> #There are some rules and conditions
>>> #1]In positive stridng Highest value to lowest value not posible
>>> a="Python course"
>>> a[9:4:3]
''
>>> #2]In Negative stridng Highest value to lowest value not posible
>>> a[-6:-4:-2]
''
