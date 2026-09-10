#comparsion operators
a=10
b=20


print(a == b)
print(a!= b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#age eligibility checker
age = int(input("enter your age:"))

print("eligble:,age>=18")

#idenity operators
a=None
print(a is None)
print(a is not None)

#bitwise operators
a=5
b=3
print(a&b)
print(a|b)
print(a^b)
print(a<<b)
print(a>>b)
a=12
b=6
print(a>>b)
print(a<<b)
a=7 

b=4 
print(a<<b)
a=9
b=3
print(a>>b)
#electricity bill calcualtor
units=int(input("enter electricity units:"))
rate=6
bill=units*rate
print("Electricity Bill:",bill)
#travel  expense calculator
travel=float(input("Travel expense:"))
food=float(input("Food expense:"))
hotel=float(input("Hotel expense:"))

total=travel+food+hotel
print("Total Expense:",total)
#list in python 
#list is an ordered and changeable collection that can store
marks=[80,90,75,85]
print(marks)

#accessing elements in a liSt 
marks=[80,90,75,85]

print(marks[0])
print(marks[1])
print(marks[2])

#change elements in a list 
marks=[80,90,75]

marks[1]=95

print(marks)

#add element to a list
marks=[80,90,75]
marks. append(85)
print(marks)

#remove elements from a list 
marks=[80,90,75]
marks. remove(90)
print(marks)

a=[1,2,3]
b=[4,5,6]

a.extend(b)
print(a)

numbers=[10,20,30]
numbers.clear()
print(numbers)

numbers=[10,20,30,40]
print(numbers.index(20))

numbers=[10,20,20,30,20]
print(numbers.count(20))

numbers=[10,20,30,40,]
numbers.reverse()
print(numbers)

a=[1,2,3]
b=a.copy()
print(b)

numbers=[10,20,30,40,50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

#tuples in python 
#tuples is a collection of multiple value that is ordered and cannot be changed after the creaction
student=("Bhargavi",98,"python")
print(student[0])

#acess value in a tuple
student=("Bhargavi",21,85.5)

print(student[0])
print(student[1])
print(student[2])

#tuples are immutable ,meaning they cannot be changed after the creation
numbers= (10,20,20,30,20)
print(numbers.count(20))

numbers=(10,20,30,40)
print(numbers.index(30))


numbers=(10,20,30,40)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#sets in python
#set is a collection of unique values that is unordered and  mutable
numbers={10,20,30,20,10}

print(numbers)


# why use set?

#suppose students have slected subjects
subjects={"Pyhton","JAVA","Python","SQL","Java"}
print(subjects)


#add values to a set 
subjects={"python","Java"}

subjects.add ("SQL")

print(subjects)

#remove values from a set 
subjects.remove("Java")

print(subjects)
# sets do not allow duplicate values 
numbers={1,2,3,2,3,4}
print(numbers)
