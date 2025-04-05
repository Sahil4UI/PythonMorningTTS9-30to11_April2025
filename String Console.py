Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#String - String is Python's Data Type
#String is immutable(which cannot be changed)
x = 'hello how are you?"
SyntaxError: unterminated string literal (detected at line 1)
x = 'hello how are you?'
type(x)
<class 'str'>
x = "hello how are you?"
type(x)
<class 'str'>
x = "hello
SyntaxError: unterminated string literal (detected at line 1)
x = '''hello
welcome to python'''
x
'hello\nwelcome to python'
print(x)
hello
welcome to python
#''' ''' -  multiline string
x = "Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document.
To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want from the different galleries.
"
SyntaxError: unterminated string literal (detected at line 1)
x = '''
Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document.
To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want from the different galleries.'''
print(x)

Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document.
To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want from the different galleries.
x = "Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document.
To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want from the different galleries.
"
SyntaxError: unterminated string literal (detected at line 1)
x = """Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document.
To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want from the different galleries.
"""
print(x)
Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document.
To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want from the different galleries.

x = "hello "python""
SyntaxError: invalid syntax
x = 'hello "Python"'
print(x)
hello "Python"
x = "hello 'Python'"
print(x)
hello 'Python'
x = "hello \"python""
SyntaxError: unterminated string literal (detected at line 1)
x = "hello \"python\""
print(x)
>>> hello "python"
>>> #\-escape sequence
>>> x = "hello welcome TO PYTHON"
x.lower()
>>> 'hello welcome to python'
x.upper()
>>> 'HELLO WELCOME TO PYTHON'
x.capitalize()
>>> 'Hello welcome to python'
x.title()
>>> 'Hello Welcome To Python'
x
>>> 'hello welcome TO PYTHON'
x.swapcase()
>>> 'HELLO WELCOME to python'
x
>>> 'hello welcome TO PYTHON'
len(x)
