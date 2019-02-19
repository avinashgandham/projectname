import sys
print " number of argument is " , len (sys.argv), 'arguments.'
print " Argument list " ,str (sys.argv)

import sys
print " number of argument is " , len (sys.argv), 'arguments.'
print " Argument list " ,str (sys.argv[0])

raw_input("Enter a number :")
Enter a number : 10

input("Enter a number :")
Enter a number :10

a = raw_input("Enter Something :")
Enter Something : 10
b = input("Enter Something : ")
Enter Something : 10

type(a)
<type 'str'>
type(b)
<type 'int'>
# raw_input -> returns a string
# input -> Returns a number

a = raw_input ("Enter a String : ")
Enter a string: Hello
b = input("Enter a string : ")
Enter a string : hello

b = input ('Enter a string : ')
Enter a string ; 'hello'
type(b)

# input -. returns a number as well as a string based on the data

b = input ("enter a list :")
enter a list :[1,2,3]

type(b)
<type 'list'>
 
for i in 'python':
	if i=='o':
		break
	
for i in 'python':
	if i=='o':
		break
	else:
		print i
		
		
for j in range(2):
	for i in 'python':
		if i == 'o':
			break #break out of FOR Loop
		print'=========='
		print j
		print'=========='
		
		
for i in 'python':
	if i == 'o':
	print i
	
def mathcalc():
	pass #placeholder
	
for i in 'python':
	if i == 'o':
		continue 
	print i
	
def mathcalc():
	pass #placeholder
	
	
for i in 'python':
	if i=='o':
		break
	else:
		print i
else:
	print "Where am I"
	
range(10)
range(100)
range(10, 20)
range(20, 25)
range(10, 20, 2)

#range(start, stop, step)
#range(stop) -> step =1
#range(stop) -> start=0, step=1


for i in xrange(10,20,2)
	print i
	

t1 = ()
type

<type 'type'>
type(t1)
<type 'tuple'>

l1 = []
type(l1)
<type 'list'>
d1 = {}
type(d1)
<type 'dict'>

t1 = ()
type(t1)
<type 'tuple'>

l1 = ['a', 'b']
type(l1)
<type 'list'>

l2 = [1,2]
l1

l2

l3= l1+l2
l3

l4=[('apple' ,'ball' , 'cat'), ('dog' , 'lion', 'tiger')]
l4

type(l4)

l1

l2

l3

l1[0]

l4

l4[0]

type(l4[0])

t1 = l4[0]

t1[0]

l4

l4[0]

l4[0][0]

l1

l2

l3

l3[3]

l3[-1]

l3[1:3]

l3

len(l4)

len(l3)

dir(l3)

l3.sort()
l3

l3.reverse()
l3

l3.rempve()

dir(l3.remove())

l3.remove_doc_

l3.append('b')
l3

l3.remove('b')
l3

l3.remove('b')
l3

l3.remove('d')

l3

l3.pop()

l3

l3.pop()

l3

l3.pop()

dir(l3)

l3.insert_doc_

l3

l3.insert(2,'z')

l3.insert(-1,'y')

l3

l3.index_doc_

l3.index('b')

l3.index('y')

l3.extend_doc_

l3

l2

l1

l4
l3.extend(l4)

l3.count_doc_

l3

l3.count('a')

l3.extend(l4)
l3

l3

l2

l3.append(l2)
l3

#append vs extend
#Extend => it adds onto the same list as element
#Append => it adds whatever is there in the object with the datatype

t1('appple','ball','cat')
l9=list(t1)
l9

l1=[a,b]
l1*2

l1*4

t1=('apple','ball','cat')
t1

type(t1)
<type 'tuple'>


l3=['a','b',1,2,3]
l3

dir(l3)
dir(l3)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 
'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

>> dir(t1)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
 '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', 
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

 t1.pop()
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    t1.pop()
AttributeError: 'tuple' object has no attribute 'pop'
>>> t1.remove('apple')
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    t1.remove('apple')
AttributeError: 'tuple' object has no attribute 'remove'
>>


>>> t3=()
>>> t2=tuple(l3)
>>> t2
('a', 'b', 1, 2, 3)
>>> type(t2)
<class 'tuple'>
>>> type(l3)
<class 'list'>
>>> t1=(1)
>>> t2=(2)
>>> cmp(1,2)
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    cmp(1,2)
NameError: name 'cmp' is not defined
>>> (1>2)-(1<2)
-1
>>> (2>1)-(2<1)
1
>>> (1>1)-(1<1)
0
>>> t1=('apple')
>>> t2=('ball')
>>> (t1>t2)-(t1<t2)
-1
>>> t1 =('apple','ball')
>>> t2=('apple','ball','cat')
>>> (t1>t2)-(t1<t2)
-1
>>> (t2>t1)-(t2<t1)
1
>>> max(t1)
'ball'
>>> min(t1)
'apple'
>>> enumerate(t2)
<enumerate object at 0x000001FE26D97EE8>
>>> t2
('apple', 'ball', 'cat')
>>> tuple(enumerate(t2))
((0, 'apple'), (1, 'ball'), (2, 'cat'))
>>> t2[1]
'ball'
>>> t2[0]
'apple'
>>> t2[2]
'cat'
>>> tuple(enumerate(t2))
((0, 'apple'), (1, 'ball'), (2, 'cat'))
>>> list(enumerate(t2))
[(0, 'apple'), (1, 'ball'), (2, 'cat')]
>>> d={}
>>> type(d)
<class 'dict'>
>>> a={'a':'apple','b':'ball','c':'cat'}
>>> d['a']
Traceback (most recent call last):
  File "<pyshell#251>", line 1, in <module>
    d['a']
KeyError: 'a'
>>> a['a']
'apple'
>>> a[0]
Traceback (most recent call last):
  File "<pyshell#253>", line 1, in <module>
    a[0]
KeyError: 0
>>> a['b']
'ball'
>>> a['c']
'cat'
>>> a
{'a': 'apple', 'b': 'ball', 'c': 'cat'}
>>> d={'a':'apple','b':'ball','c':'cat'}
>>> d
{'a': 'apple', 'b': 'ball', 'c': 'cat'}
>>>  d['a']
SyntaxError: unexpected indent
>>> d['a']
'apple'
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#261>", line 1, in <module>
    d[0]
KeyError: 0
>>> d['b']
'ball'
>>> d['c']
'cat'
>>> d
{'a': 'apple', 'b': 'ball', 'c': 'cat'}
>>> dir(d)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> d
{'a': 'apple', 'b': 'ball', 'c': 'cat'}
>>> d.items()
dict_items([('a', 'apple'), ('b', 'ball'), ('c', 'cat')])
>>> l=d.items()
>>> type(l)
<class 'dict_items'>
>>> d.iteritems()
Traceback (most recent call last):
  File "<pyshell#270>", line 1, in <module>
    d.iteritems()
AttributeError: 'dict' object has no attribute 'iteritems'
>>> tuple(d.items())
(('a', 'apple'), ('b', 'ball'), ('c', 'cat'))
>>> d.keys()
dict_keys(['a', 'b', 'c'])
>>> d.values()
dict_values(['apple', 'ball', 'cat'])
>>> d.pop('c')
'cat'
>>> d
{'a': 'apple', 'b': 'ball'}
>>> dir(d)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> d
{'a': 'apple', 'b': 'ball'}
>>> d.update({'c':'cat'})
>>> d
{'a': 'apple', 'b': 'ball', 'c': 'cat'}
>>> d.popitem()
('c', 'cat')
>>> d
{'a': 'apple', 'b': 'ball'}
>>> d.viewitems.__doc__
Traceback (most recent call last):
  File "<pyshell#282>", line 1, in <module>
    d.viewitems.__doc__
AttributeError: 'dict' object has no attribute 'viewitems'
>>> d.__doc__
"dict() -> new empty dictionary\ndict(mapping) -> new dictionary initialized from a mapping object's\n    (key, value) pairs\ndict(iterable) -> new dictionary initialized as if via:\n    d = {}\n    for k, v in iterable:\n        d[k] = v\ndict(**kwargs) -> new dictionary initialized with the name=value pairs\n    in the keyword argument list.  For example:  dict(one=1, two=2)"
>>> d.get.__doc__
'D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.'
>>> d.get('b')
'ball'
>>> d['b']
'ball'
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=['apple','ball']
>>> enumerate(a)
<enumerate object at 0x0000026599470090>
>>> tuple(enumerate(a))
((0, 'apple'), (1, 'ball'))
>>> a='apple'
>>> print'{0}.format('apple','ball')
SyntaxError: invalid syntax
>>> print'{0}.{1}'.format('apple','ball')
SyntaxError: invalid syntax
>>> print('{0}.{1}'.format('apple','ball'))
apple.ball
>>> print('{0}::::{1}'.format('apple','ball'))
apple::::ball
>>> print('{0}'.format('apple','ball'))
apple
>>> q
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    q
NameError: name 'q' is not defined
>>> q=10
>>> q
10
>>> l1=[1,2,3]
>>> l1[4]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    l1[4]
IndexError: list index out of range
>>> d={'a':'apple'}
>>> d['a']
'apple'
>>> d['b']
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d['b']
KeyError: 'b'
>>> f=open('C:/Users/pc/Desktop/Avinash/file1.txt')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    f=open('C:/Users/pc/Desktop/Avinash/file1.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/pc/Desktop/Avinash/file1.txt'
>>> import os
>>> import tood
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    import tood
ModuleNotFoundError: No module named 'tood'








	
	
	
