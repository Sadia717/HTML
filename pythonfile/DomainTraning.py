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
import numpy as np 
linspace_fun=np.linspace(1,8,5,endpoint=False)
print(linspace_fun)
longspace_fun=np.longspace(1,8,5,endpoint=False)
print(longspace_fun)
Zeros_fun=np.zeros([2,5])
print(Zeros_fun)
ones_fun=np.ones([3,5])
print(ones_fun)
