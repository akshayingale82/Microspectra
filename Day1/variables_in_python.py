>>> 100 = number
SyntaxError: cannot assign to literal
>>> number = 100
>>> number
100
>>> name="Akshay"
>>> name
'Akshay'
>>> print(type(name))
<class 'str'>
>>> num ="420"
>>> print(type(num))
<class 'str'>
>>> num
'420'
>>> num = 500
>>> num
500
>>> x,y,z = 10,20,30
>>> x
10
>>> y
20
>>> z
30
>>> x=y=z="abc"
>>> x
'abc'
>>> id(num)
2441024969744
>>> AkshayIngale
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    AkshayIngale
NameError: name 'AkshayIngale' is not defined
>>> del(num)
>>> num
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    num
NameError: name 'num' is not defined
>>> del(number)
>>> number
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    number
NameError: name 'number' is not defined
>>> 
