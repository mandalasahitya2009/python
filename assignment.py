#getting the input from user
name=input("enter your name")
age=int(input("enter your age"))
height=float(input("enter your height"))
#printing the values
print(name)
print(age)
print(height)

#program 2:personalized greeting
name=input("enter your name")
print(F"Hello,{name}!")

#program3:add two numbers read as strings
#taken the input as a string
a=input()
b=input()
#converting the string into interger
a=int(a)
b=int(b)
#find the sum
total=a+b
#print the result
print(total)

#float:numbers wiht decimal value 
#int:whole number without any decimal or fractional value
# reading a float value from the user
n=float(input())
#print the float the value
print(n)
#convert the float into interger:decimal point values will be removed
new=int(n)
#print the result
print(new)

#program5:sum using arithmetic operator
#reading 2 intergers from the user
a=int(input())
b=int(input())
#finding the sum and printing the result
print(a+b)

#reading input from the user
length=float(input())
breadth=float(input())
#calculating the area of a rectangle
area=length*breadth
#print the result
print(area)

#user inputs
a=int(input())
b=int(input())
#find the quoteint
q=a/b
#find the remainder
r=a%b
#print the result
print(q)
print(r)

#reading user the input
base=int(input())
exponent=int(input())
#calculate the power of and print the result
print(base**exponent)

#taking 3 interger numbers from the user
n1=int(input())
n2=int(input())
n3=int(input())
#find the total
total=n1+n2+n3
#find the average
avg=total/3#division operator/-->always gives the result as a float
#print the average
print(avg)


#read2 interger numbers from  user
a=int(input())
b= int (input())
#check wether the 1st number  is greater than the 2nd number
print(a>b)


#check whether bothe the numbers are same or not
#if the numbers are same -true
#if the numbers are different-flase
#reading the input from the user
n1=int(input())
n2=int(input())
print(n1==n2)

#if the number is greater than 0
#logical and -->if all the combinig conditions are true,result is true
# reading the input from the user
n1=int(input())
n2=int(input())
print(n1>0 and n2>0)


#logical note -->reverse the result
#true-->false
#false--> true
#reading the input from the user
num=int(input())
print(not(num>0))


#read a number from the user
a=int(input())#20
a=a+5#a=20+5-->25
a=a*2#a=25*2
a=a-3#a=50-3-->47

#formula:f=(c*9/5)+32
#read the temperature in celsius
c=float(input())
#convert the clesius to fahrenit
f=(c*9/5)+32
print(f)

#check divsibility by 3 and 5
n=int(input())
print(n%3==0 and n%5==0)

 
