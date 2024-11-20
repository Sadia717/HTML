#To take the input from user and check it is one digit or two digit
'''n=int(input('Enter Number'))
if (n>=-9 &n<=9):
    print('one digit number')
else:
    print('Two digit number')'''
#To take input from user month number and print no days
'''n=int(input("Enter Number"))
if(n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12):
    print("No of days in month{n} is 31 days")
elif(n==2):
    print("No of days in month{n} is 28 days")
else:
    print("No of days in month{n} is 30 days")
#For the invalid Number
n=int(input("Enter Number"))
if(n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12):
    print("No of days in month{n} is 31 days")
elif(n==2):
    print("No of days in month{n} is 28 days")
elif(n==4 or n==6 or n==9 or n==11):
    print("No of days in month{n} is 30 days")
else:
    print("Invalid Month Number")'''

#Take  4 subjects marks and calculate the average and 
#85+ Grade A
#60+ Grade B
#50+ Grade C
#35+ Grade D
#Less than 35 "Fail"
#sol1
'''n=int(input("Enter Maths Marks"))
n=int(input("Enter Physics Marks"))
n=int(input("Enter chemistry Marks"))
n=int(input("Enter Biology Marks"))
if(n>=85):
    print("Grade:A")
elif(n>=60):
    print("Grade:B")
elif(n>=50):
    print("Grade:C")
elif(n>=35):
    print("Grade:D")
else:
    print("Fail")
#sol2
n1=int(input("Enter sub1"))
n2=int(input("Enter sub2"))
n3=int(input("Enter sub3"))
n4=int(input("Enter sub4"))
avg=((n1+n2+n3+n4)/4)
if(n1<35 or n2<35 or n3<35 or n4<35):
    print("Fail")
else:
    if(avg>=85):
        print("Pass: A Grade")
    elif(avg>=60):
        print("Pass: B Grade")
    elif(avg>=50):
        print("Pass: c Grade")
    elif(avg>=35):
        print("Pass")'''

#Take input from user of N and print the number upto N from 1 using while loop
'''n=int(input())
i=0'''
'''while(i<=n):
    print(i)
    i+=1

for i in range(1,n+1):
    print(i,end=" ")'''

'''while(n>=1)
    print(n,end="")
    n-=1

for i in range(n,0,-1):
    print(i,end="")'''

#Take a user from input and print tables using for loop
'''n=int(input())
for i in range(1,11):
    print(f"{n}x{i}=",n*1)'''
#Arrays
#one-D Array and Mutidimensional Array
#Take the float values from user of size 10 and print the array
'''import array as arr
a=[]
a=arr.array()
print(type(a))
for i in a:
    print(i)

'''
'''import array as arr
n=int(input("Enter the size"))
a=arr.array('f',[])
for i in range(n):
    a.append(float(input("Enter the element:")))
print(a)
for i in range(n):
    print(a[i])'''
#it adds the value and it doesn't replace the value:
'''import array as arr
n=int(input("Enter the size"))
a=arr.array('f',[])
for i in range(n):
    a.append(float(input("Enter the element:")))
print(a)
for i in range(n):
    print(a[i])
'''
#append,insert,pop,pop(n),remove,index,reverse,extend,slicing[start:stop:step]
#by using the above methods
'''import array as arr
a=arr.array('i',[101,102,103,104,105,1,0,2,5,8,5,85,88,1,0,2,5,8,5,85,88])
print(len(a))
#remove(88)
a.remove(88)
print(a)
a.pop()
print("Ater pop length",len(a))
sliced_array=a[15:20]
print(a)
a.pop(0)
print("after pop(0) Length ",len(a))
a.extend(sliced_array)
print("After sliced array extend Length",len(a))
a.reverse()
print("Final Length",len(a))
print("index of 0",a.index(0))'''

#ways to create Arrays using Numpy:
#array()Function
#linspace()Function
#longspace()Function
#arange()Function
#zeros()Function
#ones()Function
#syntax : numpy.array(object,dtype=None,copy=True,order='k',sub)
#declare a list with a different datatype and display a list as array
'''import array as arr
import numpy as np
a=[1,2,35,8,9,5,6,9,3.6,96.5,9,5]
arr_1=np.array([a],int)
print(arr_1)'''

#linspace()Function syntax:
#numpy.linspace(start,stop,num=50,endpoint=True,restep=False,dtype=None,axis=0)
#start-it represents starting element.
#stop- it represents endpoint element.
#num-it represents number of parts the element should be divided.default is 50,it must be non-negative.
#endpoint-if True,stops is the last element.if false,stop is not included.
'''import numpy as np 
linspace_fun=np.linspace(1,8,5,endpoint=False)
print(linspace_fun)
longspace_fun=np.longspace(1,8,5,endpoint=False)
print(longspace_fun)
Zeros_fun=np.zeros([2,5])
print(Zeros_fun)
ones_fun=np.ones([3,5])
print(ones_fun)
'''
#Lists:
'''
a=[]
n=int(input("Enter Number of Elemens:"))
for i in range(n):
    a.append(int(input("Enter Element")))
print("List")
for element in a:
    print(element)'''

#Write a program to find sum of all digits in a number n=1+2+3+4=10
'''n = 1234
sum_of_digits = 0
while n > 0:
    sum_of_digits += n % 10
    n //= 10
print("Sum of digits:", sum_of_digits)'''

'''def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total
'''
'''n = 1234
print("Sum of all digits:", sum_of_digits(n))'''

'''n = 1234
total = 0

while n > 0:
    total += n % 10
    n = n // 10

print("Sum of all digits:", total)'''
'''n = 123
product = 1

while n > 0:
    product *= n % 10
    n = n // 10

print("Product of all digits:", product)
'''
#write the program to find out whether the given number is neon or not 
#a number is said to be neon if the sum of all the digits od square of number is equal to the given number
'''n=int(input())
sq=n*n
sum=0
while sq:
    d=sq%10
    sum+=d
    sq=sq//10
if sum==n:
    print("Neon")
else:
    print("Not neon") '''

#write a python program to find out the given number is spy number or not
#a number is said to be spy if sum of all digits number is equal to the product of all the digits ex=123
'''n=int(input())
sum,prod=0,1
while n:
    d=n%10
    sum+=d
    prod*=d
    n=n//10
if sum==prod:
    print("spy")
else:
    print("not spy")'''

#wite a python prgm to count number of digits in a number n=1234
'''n=int(input())
count=0
while n:
    count+=1
    n=n//10
print("count")'''
#write a python program to reverse of a number
'''n=int(input())
reverse=0
while n:
    d= n % 10
    reverse=reverse*10+d
    n=n//10
print("Reverse number:", reverse)'''

#write a python prgm to find factorial of given number
#to find factorial we have to perform product of all the digits from given number is 5 to till 1
'''n=int(input())
fact=1
for i in range(1,n+1): #for i in range(1,n+1)or (n,0,-1):
    fact=fact*i
print("fact")'''

#wite a python program to find out a strong number
#we have to find out sum of factorials of all the digits of a number is equal to the given number ex=145
'''import math

n=int(input())
sum_of_factorials = 0
temp=n
while temp>0:
    digit=temp % 10
    sum_of_factorials+=math.factorial(digit)
    temp=temp//10
if sum_of_factorials == n:
    print(n, "is a strong number.")
else:
    print(n, "is not a strong number.")'''

'''n=int(input("Enter the number:"))
m=n
fact=1
sum=0
while n:
    d=n%10
    for i in range(1,d+1,1):
        fact=fact*i
    sum+=fact
    fact=1
    n=n//10
if sum==m:
    print("strong")
else:

    print("not strong")'''

#wrire a python program to find the given number is armstrong number or not
# to find armstrong number we have to find power of all the digits of a number=the given number ex=153
'''n=int(input())
a=n
m=str(n)
digit=len(m)
sum=0
while n:
    d=n%10
    cube=d**digit
    sum+=cube
    n=n//10
if sum==a:
    print("armstrong")
else:
    print("not armstrong")'''

#write a python prgm to find out prime or not 
#a number must have only tow numbers that is 1 and number itself 
'''n=int(input())
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")'''

#write a python program to find whether the given number is a magic number or not
#to find magic number we have to find sum of all the digits recursively till the sum become 1 then it is
# a magic number else not a magic number ex=55, ex=73
'''n=int(input("Enter the number:"))
while n>9:
    sum=0
    while n>0:
        sum+=n%10
        n= n//10
    n=sum
if n==1:
    print("It is a magic number")
else:
    print("It is not a magic number")'''
'''while n>9:
    sum=0
    temp=n
    while n:
        d=n%10
        sum+=d
        n=n//10
    n=sum
if n==1:
    print("magic")
else:
    print("not magic")'''

#write a python prgm to swap the variables a=10,b=20
#3 approaches are: 1,temp 2,pthon logic 3,xor
#a variable is a name give to location of memory stack memory,heap memory
#2
'''a=10
b=20
a,b=b,a
print(a)
print(b)'''
#1
'''a=10
b=20
cse=a
a=b
b=cse
print(a)
print(b)'''
#3
'''a=10
b=20
a=a^b
b=a^b
a=a^b
print(a)
print(b)'''

#write a python program to find fibonacii sequnce for the range 
#the sum of previous two numbers is equal to next number is called fibonacii numbers ex: n=5
n=int(input())












