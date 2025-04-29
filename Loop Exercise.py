#find the sum of first 10 natural numbers
'''
result = 0
for i in range(1,6):
    result+=i
print(result)
'''
#write a program to find the factorial of number
'''
result = 1
x = int(input("Enter a no : "))
for i in range(1,x+1):
    result*=i
print(result)
'''
#write a program to check whether a given number is prime or not
'''
x = int(input("Enter no:"))
for i in range(2,x):
    if x%i==0:
        print("not prime")
        break
else:
    print("prime")
'''
#write a program to find the sum of digits of number
# 125 =>1+2+5=8
x = int(input("Enter no :"))
res = 0
for i in range(len(str(x))):
    rem  = x%10
    res += rem
    x = x//10
print(res)


#find the reverse of number =>123=321



















