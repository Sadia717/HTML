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
n=int(input())
i=0
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
n=int(input())
for i in range(1,11):
    print(f"{n}x{i}=",n*1)
