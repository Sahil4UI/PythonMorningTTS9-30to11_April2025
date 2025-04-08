Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #String Methods
>>> x = "hello welcome to PYTHON"
>>> x.upper()
'HELLO WELCOME TO PYTHON'
>>> x.lower()
'hello welcome to python'
>>> x.title()
'Hello Welcome To Python'
>>> x.capitalize()
'Hello welcome to python'
>>> len(x)
23
>>> #Indexing
>>> x[0]
'h'
>>> x[3]
'l'
x[-1]
'N'

x
'hello welcome to PYTHON'
#slicing
x[0:5]
'hello'
x[0:5:1]
'hello'
x[0:5:2]
'hlo'
x[:5]
'hello'
x[0:]
'hello welcome to PYTHON'
x[:]
'hello welcome to PYTHON'
x[::1]
'hello welcome to PYTHON'
x[::-1]
'NOHTYP ot emoclew olleh'
x
'hello welcome to PYTHON'
x.find("P")
17
x[17:]
'PYTHON'
x
'hello welcome to PYTHON'
x.find("o")#first occurence
4
x.rfind("o")#last occurence
15
x.find("o",0)
4
\
x.find("0",5)
-1
#here -1 means value not found
x.find("o",5)
10
x = '''hello lets learn python
python is a general purpose programming'''
x.find("purpose")
44
x
'hello lets learn python\npython is a general purpose programming'
x.find("h")
0
x.index("h")
0
x.find("X")
-1
x.index("X")
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    x.index("X")
ValueError: substring not found
x
'hello lets learn python\npython is a general purpose programming'
x.split()
['hello', 'lets', 'learn', 'python', 'python', 'is', 'a', 'general', 'purpose', 'programming']
x[-2]
'n'
x.split()[-2]
'purpose'
x = ['hello', 'lets', 'learn', 'python', 'python', 'is', 'a', 'general', 'purpose', 'programming']
type(x)
<class 'list'>
" ".join(x)
'hello lets learn python python is a general purpose programming'
"#".join(x)
'hello#lets#learn#python#python#is#a#general#purpose#programming'
