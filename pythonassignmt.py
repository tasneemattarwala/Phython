

#wap to take input from user and check whether it is even or greater than 50
'''x=int(input("enter the number"))
if(x%2==0 or x>50):
 print("THE NUMBER IS EVEN")
elif(x>50):
 print("THE NUMBER IS GREATER THAN 50")
else:
 print("ENTER VALID NUMBER")
''' 

#wap to take float as a number and create calculator
'''
a=float(input("ENTER FIRST NUMBER"))
b=float(input("ENTER SECOND NUMBER"))
c=a+b
d=a/b
f=a-b
print("ANSWER=",c,b,f)
'''

#wap to take 2 strings from user and perform concatenation as follows
'''eg: x='Hello'
    y='World'
 o/p : Hello World

'''
'''
x=("HELLO")
y=("WORLD")
c=x+" "+y
print(c)
'''

#wap to take 2 numbers from user and check whether its a divisible of 17 or not
'''
a=int(input("Enter the first no"))
b=int(input("Enter the second no"))
if(a%17==0 and b%17==0):
 print("THE Numbers IS DIVISIBLE BY 17")
else:
 print("THE NUMBERS ARE NOT DIVIBLE BY 17")     
#else:
#elif(b%17==0):
#print("THE NUMBER IS DIVISIBLE BY 17 ")
'''

#wap to take 2 input from a user and calculate exponential
'''a=int(input("Enter the first no"))
b=int(input("Enter the second no"))
d=a**b
print(d)
'''
#wap to take 2 input from user and perform division which gives answer in integer form

'''
a=int(input("Enter the first no"))
b=int(input("Enter the second no"))
d=a/b
print(d)
'''

#WAP to take a number from user and print whether that number is even or odd
'''a=int(input("enter a number"))
if(a%2==0):
 print("The number is even")
else:
 print("The number is odd")
'''

#WAP to take percentage from user and print 1st class if percentage is above 60 print 2nd class if % is in between 40 to 60,print fail if % is less than 40.
'''a=int(input("enter a percentage"))
if(a>60):
 print("FIRST CLASS")
elif(a>=40 and a<=60):
 print("SECOND CLASS")
else:
 print("FAIL")
'''

#WAP to take MRP from user of a product and display the final price after calculating with different schemes.
'''scheme 1: 40% of on MRP
  s 2: 60% of on MRP 
 s 3: 80% of on MRP
for all other products there is no scheme applicable

a=int(input("Enter a  price"))
'''

'''
MRP=float(input('Enter MRP'))
Scheme=int(input('Enter  the scheme to apply'))
if(Scheme==1):
 print('Final price:',MRP*60/100)
elif(Scheme==2):
 print('Final price:',MRP*40/100)
elif(Scheme==3):
 print('Final price:',MRP*20/100)    
else:
 print('Final price:',MRP)   


'''
#WAP to swap 2 numbers
'''a=30
b=40
c=(b,a)
print("nos are",c)'''

'''
a=int(input("Enter the first no"))
b=int(input("Enter the second no"))
(a,b)=(b,a)
print("a=",a,"b=",b)
'''

'''#WAP to print "Python" 20 times.
a=str("python")
for i in range(1,21):
 print(a)
'''


#WAP to print n natural numbers.
'''
num=int(input("enter the nons"))
i=1
while(i<=num):
 print("n=",i)
 i=i+1
 
'''

'''#WAP to print 10 to 1.
num=int(input("enter the nons"))
i=10
while(i>=1):
 print(" ",i)
 i=i-1
'''





#WAP to find GCD and LCM of 2 numbers.
'''
a=int(input("Enter the first no"))            
b=int(input("Enter the second no"))
temp1=a
temp2=b
while(a!=b):
 if(a>b):
  a=a-b
 else:
  b=b-a
gcd=a
lcm=(temp1*temp2)/gcd
print("gcd is",gcd,"lcm is",lcm)
'''


'''#WAP to count no of digits inthe given number

a=int(input("Enter the first no"))
count=0
no=a.count()
print(no)'''


#wap to print armstrong
'''
a=int(input("Enter the first no"))
sum1=0
temp=a
while(temp>0):
 dig=temp%10
 sum1=sum1+dig**3
 temp//=10
if(a==sum1):
 print("ARMSTRONG NO")
else:
 print("not armstrong")

'''


#WAP to generate fibonacci series
'''n=int(input("Enter the first no"))
n1,n2=0,1
print(n1,n2)
for i in range (1,n-1):
 temp=n1+n2
 print(temp)
 n1,n2=n2,temp
'''

#WAP to print all odd numbers between 13 to 123
'''
for i in range(13,124,2):
 print(i)
'''

#WAP to print all natural numbers from 100 to 1 using for loop
'''n=int(input("Enter the first no"))
i=100
while(i>0):
 print("n=",i)
 i=i-1

''' 
 
#WAP to check whether given no is prime or not
a=int(input("Enter the first no"))
if(a%2!=0):
 print("is a prime")
else:
 print("not a prime")


#WAP optimal code to check whether the given no is prime or not
'''a=int(input("Enter the first no"))
b=a%2!=0
print("is",b)'''
 
#WAP to print prime numbers between 1 to 100.

'''for i in range (1,101):
 if(i%2!=0):
  print(i)
'''


#WAP to print armstrong number between 1 to 1000.
'''
for i in range(1,1001):
 sum1=0
 temp=i
while(i>0):

 sum1=sum1+(i%10)**3
 i//=10
if(sum1==temp):
 print(i)
'''

#program 1
'''
excluded_list=["is","am","are","of","as","on","a"]
a=input("enter a sentence")
temp=a.lower().split()
list1=[]
for each in excluded_list :
 if(each in temp):
  temp.remove(each)
a=("  ".join(temp))
print("final sentence=",a)
'''

#program2
'''
excluded_list=["is","am","are","of","as","on","a"]
a=input("enter a sentence")
temp=a.lower().split()
list1=[]
for each in excluded_list :
 if(each not in temp):
  list1.append(temp)
a=("  ".join(list1))
print("final sentence=",a)

'''




#program3

'''
a=input("enter the sentence")
b=input("enter a word")
st=a.split()
c=a.lower()
d=b.lower()
list1=[]
if (d in c):
 print("this is present"," ",c.count(d))
else:
    ("invalid")
  '''   
#WAP to take input from a user for name,mobile number, address with validation.
'''
name=input('Enter your name')
if(name.isdigit() or name.isalnum()):
 print('Enter Alphabets')
'''

#WAP to take input from user and give square root.
'''
import math

a=int(input("enter the no"))
ans=math.sqrt(a)   
print("square root is",ans) 
'''


#WAP to take n inputs and print the largest,smallest,total,average number .
'''n=int(input("enter the nos"))
for x in range(1,n+1):
 print( "avg =",x+n//2,"largest=",x>n,"smallest=",x<n,"total=",x+n) 
'''
#Factorial of a number.
'''a=int(input("enter the no"))
fact=1
for i in range(1,a+1):
 fact=fact*i
print("factorial is",fact)
'''
#pattern 
'''
123
123
123
123
'''
'''
a=int(input("enter the no of rows"))
for i in range(1,5):
 for j in range(1,4):
  print(j,end=" ")
 print()
     '''
