Python 3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Enter "help" below or click "Help" above for more information.
#Data Collection - List
x = [1,2,3,4,5,6]
y = [3,3.43,True,"hey"]
type(x)
<class 'list'>
x
[1, 2, 3, 4, 5, 6]
#indexing
x[0]
1
x[-1]
6
#slicing
x[0:5]
[1, 2, 3, 4, 5]
x[::-1]
[6, 5, 4, 3, 2, 1]
#nested list
x = [1,2,3,[4,5,6,[7,8,9,10]]]
x[3][3][-1]
10
x[-1][3][-1]
10
x = [1,2,3,4,5]
x.append(90)#add value at the end
x
[1, 2, 3, 4, 5, 90]
x.append(80)
x
[1, 2, 3, 4, 5, 90, 80]
x.insert(0,100)
x
[100, 1, 2, 3, 4, 5, 90, 80]
x.insert(3,-10)
x
[100, 1, 2, -10, 3, 4, 5, 90, 80]
#update
x[0] = 5
x
[5, 1, 2, -10, 3, 4, 5, 90, 80]
x
[5, 1, 2, -10, 3, 4, 5, 90, 80]
x.pop()# it will remove the last value
80
x
[5, 1, 2, -10, 3, 4, 5, 90]
x.pop(0)#remove by index
5
x
[1, 2, -10, 3, 4, 5, 90]
x.remove(90)
x
[1, 2, -10, 3, 4, 5]
#remove by value
del x[0]
x
[2, -10, 3, 4, 5]
x.clear()
x
[]
#list comprehension
x = [i for i in range(1,11)]
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = [1,2,3,4]
y = [5,6,7,8]
x+y
[1, 2, 3, 4, 5, 6, 7, 8]
x
[1, 2, 3, 4]
x*3
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
x.append(y)
x
[1, 2, 3, 4, [5, 6, 7, 8]]
x
[1, 2, 3, 4, [5, 6, 7, 8]]
del x
x
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    x
NameError: name 'x' is not defined
x = [1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(x)):
    print(x[i])

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
for item in x:
    print(item)
2
SyntaxError: invalid syntax
for item in x:
    print(item)

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
