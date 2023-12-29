#Printing

# print("Hello world")  

# #Variable declarartion
# a = 5
# c='s'
# string="Sabin"
# f=5.7

# print(a)
# print(c)
# print(string)
# print(f)

# print(type(a))
# print(type(c))
# print(type(string))
# print(type(f))


#Arithmetic operation

# a=int(input("Enter a number :"))
# b=int(input("Enter second number :"))

# add= a+b
# print("Sum is :",add)

# c=5
# while c<=7:
#     print(f"{c} is lesser or equal to 7")
#     c+=1

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

#Pyramid
# n = int(input("Enter a value: "))
# def pyramid(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("* ",end="")
#         print('\r')
# pyramid(n)  

#Triangle

# n = 5   

# for i in range(1, n+1):
#     for j in range(1, n-i+1):
#         print(" ", end="")
#     for k in range(1, 2*i):
#         print("*", end="") 
#     print()   

# #Simple number guessing game
# import random

# # Generate a random number between 1 and 10
# secret_number = random.randint(1, 10)


# print("Welcome to the Guess the Number game!")

# while True:
#     try:
#         guess = int(input("Enter your guess (between 1 and 10): "))

#         if 1 <= guess <= 10:
#             if guess == secret_number:
#                 print(f"Congratulations! You guessed the correct number, which was {secret_number}.")
#                 break
#             else:
#                 print("Wrong guess. Try again!")
#         else:
#             print("Please enter a number between 1 and 10.")

#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")

# End of the game

#Multilevel

#Area of triangle
# Three sides of the triangle is a, b and c:  
# a = float(input('Enter first side: '))  
# b = float(input('Enter second side: '))  
# c = float(input('Enter third side: '))  
  
# # calculate the semi-perimeter  
# s = (a + b + c) / 2  
  
# # calculate the area  
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 
# print("Area is: ",area) 
# print('The area of the triangle is %0.4f' %area)

# for Loop

# for i in range(10):
#     print(i) 

# var = "Lumbini"
# for x in var:
#     print(x)     



#If else

# age = int(input("Enter your age:"))
# if age>18:
#     print("You are elligible to vote")
# else:
#     print("You are not eligible to vote")    

#Method overloading
# def product(a, b):
#     p = a * b
#     print(p)
 
# def product(a, b, c):
#     p = a*b*c
#     print(p)

# #product(5,7)  
# product(4, 5, 5)   

# calc = lambda num: "Even number" if num % 2 == 0 else "Odd number" 
# print(calc(20)) 

# #try_except 
# try: 
#     numerator = 10 
#     denominator = 0
#     result = numerator/denominator 
#     print(result) 
# except: 
#     print("Error: Denominator cannot be 0.")
# finally:
#     print("The rest of the code ")   

# #Declaring a list 
# L = [1, 'a' , "string" , 1+2] 
# print (type(L)) 
# #Adding an element in the list 
# L.append(6) 
# print(L)
# L += [23,49,57]
# print (L) 
# #Deleting last element from a list 
# L.pop() 
# print (L) 
# #Displaying fourth element of the list 
# print (L[3])    

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


# #try_except 
# try: 
#     numerator = 10 
#     denominator = 0
#     result = numerator/denominator 
#     print(result) 
# except: 
#     print("Error: Denominator cannot be 0.")

# finally:
#     print("This is the rest of the code")    

#LIST

# l = [1,4.5,'sabin',9+7]
# print(l)
# print(type(l))
# l.append(53)
# print(l)
# l += ['cat','dog','mouse']
# print(l)
# l.pop()
# print(l)
# print(l[3])

#Tuple

# t = (1,'a',"string",1+8)
# print(t)
# print(type(t))
# print(t[2])

# tup = t + (4,5,6)
# print(tup)
  

# #Dictionary

# dict = {1:"CSIT",2:"BCA",3:"BIM"}
# print(dict)

# dict[4]="BHM"
# print(dict)

#Method overloading
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
# product(4, 5, 5)   

# #Pyramid
# n = int(input("Enter a value: "))
# def pyramid(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("* ",end="")
#         print('\r')
# pyramid(n)  
#-----------------------------------------------------------------------------------------------------------------------
#Assignment (1)
#Table of 7
# for i in range(1, 11):
#     print("7 x", i, "=", 7*i) 

#Assignment 2
# Create a class called "Rectangle" that has two attributes: "length" and "width".
# The class should have a method called "area" and "perimeter" that calculates the area & perimeter of the rectangle.
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         print("Area of rectangle is: ",(self.length * self.width))

#     def perimeter(self):
#         print("Perimeter of rectangle is: ",2*(self.length+self.width))    

# rect = Rectangle(5,4)
# rect.area()     
# rect.perimeter() 

#Assignment 3

# Create a class called "BankAccount" that has two attributes: "balance" and "account_number". 
# The class should have methods called "deposit" and "withdraw" that allow a user to deposit or withdraw
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

#Assignment 4: Write a program that takes a list of words as input and returns a new list 
#containing only the words that have more than three letters and start with the letter 'a',
#sorted in alphabetical order.

# word_list = ['apple', 'banana', 'ant', 'cat', 'act', 'acorn', 'bat','zebra']
# new_list = []

# for word in word_list:
#     if len(word) > 3 and word[0] == 'a':
#         new_list.append(word)

# new_list.sort()
# print(new_list)  

#Assignment 5
#Simple number guessing game
# import random

# # Generate a random number between 1 and 10
# secret_number = random.randint(1, 10)


# print("Welcome to the Guess the Number game!")

# while True:
#     try:
#         guess = int(input("Enter your guess (between 1 and 10): "))

#         if 1 <= guess <= 10:
#             if guess == secret_number:
#                 print(f"Congratulations! You guessed the correct number, which was {secret_number}.")
#                 break
#             else:
                
#                 print("Wrong guess. Try again!")
#         else:
#             print("Please enter a number between 1 and 10.")

#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")

# #End of the game

#Assignment 6: Write a program that takes a list of words as input and returns a new list 
#containing only the words that have less than five letters and do not start with the letter 'b',
#sorted in reverse alphabetical order.

# word_list = ['apple', 'banana', 'ant', 'cat', 'act', 'acorn', 'bat','zebra']
# new_list = []

# for word in word_list:
#     if len(word) < 5 and word[0] != 'b':
#         new_list.append(word)

# new_list.sort()
# new_list.reverse()
# print(new_list)  



#Assignment 4: Write a program that takes a list of words as input and returns a new list 
#containing only the words that have less than five letters and do not start with the letter 'b',
#sorted in reverse alphabetical order.



# Create a class called "BankAccount" that has two attributes: "balance" and "account_number". 
# The class should have methods called "deposit" and "withdraw" that allow a user to deposit or withdraw
# money from the account.The balance should be updated accordingly. 