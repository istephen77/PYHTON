# n = 0
# n = int(input("Enter Number : "))
# if True:
#     n += 1
# print(n)


# age = int(input("Enter your age: "))
# if age > 18:
#     print("You are eligible to Vote")


#
# age = int(input("Enter Age : "))
# if(age>=18 and age<=120):
#     print("You are eligible to vote.")
# else:
#     print("Sorry,You are not eligible to vote")


# number = int(input("Enter Number: "))
#
# if number % 2 == 0:
#     print(number,'Number Is Even')
# else:
#     print(number,'Number is Odd')


# salary = int(input("Enter you salary :"))
# gender = input("Enter yor Gender m or f:")
#
# if gender.lower() == 'm':
#     bonus = salary * 0.10
# else:
#     bonus = salary * 0.25
#
# final_salary = salary + bonus
# print("Actual salary :", salary)
# print("Bonus :", bonus)
# print("Final salary :", final_salary)


# x = int(input("Enter number :"))
# if x > 0:
#     print("Positive number")
# elif x == 0:
#     print("Zero")
# else:
#     print("Negative number")


# list('aeiou')
# a = input("Enter any letter: ")
#
# if a in list('aeiou'):
#     print(a, "is vowel")
#
# elif a in list('AEIOU'):
#     print(a, "is vowel")
#
# else:
#     print(a, "is consonant")

#
# n = int(input("Enter number : "))
#
# if n%2==0:
#     if n >= 2 and n <=5:
#         print(n, "is Small")
#     elif n>= 6 and n <=20:
#         print(n,"is Medium")
#     elif n>20:
#         print(n, "is Big")
# else:
#     print(n, "is Odd")


# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# count = 1
# sum = 0
# avg = 0
# while count <= 10:
#     sum += count
#     count += 1
#     avg = sum // count
# print('Sum  = ',sum)
# print('Average = ',avg)

# i = 1
# while i <= 50:
#     print('-', end= ' ')
#     i += 1


# m = int(input("Enter M : "))
# n = int(input("Enter N : "))
# sum = 0
# while m <= n:
#     sum = sum + m
#     m += 1
# print(sum)


# i = 10
# while i >= 0:
#   print(i)
#   i = i - 1

# n = int(input("Input a number: "))
# for i in range(1,11):
#  print(n,'x',i,'=',n*i)

# m = int(input("Enter M: "))
# n = int(input("Enter N: "))
# for i in range(m,n):
#     if i % 2 == 0:
#         print('{} is {}'.format(i,'even'))
#     else:
#         print('{} is {}'.format(i,'odd'))


# for x in "stephin":
#     if x == "i":
#         break
#     print(x)

# car=["Audi","BMW","Mercedes","Volkswagon","Porche","Fiat"]
# for x in car:
#     if(x=="Volkswagon"):
#         continue
#     print(x)

# for i in range(1800,2022):
#     if i%4==0:
#         print(i,' is leap year')



# def add(n1, n2):
#   return n1+n2
#
# def sub(n1, n2):
#   return n1-n2
#
# def mul(n1, n2):
#   return n1*n2
#
# def div(n1, n2):
#   return n1/n2
#
# num1 = int(input("Enter num1 : "))
# num2 = int(input("Enter num2 : "))
# print("****************")
# print("Addition : ",add(num1,num2))
# print("Subtraction : ",sub(num1,num2))
# print("Multiplication : ",mul(num1,num2))
# print("Division : ",div(num1,num2))

#
# def welcome():
#     name = input(" Enter your Name :")
#     if name:
#         print(f'Welcome to Facebook, {name}')
#     else:
#         print('Name not provided')
# print(welcome())

# sum1 = lambda a,b: a+b
# print(sum1(6,3))


list1 = []
for i in range(11):
    if i>=1:
        list1.append(i)
print(list1)

even = list(filter(lambda x : x%2==0, list1))
print(even)

m = list(map(lambda x: x**2, list1))
print(m)

#
# from functools import reduce
#
# sum_list = reduce(lambda x,y: x+y, list1)
# print(sum_list)


#Q1
# class target_number:
#   def sum(self,nums, target):
#        search = {}
#        for i, num in enumerate(nums):
#            if target - num in search:
#                return (search[target - num], i )
#            search[num] = i
# print("index_1 = %d, index_2 = %d"% target_number().sum((10,20,10,20,40,50,40,50,60,100),100))

#Q2
# class Critical_River_Python_Students:
#
#     def __init__(self, student_id, student_name):
#         self.student_id = student_id
#         self.student_name  = student_name
#
#     def student_info(self):
#         print(f"Student ID: {self.student_id} ")
#         print(f"Student Name : {self.student_name} ")
#
# class student(Critical_River_Python_Students):
#     def student_details(self):
#         print(f"Student ID: {self.student_id} ")
#         print(f"Student Name : {self.student_name} ")
#
# stephin = student("1408","Stephin")
# stephin.student_details()

#Q4
# num = int(input("Enter num: "))
# def factorial(n):
#    if n == 1:
#        return n
#    else:
#        return n*factorial(n-1)
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    print("The factorial of", num, "is", factorial(num))


#Q5
# Encapsulation :
# class employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self._age = age
#         self.__salary = salary
#
#     def get_salary(self):
#         return self.__salary
#
#     def set_salary(self, updated_sal):
#         self.__salary = updated_sal
#
#     def __verification(self):
#         print("I am a private method !")
#
#     def get_verification(self):
#         return  self.__verification()
#
#     def set_verification(self, updated_ver):
#         self.__verification = updated_ver
#
# stephin = employee("Stephin", 25, 45000)
# stephin.set_salary(60000)
# print(stephin.get_salary())
# print(stephin.get_verification())
# print(stephin.name)
# print(stephin._age)
# print(stephin._employee__salary)
#
# Polymorphism
#
# class expenses:
#     def __init__(self, exp):
#         self.expenses = exp
#
#     def __add__(self, other):
#         print(self.expenses + other.expenses)
#
# friends = expenses(2000)
# medical = expenses(3000)
# friends + medical
#
# Inheritence
# class father:
#     def house(self):
#         print("I am a Parent and I own a house !")
#
# class mother():
#     def car(self):
#         print("I am a Mother and I own a car !")
#
# class child(father,mother):
#     def bike(self):
#         print("I am a Child and I own a bike !")
#
# stephin = child()
# stephin.bike()
# stephin.car()
# stephin.house()
#
#
# Abstraction
# from abc import ABC, abstractmethod
# class parent(ABC):
#     @abstractmethod
#     def addition(self):
#         pass
#     def subtraction(self):
#         pass
#
# class child(parent):
#     def __init__(self,n1,n2):
#         self.num1 = n1
#         self.num2 = n2
#
#     def addition(self):
#         return self.num1 + self.num2
#
#     def subtraction(self):
#         return self.num1 + self.num2
#
# x = int(input("Enter Num1 : "))
# y = int(input("Emter Num2 : "))
# stephin = child(x,y)
# print(stephin.addition())


# Q6
# from math import pi
#
# def calc_area_peri(r):
#     return pi * r * r, 2 * pi * r
#
# area, perimeter = calc_area_peri(10)
# print('Area=', area)
# print('Circumference=', perimeter)




