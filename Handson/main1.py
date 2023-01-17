# import pickle
#
# # myCar = ["Audi", "BMW", "Tata", "Tesla", "Suzuki"]
# # file = "myCar.pkl"
# # file_obj = open(file,"wb")
# # pickle.dump(myCar, file_obj)
# # file_obj.close()
#
#
# file = "myCar.pkl"
# file_obj = open(file,"rb")
# carList = pickle.load(file_obj)
# print(carList)
# print(type(carList))
#
#
# class car:
#     def car_purchase(self, name, color):
#         print(f"Name : {name}, Color : {color}")
# x = car()
# x.car_purchase("BMW", "Black")
# y  = car()
# y.car_purchase("Audi", "White")
#
# By using init() for reducing the complexity and resuability of code
# class mobile:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def mobile_purchase(self):
#         print(f"Name: {self.name}, Color : {self.color}")
#
# x = mobile("Samsung", "Black")
# x.mobile_purchase()
# y = mobile("Apple", "White")
# y.mobile_purchase()
#
# class variable : A class variable can be shared by all instance methods of the class
# instance method : an instance methods can only be accessed by creating an object of the class, an instance methods doesn't belong to the class
#
# class vehicle:
#     equipments = 'Equipments : Available' #class variable
#     def __init__(self, name, brand, color):  #instance method
#         self.name = name
#         self.brand = brand   #value of instances or operations are initialized inside init()
#         self.color = color
#
#     def vehicle_purchase(self):
#         print(f"Name : {self.name} Color : {self.color}  Brand : {self.brand}")
#
# x = vehicle("Audi Motors", "Black", "Audi")
# x.vehicle_purchase()
# print(x.equipments)  #class variable
# print(vehicle.equipments)
#
# class method
#
# class mobile:
#     charger = "Yes"
#
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def mobile_purchase(self):
#         print(f"Name : {self.name} Color : {self.color}")
#
#     @classmethod
#     def verification(cls):
#         print("Charger Available : ", cls.charger)
#
# x = mobile("Samsung", "Black")
# x.mobile_purchase()
# x.verification()
# mobile.verification()
#
# Static method
#
# class test:
#     charger = "Yes"
#
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def test_method1(self):
#         print(f"Name : {self.name} Color : {self.color}")
#
#     @classmethod
#     def test_method2(cls):
#         print("Charger Available : ", cls.charger)
#
#     @staticmethod
#     def test_method3(a,b):
#         print("Addition : ",a+b)
# x = test("Test","Alpha")
# x.test_method1()
# x.test_method2()    #Class method accessed with use of object or instance
# test.test_method2() #Class method accessed with use of class name
# test.test_method3(10,20)  #Static method accessed with use of class name
#
# Code to illustrate composition - Strong association
#
# class flipkart:
#     def __init__(self):
#         print("Welcome to FLipkart")
#
#     class men:
#         def __init__(self):
#             print("Welcome to Men's section!")
#
#         class footwear:
#             def __init__(self, name, color):
#                 print("Welcome to footwear section")
#                 self.name = name
#                 self.color = color
#
#             def nike(self):
#                 print(f"Name : {self.name} , Color : {self.color}")
#
#             def addidas(self):
#                 print(f"Name : {self.name} ,  Color : {self.color}")
#
#         class clothing:
#             class footwear:
#                 def __init__(self, name, color):
#                     print("Welcome to clothing section")
#                     self.name = name
#                     self.color = color
#
#                 def denim(self):
#                     print(f"Name : {self.name} , Color : {self.color}")
#
#                 def levis(self):
#                     print(f"Name : {self.name} , Color : {self.color}")
#
#     class women:
#         def __init__(self):
#             print("Welcome to Women's section!")
#
#         class footwear_w:
#             def __init__(self, name, color):
#                 print("Welcome to footwear section")
#                 self.name = name
#                 self.color = color
#
#             def nike_w(self):
#                 print(f"Name : {self.name} , Color : {self.color}")
#
#             def addidas_w(self):
#                 print(f"Name : {self.name} , Color : {self.color}")
#
#         class clothing_w:
#             class footwear_w:
#                 def __init__(self, name, color):
#                     print("Welcome to clothing section")
#                     self.name = name
#                     self.color = color
#
#                 def denim_w(self):
#                     print(f"Name : {self.name} ,  Color : {self.color}")
#
#                 def levis_w(self):
#                     print(f"Name : {self.name} , Color : {self.color}")
#
# x = flipkart.men.footwear("Nike", "Black")
# x.nike()
# y = flipkart.men.footwear("Addidas", "Red")
# y.addidas()
#
#
# Aggregation - weak association
#
# class laptop_details :
#     def __init__(self, name, brand, color, inch):
#         self.name = name
#         self.brand = brand
#         self.color = color
#         self.inch = inch
#
#     def laptop_info(self):
#         print(f"Name : {self.name}, Brand : {self.brand}, Color : {self.color}, Inch: {self.inch}")
#
# class employee_details:
#     def __init__(self, emp_no, emp_name, lap_det):
#         self.emp_no = emp_no
#         self.emp_name = emp_name
#         self.lap_det = lap_det
#
#     def emp_info(self):
#         print(f"Employee NO : {self.emp_no}. Employee Name : {self.emp_name}, Laptop Details : ")
#         self.lap_det.laptop_info()
#
# x = laptop_details("HP","Pavilion","Black","32")
# y = employee_details(101, "Stephin Sebastian", x)
# y.emp_info()
#
# class processor:
#     def __init__(self, name):
#         self.name = name
#
#     def processor_info(self):
#         print(f"Thanks for purchasing {self.name}")
#
#
# class camera:
#     def __init__(self, name):
#         self.name = name
#
#     def camera_info(self):
#         print(f"Thanks for purchasing {self.name}")
#
# class mobile_display:
#     def __init__(self, name):
#         self.name = name
#
#     def mobile_display_info(self):
#         print(f"Thanks for purchasing {self.name}")
#
# class iphone:
#     def __init__(self):
#         self.processor = processor("Processor")
#         self.camera = camera("Camera")
#         self.mobile_display = mobile_display("Mobile Display")
#
#     def iphone_info(self):
#         print("Welcome to iPhone")
#         self.processor.processor_info()
#         self.camera.camera_info()
#         self.mobile_display.mobile_display_info()
#
# x = iphone()
# x.iphone_info()
#
# Single Inheritence :
#
# class parent:
#     def parentmethod(self):
#         print("I am Parent")
#
# class child(parent):    #parent class is injected into the child class
#     def childmethod(self):
#         print("I am Child")
# x = child()
# x.parentmethod()    #parent class can be accessed by using the instance or object of the child class
# x.childmethod()
#
# Multi-Level inheritence
# class parent:
#     def parentmethod(self):
#         print("I am Parent")
#
# class child(parent):    #parent class is injected into the child class
#     def childmethod(self):
#         print("I am Child")
#
# class grandchild(child):
#     def grandchildmethod(self):
#         print("I am a grandchild")
# x = grandchild()
# x.parentmethod()
# x.childmethod()
# x.grandchildmethod() #parent class can be accessed by using the instance or object of the grandchild class
#
# Hiearchial Inheritence
#
# class parent:
#     def parentmethod(self):
#         print("I am a parent")
#
# class child1(parent):
#     def child1method(self):
#         print("I am a child1")
#
# class child2(parent):
#     def child2method(self):
#         print("I am a child2")
#
# x = child1()
# x.parentmethod()
# y = child2()
# y.parentmethod()
#
# Multiple inheritence
#
# class father:
#     def fmethod(self):
#         print("I am father")
#
# class mother:
#     def mmethod(self):
#         print("I am mother")
#
# class child(father, mother):
#     def child(self):
#         print("I am a child")
#
# x = child()
# x.fmethod()
# x.mmethod()
#
# Enumerators
#
# list1 = ["Red","Blue","Black","Green","Grey","Voilet"]
# list2 = ["Rose","Sunflower","Jasmine","Lotus","Mogra","Tulip"]
# list3 = "Rose"
# list4 = ["Rose"]
#
# x = enumerate(list1)
# for count in x:
#     print(count)
#
# y = enumerate(list2, 100)
# for cout, xls in y:
#     print(cout)
#     print(xls)
#
# Encapsulation - Private, protected and Public
#
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
#         print("I am a private method")
#
#     def get_verification(self):
#         return self.__verification()
#
#     def set_verification(self, updated_ver):
#         self.__verification = updated_ver
#
# x = employee("Stephin", 26, 50000)
# x.set_salary(50000)
# print(x.get_verification())
# print(x.name)
# print(x._age)
# print(x._employee__salary)
#
# Abstraction
#
# from abc import ABC, abstractmethod
# class parent(ABC):
#     @abstractmethod
#     def addition(self):
#         pass
#
#     def subtraction(self):
#         pass
#
# class child(parent):
#     def __init__(self, n1,n2):
#         self.num1 = n1
#         self.num2 = n2
#
#     def addition(self):
#         return self.num1 + self.num2
#
#     def subtraction(self):
#         return self.num1 - self.num2
#
# x = int(input("Enter num 1 : "))
# y = int(input("Enter num 2 : "))
# obj = child(x,y)
# print(obj.addition())
# print(obj.subtraction())
#
# Polymorphism :
# a=50
# b=20
# x='30'
# y='20'
# print(int.__add__(a,b))
# print(str.__add__(x,y))
# class test:
#     def __init__(self, exp):
#         self.expenses = exp
#
#     def __add__(self, other):
#         print(self.expenses, other.expenses)
#
# friends = test(3000)
# medical = test(2000)
# friends + medical
#
# class test:
#     def __init__(self, num1):
#         self.num1 = num1
#
#     def __add__(self, add):
#         print(self.num1 + add.num1)
#
#     def __mul__(self, other):
#         print(self.num1 * other.num1)
#
# x = test(100)
# y = test(200)
# z = test(300)
# x+y
# x*z
# x*y
#
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
#         print("This is a private method")
#
#     def get_verification(self):
#         return self.__verification()
#
#     def set_verification(self, updated_ver):
#         self.__verification = updated_ver
#
# x = employee("Stephin", 26, 60000)
# print(x.get_salary())
# print(x.get_verification())
# print(x.name)
# print(x._age)
# print(x._employee__salary)
#
# class employee:
#     def __init__(self, name, age, salary, pvt_age, pvt_sal):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self._pvt_age = pvt_age
#         self.__pvt_sal = pvt_sal
#
#     def get_age_info(self):
#         print(f"Name : {self.name}, Age : {self.age}, Salary : {self.salary}")
#
#     def get_pvt_age(self):
#         return self._pvt_age
#
#     def set_pvt_age(self, updated_age):
#         self._pvt_age = updated_age
#
#     def get_pvt_sal(self):
#         return self.__pvt_sal
#
#     def set_pvt_sal(self, updated_sal):
#         self.__pvt_sal = updated_sal
#
# class laptop_details:
#     def __init__(self, brand, color, emp_det):
#         self.brand = brand
#         self.color = color
#         self.emp_det = emp_det
#
#     def lap_info(self):
#         print(f"Brand : {self.brand}, Color : {self.color}, Emp_Det : ")
#         self.emp_det.get_age_info()
#
# x = employee("Stephin", 26, 45000, 25, 60000)
# y = laptop_details("HP","Black",x)
# y.lap_info()
# print(x.get_pvt_age())
# print(x.get_pvt_sal())
#
# from abc import ABC, abstractmethod
# class mobile_design(ABC):
#
#     @abstractmethod
#     def mobile_camera(self):
#         pass
#
#     @abstractmethod
#     def mobile_screen(self):
#         pass
#
#     def mobile_charger(self):
#         pass
#
# class mobile_design_info(mobile_design):
#     def mobile_screen(self):
#         print("Welcome to mobile screen")
#
#     def mobile_camera(self):
#         print("Welcome to mobile camera")
#
#     def mobile_charger(self):
#         print("Welcome to mobile charger")
#
# x = mobile_design_info()
# x.mobile_screen()
# x.mobile_charger()
#
#
# Method Overloading is not possible in python as it always considers the excution of the latest method which is being defined
# class test:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def method(self):
#         print("Method 1")
#
#     def method(self):
#         print("Method 2", self.a)
#
#     def method(self):
#         print("Method 3", self.a, self.b)
#
# x = test(1,2)
# x.method()
#
# Method 1 - to overcome the problem of method oevrloading in python
#
# class test:
#     def add(self, datatypes, *args):
#         if datatypes == 'int':
#             answer=0
#
#         if datatypes == 'str':
#             answer=''
#
#         for x in args:
#             answer = answer + x
#
#         print(answer)
#
# y = test()
# z = test()
# y.add('int',5,6)
# y.add('int',12,12,23,34,45)
# z.add('str', 'Hello', 'Stephin')
#
# *args is a special non-keyword used to overcome the problem of method overloading in python. With the help of *args there is no need to write multiple functions with same names and different arguments, instead we can use the *args as an object and iterate for loop over it to get the desired result.
#
# class test:
#     def test_method(self, *num):
#         total = 1
#         for x in num:
#             total *= x
#
#         print("Total : ", total)
#
# x = test()
# x.test_method(5,5,5)
#
# Method Overriding
#
# class test:
#     def test_method1(self):
#         print("This is method 1")
#
# class test1(test):
#     def test_method1(self):
#         print("This is method 1.1")
#
# x = test1()
# x.test_method1()  #Here test_method1 of child class is overriding the same method name from parent class
#
# class parent:
#     def mobile(self):
#         print("Parent have Samsung")
#
# class child(parent):
#     def mobile(self):
#         super().mobile()   #Used to call the parent class method inside the child class
#         print("I have iPhone")
#
# x = child()
# x.mobile()
#
# class company:
#     def __init__(self, company_name):
#         self.company_name = company_name
#
#     def display_info(self):
#         print(f"Company Name : {self.company_name}")
#
# class employee(company):
#     def __init__(self, company_name, employee_name):
#         super().__init__(company_name)
#         self.employee_name = employee_name
#
#     def display_info(self):
#         print("Company Name : ", self.company_name)
#         print("Employee Name : ", self.employee_name)
#
# x = employee("Mu Sigma", "Stephin Sebastian")
# x.display_info()
#
# name, model , wheels, price, payment type
#
# class car:
#     def __init__(self, name, model, wheels):
#         self.name = name
#         self.model = model
#         self.wheels = wheels
#
#     def display(self):
#         print(f"Name : {self.name}, Model : {self.model}, Wheels : {self.wheels}")
#
# class car_info(car):
#     def __init__(self, name, model, wheels, price, payment_type):
#         super().__init__(name, model, wheels)
#         self.price = price
#         self.paymen_type = payment_type
#
#     def display(self):
#         super().display()
#         print(f"Price : {self.price}. Payment Type : {self.paymen_type}")
#
# x = car_info("Mercedes","S Class",4,100000,"Bitcoin")
# x.display()
#
# class mobile:
#     def __init__(self, name, ram, color):
#         self.name = name
#         self.ram = ram
#         self.color = color
#
#     def display(self):
#         print(f"Name : {self.name}, Brand : {self.ram}, Color : {self.color}")
#
# list_of_mobile = []
#
# while True:
#     name = input("Enter the name of the mobile : ")
#     ram = int(input("Enter the required RAM : "))
#     color = input("Enter the color : ")
#     m = mobile(name, ram , color)
#     list_of_mobile.append(m)
#     repeat_order = input("Do you want to make purchase again ? [Yes/No] : ")
#     if repeat_order.lower() == 'no':
#         break
#
# for x in list_of_mobile:
#     x.display()
#
# Method - 2 which is efficient way to handle method overloading
# from multipledispatch import dispatch
# class dispatch_func:
#
#     @dispatch(int,int)
#     def product(self, first, second):
#         result = first*second
#         print(result)
#
#     @dispatch(int,int,int)
#     def product(self, first, second, third):
#         result = first*second*third
#         print(result)
#
#     @dispatch(float, float, float)
#     def product(self,first, second, third ):
#         result = first * second * third
#         print(result)
#
# x = dispatch_func()
# x.product(2,3)
# x.product(3,4,5)
# x.product(2.3,4.5,3.5)
#
#
# String slicing and other functions - Advanced Indexing
#
# mystr = "Stephin is a Data Engineer is"
# print(mystr)
# print(mystr[0:5])  #[n:n-1]
# print(len(mystr[0:5]))
# print(len(mystr))
# print(10 * mystr )
# print(mystr[::])
# print(mystr[:5:])
# print(mystr[:5:2])   # [n:n:n-1] - It will skip 1 character and then print the rest
# print(mystr[::76666])
#
# Negative Indexing
#
# print(mystr[-4:-2])  #[n,n-1] - negative indices can be resolved by converting it into positive indices
#
# Reversing a string
# print(mystr[::-2])
#
# print(mystr.capitalize())
# print(mystr.casefold())
# print(mystr.center(40,"x"))
# print(mystr.count('a'))
# print(mystr.encode())
# print(mystr.endswith("Engineer"))
# print(mystr.expandtabs(3))
# print(mystr.find("is"))
# print((mystr.index("a"))) ---- similar to find()
#
# txt = "Item is priced at {price:.2f}"
# print(txt.format(price=100))
#
# txt = "My name is {fname} and i am from {city}".format(fname = "Stephin", city = "Mumbai")
# print(txt)
#
# txt =  "My name is {0} and i am from {1}".format("Stephin","Mumbai")
# print(txt)
#
# txt = "My name is {} and i am from {}".format("Stephin","Mumbai")
# print(txt)
#
# dict1 = {"name": "John", "country": "Norway"}
# seperator = "_"
# x = seperator.join(dict1)
# print(x)
#
# x = mystr.maketrans("a","X")
# print(mystr.translate(x))
# print(mystr.partition("Data"))
# maketrans-translate and replace are kind of similar to each other
#
# print(mystr.replace("is", "are"))
#
# print(mystr.rfind("is")) ----> similar to rindex()
#
# str1 = '.,.,.,.88stephin****'
# print(str1.swapcase())
# print(str1.strip(".,8*"))
# print(mystr.startswith("Stephin"))
#
# mystr1 = "Stephin is a useless & unemployed fellow"
# print(mystr1.split())
# print(mystr1.split("&"))
# print(mystr1.split("&",2))
#
# str1 = "Stephin"
# x = str1.ljust(30)
# print(x,"is a bad guy")
# print(len(x))
#
# str2 = "is a bad guy"
# x = str2.rjust(30)
# print("Stephin",x)
# print(len(str2))
#
# List and Tuple
# car = ["BMW","Audi","Lamborghini", "Pagani Zonda", "Ferrari", "Maserati", "Range Rover"]
# print(car)
# print(len((car)))
# for x in car:
#     print(x)
#
# number = [34,21,35,1,31,12,39,123,322,12,8,4,6,23,9,32,1]
# number1 = [45,34,54,4,323,34,3,434]
# number.append(12)
# print(number)
# number.clear()  a,c,c,c,e,i,i,p,r,r,s
# print(number)
# number.copy()
# print(number)
# x = number.count(12)
# print(x)
# number.extend(number1)
# print(number)
# number.insert(0,100)
# print(number)
# x = number.index(322)
# print(x)
# number.pop(0)
# print(number)
# number.pop()
# print(number)
# number.remove(322)
# print(number)
# number.reverse()
# print(number)
# number.sort()
# print(number)
#
#  List Slicing
# print(number[::-1])
# print((number[0:4]))
# print(number[::2])
#
#
# dictionary = {"Naucet":"Tap",
#               "Happy":"An emotion",
#               "Laugh": "An expression",
#               "Cow":"An Animal",
#               "Israel":"Country in Middle East",
#               "Switzerland":"Rich peopl's country",
#               "Russia":"Apartheid State"
#               }
#
# word = input("Enter Word : ")
# print(dictionary.get(word))
# print(dictionary[word])
# dictionary1 = dictionary
# print(dictionary1)
# del dictionary1["Cow"]
# print(dictionary)
# dictionary_new = dictionary.copy()
# del dictionary_new["Cow"]
# print(dictionary)
# dictionary.update({"Cock":"A bird"})
# print(dictionary)
#
# s = set()
# print(type(s))
# l = [1,2,3,4,5,6]
# s = set(l)
# # print(s)
# l1 = [11,23,2,3,43,34]
# s1 = set(l1)
# # print(s1)
# print(s.intersection(s1))
# print(s.isdisjoint(s1))
# print(s.difference(s1))
#
# Faulty calculator
#
# def add(n1, n2):
#     list = [56,9]
#     if (n1!=n2) and (n1 in list) and (n2 in list):
#         return 77
#     else:
#         return n1 + n2
#
# def sub(n1, n2):
#     return n1 - n2
#
# def mul(n1, n2):
#     list = [45,3]
#     if (n1!=n2) and (n1 in list) and (n2 in list):
#         return 555
#     else:
#         return n1 * n2
#
# def div(n1, n2):
#     list = [56,5]
#     if (n1 == list[0 and n2 == list[1]]):
#         return 4
#     else:
#         return n1/n2
#
# print("Choose a number : 1) Addition 2) Subtraction 3) Multiplication  4) Division")
# n = int(input("Enter the number : "))
# a = int(input("Enter 1  : "))
# b = int(input("Enter 2 : "))
# if n==1:
#     print("Addition : ", add(a,b))
# elif n==2:
#     print("Subtraction : ", sub(a,b))
# elif n==3:
#     print("Multiplication : ", mul(a,b))
# else:
#     print("Division : ", div(a,b))
#
# List Comprehension
#
# ls = []
# for x in range(100):          ------> #Traditional approach
#     if x%3==0:
#         ls.append(x)
# print(ls)
#
# ls = [i for i in range(100) if i%3==0]         ---------> #List Comprehension
# print(ls)
#
# Dictionary comprehension
# dict1 = {i : f"item {i}" for i in range(1,1001) if i%100==0}
# print(dict1)
#
# dict1 = {i : f"item {i}" for i in range(5)}
# dict1 = {value:key for key,value in dict1.items()}
# print(dict1)
#
# Set comprehension
#
# dresses = {dress for dress in ["dress1", "dress1", "dress1", "dress2", "dress2", "dress2"]}
# print(dresses)
#
# Generate comprehension :
#
# evens = (i for i in range(100) if i%2==0)
# print(type(evens))
# print(evens.__next__())
# for items in evens:
#     print(items)
#
#
# Generators
#
# Iterable -  Iterable is a python object on which __iter__ or __getitem__() method is run on top of it to obtain Iterators
# Iterators - __next__()
# Iteration - performed on iterators
#
# def gen(n):
#     for i in range(n):
#         yield i
#
# g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
#
# h = "Stephin"
# x = iter(h)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
#
# Factorial using generators
#
# limit = int(input("Enter the number : "))
#
# def factorial(limit):
#     facto = 1
#     for i in range(1, limit+1):
#         facto *= i
#     yield facto
#
# generator = factorial(limit)
# for x in generator:
#     print("Factorial : ",x)
#
# Fibonacci using generators
#
# fibo = int(input("Enter number : "))
#
# def fibonacci(fibo):
#     a,b = 0,1
#     while(a<=fibo):
#         a,b = b, a+b
#     yield a
#
# x = fibonacci(fibo)
# for y in x:
#     print("Fibonacci : ", y)
#
# no_of_elements = int(input("Enter the nunber of elements in the list : "))
# list1 = []
# for x in range(no_of_elements):
#     y = input("Enter the elements : ")
#     list1.append(y)
#
# print("[AVAILABLE OPTIONS] : 1) LIST COMPREHENSION 2) DICTIONARY COMPREHENSION 3) SET COMPREHENSION ")
# option_input = int(input("Enter the option : "))
# if option_input == 1:
#     ls = [i for i in list1]
#     print(ls)
#
# elif option_input == 2:
#     ls = {i : f"item {j}" for i in range(list1) for j in range(1, len(list1) + 1)}
#     print(ls)
#
# elif option_input == 3:
#     ls = {i for i in list1}
#     print(ls)
#
# else: print("INVALID INPUT !")
#
# For loop
#
# list1 = [["Car",1],["Bike",2],["Jeep",3],["Airplane",4],["Super-Car",5],["Helicopter",6]]
# for x,y in list1:
#     print(x,y)
#
# list1 = [["Car",1],["Bike",2],["Jeep",3],["Airplane",4],["Super-Car",5],["Helicopter",6]]
# dict1 = dict(list1)
# for x,y in dict1.items():
#     print(x,y)
#
# ls = [int, float, "sheep", 45,3,4,5,23,4,5,34,23,342]
# for x in ls:
#     if str(x).isnumeric() and x > 23:
#         print(x)
#
# While loop
# i = 1
# while(i<=45):
#     print(i)
#     i+=1
#
# i = 1
# while(i<=45):
#     print()
#
# ********************************************************(iNeuron-Python)***********************************************
#
