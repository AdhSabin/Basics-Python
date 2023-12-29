#break
# num = 0
# for i in range(10):
#     num += 1
#     if num == 8:
#         break
#     print("The num has value:", num)
# print("Out of loop")  

# #Continue
# for var in "Lumbini ict campus":
#     if var == "i":
#         continue
#     print(var) 

#print odd numbers

# for i in range(30):
#     if i % 2 != 0:
#         continue
#     print(i) 

# calc = lambda num: "Even number" if num % 2 == 0 else "Odd number" 
# print(calc(29)) 

#Function

# def sum():
#     a=int(input("Enter first number: "))
#     b=int(input("Enter second number: "))
#     c=int(input("Enter third number: "))
#     sum = (a+b+c)
#     print("Sum is : ",sum)

# sum()    

#WAP to define a function name checker to take two input from users and check which one is greater or both are equal.


# for i in range(1, 11):
#     print("7 x", i, "=", 7*i) 

# #Break & Continue

# num = 0
# for i in range(1,11):
#     num += 1

#     if num==8:
#         break

#     print("The number has value: ",num)

# print("Out of the loop")    


# num = 0
# for i in range(1,11):
#     num += 1

#     if num==8:
#         continue

#     print("The number has value: ",num)

# print("Out of the loop")    

#print odd numbers

# for i in range(50):
#     if i % 2 == 0:
#         continue
#     print(i) 

# for i in range(50):
#     if i % 2 != 0:
#         continue
#     print(i)     

#Function
# def sum(d):
#     a = int(input("Enter first number :"))
#     b = int(input("Enter second number :"))
#     c = int(input("Enter third number :"))
#     sum = a+b+c+d
#     print("Sum is :", sum)

# sum(8)    

#WAP to define a function name checker to take two input from users and check which one is greater
#  or both are equal.

# def checker():
#     a = int(input("Enter first number :"))
#     b = int(input("Enter second integer: "))

#     if a>b:
#         print(f"{a} is greater than {b}")
#     elif b>a:
#         print(f"{b} is greater than {a}")
#     else:
#         print(f"{a} and {b} both are equal")

# checker()            

#Class

# class Calculator:
#     def add(self,a,b):
#         print("Sum is:",a+b)

#     def diff(self,a,b):
#         print("Difference is:",a-b)



# obj = Calculator()
# obj.add(7,9)
# obj.diff(9,3)         

#Inheritance

# class Parent:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname

#     def printname(self):
#         print(self.firstname+' and ' + self.lastname)

# obj=Parent("Sabin","Adhikari")
# obj.printname()            
    
# class Student(Parent):
#     pass

# obj1 = Student("Aayush","Ghimire")
# obj1.printname()

#Multiple inheritance
# class Parent1:
#     def method1(self,a,b):
#         print("Sum: ",a+b)

# class Parent2:
#     def method2(self,a,b):
#         print("Difference",a-b)

# class Child(Parent1, Parent2):
#     pass

# child = Child()
# child.method1(6,2) 
# child.method2(9,0) 

#multilevel inheritance 

# class GrandParent:
#     def method1(self):
#         print("GrandParent method1")

# class Parent(GrandParent):
#     def method2(self):
#         print("Parent method2")

# class Child(Parent):
#     pass

# child = Child()
# child.method1() 
# child.method2() 

#hierarchical
# class BaseClass:
#     def method1(self):
#         print("BaseClass method1")

# class DerivedClass1(BaseClass):
#     def method2(self):
#         print("DerivedClass1 method2")

# class DerivedClass2(BaseClass):
#     def method3(self):
#         print("DerivedClass2 method3") 

# derived1 = DerivedClass1()
# derived1.method1() 
# derived1.method2() 

# derived2 = DerivedClass2()
# derived2.method1() 
# derived2.method3()

#Multilevel

# class Vehicle:
#     def wheeler(self):
#         print("Two and four wheeler")

# class Bike(Vehicle):
#     def twowheel(self):
#         print("Bike is two wheeler")

# class Ns(Bike):
#     def nsbike(self):
#         print("NS 200")

# obj = Ns()
# obj.nsbike()        
# obj.twowheel()
# obj.wheeler() 
#Hierarchical

# class Bird:
#     def fly(self):
#         print("Bird can fly")
# class Parrot(Bird):
#     def eat(self):
#         print("Parrot can eat")

# class Eagle(Bird):
#     def walk(self):
#         print("Eagle can walk") 

# class Penguin(Bird):
#     def swim(self):
#         print('Penguin can swim') 

# obj = Penguin()
# obj.swim() 
# obj.fly()

# obj1 = Eagle()
# obj1.walk()
# obj1.fly()        

#Multiple

# class Bike:
#     def twowheel(self):
#         print("Bike is two wheeler")
# class Car:
#     def fourwheel(self):
#         print("Car is four wheeler")
# class Vehicle(Bike,Car):
#     def vehicle(self):
#         print("Bike and car both are vehicle")

# obj = Vehicle()
# obj.vehicle()
# obj.twowheel()
# obj.fourwheel()      

#Pyramid
# n = int(input("Enter the number : "))
# def pypart():
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("* ",end=" ")
#         print("\r")
# pypart() 

# #Method overloading
# def product(a, b):
#     p = a * b
#     print(p)
 
# def product(a, b, c):
#     p = a*b*c
#     print(p)

# #product(5,7)  gives error
# product(4, 5, 5)  

# from multipledispatch import dispatch
# @dispatch(int, int)
# def product(a, b):
#     result = a*b
#     print(result)
 
# @dispatch(int, int, int)
# def product(a,b,c):
#     result = a*b*c
#     print(result)
 
# @dispatch(float, float, float)
# def product(a,b,c):
#     result = a*b*c
#     print(result)
 
# product(2, 3)  
# product(2, 3, 2)  
# product(2.2, 3.4, 2.3)   


#Method overloading

# def product(a,b):
#     print("Product is :",a*b)

# def product(a,b,c):
#     print("Product is :",a*b*c)    

# product(2,3)
# product(4,5,6)    

# from multipledispatch import dispatch
# @dispatch(int, int)
# def product(a, b):
#     result = a*b
#     print(result)
 
# @dispatch(int, int, int)
# def product(a,b,c):
#     result = a+b+c
#     print(result)
 
# @dispatch(float, float, float)
# def product(a,b,c):
#     result = a*b*c
#     print(result)
 
# product(2,3)
# product(4,5,6)
# product(2.3,4.5,6.7) 

#Assignment 1: Write a program that takes a list of words as input
# and returns a new list 
#containing only the words that have more than three letters
# and start with the letter 'a',
#sorted in alphabetical order.

word_list =['ant','apple','basketball','aeroplane','football']
new_list=[]

for word in word_list:
    if len(word)>3 and word[0]=='a':
        new_list.append(word)

new_list.sort()
print(new_list)        

#Assignment : Write a program that takes a list of words as input and returns
#  a new list 
#containing only the words that have less than five letters and do not start
#  with the letter 'b',
#sorted in reverse alphabetical order.



word_list =['ant','apple','basketball','aeroplane','football']
new_list=[]

for word in word_list:
    if len(word)<5 and word[0]!='b':
        new_list.append(word)

new_list.sort()
new_list.reverse()
print(new_list)    

#Assignment 2
# Create a class called "Rectangle" that has two attributes: "length" and "width".
# The class should have a method called "area" and "perimeter" that calculates the
#  area & perimeter of the rectangle.

# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth

#     def area(self):
#         print("Area of rectangle is: ",self.length*self.breadth)

#     def perimeter(self):
#         print("Perimeter of rectangle is: ",2*(self.length+self.breadth))

# obj = Rectangle(5,4)
# obj.area()
# obj.perimeter()                

#Assignment 3

# Create a class called "BankAccount" that has two attributes: "balance" and
#  "account_number". 
# The class should have methods called "deposit" and "withdraw" that allow
#  a user to deposit or withdraw
# money from the account.The balance should be updated accordingly. 


# class BankAccount:
#     def __init__(self, balance, account_number):
#         self.balance = balance
#         self.account_number = account_number
    
#     def deposit(self, amount):
#         print("Before deposit, Total Balance: ",self.balance)
#         self.balance += amount
#         print("After deposit, Total balance: ",self.balance)
    
#     def withdraw(self, amount):
#         print("Before withdraw, Total balance: ",self.balance)
#         self.balance -= amount
#         print("After withdraw, Total balance: ",self.balance) 

# obj = BankAccount(10000,12345)
# obj.deposit(1000)
# obj.withdraw(7000)    




#Random

import random

x = random.randint(1,25)
print(x)
















#Assignment 4: Write a program that takes a list of words as input and returns a new list 
#containing only the words that have less than five letters and do not start with the letter 'b',
#sorted in reverse alphabetical order.