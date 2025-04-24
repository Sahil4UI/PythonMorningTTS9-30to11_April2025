Python 3.8.10 (v3.8.10:3d8993a744, May  3 2021, 09:09:08) 
[Clang 12.0.5 (clang-1205.0.22.9)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #loop
>>> #DRY - Dont Repeat Yourself
>>> print(1)
1
>>> print(2)
2
>>> print(3)
3
>>> #instead of repeating the code,use loop
>>> for i in range(1,11):
	print(i)

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
>>> for i in range(1,11,1):
	print(i)

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
>>> for i in range(1,11,2):
	print(i)

1
3
5
7
9
>>> #jab range min to max pe jaye to ending n-1,we adjust it by +1
>>> #jab range max to min pe jaye to ending n+1,we adjust it by -1
>>> for i in range(10,0,-1):
	print(i)

10
9
8
7
6
5
4
3
2
1
>>> for i in range(10,0):
	print(i)

>>> for i in range(5):#it will starts from 0
	print(i)

0
1
2
3
4
>>> for i in reversed(range(1,11)):
	print(i)

10
9
8
7
6
5
4
3
2
1
>>> #break statement
>>> #break statement is used to trannsfer the control flow of
>>> #program outside the loop
>>> #in simple words it is used to exit the loop
>>> for i in range(1,1100000000000000000000000):
	if i==5:
		break
	print(i)

1
2
3
4
>>> 
========= RESTART: /Users/sahilkumar/Desktop/chatbot/x.py =========
Enter Msg : hey
hey...
>>> 