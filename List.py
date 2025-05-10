Python 3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Enter "help" below or click "Help" above for more information.

>>> # list - copy
>>> x = [1,2,3,4,5]
>>> type(x)
<class 'list'>

>>> y = x
>>> # x ka address y me gaya

>>> del x[0]
>>> x
[2, 3, 4, 5]

>>> y
[2, 3, 4, 5]

>>> y = x.copy()
>>> x
[2, 3, 4, 5]

>>> y
[2, 3, 4, 5]

>>> del x[0]
>>> x
[3, 4, 5]

>>> y
[2, 3, 4, 5]

>>> # Tuple - tuple is immutable (which cannot be changed)
>>> x = (1,2,3,4,5)

>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion

>>> x
(1, 2, 3, 4, 5)

>>> len(x)
5

>>> x.count(4)
1

>>> x.count(0)
0

>>> x.index(5)
4

>>> # list comprehension
>>> x = [i for i in range(1,11)]
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> y = (i for i in range(1,11))
>>> y
<generator object <genexpr> at 0x101529f00>

>>> for i in y:
...     print(i)
...
1
2
3
4
5
6
7
8
9
10
