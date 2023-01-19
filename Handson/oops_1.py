# class mobile:
#     def mobile_purchase(self,name,color):
#         print(f"Thanks for purchasing {name} with {color} color!")
#
#
# stephin = mobile()       #"stephin" is an instance of a class which has it's own unique state and behaviour
# stephin.name = "Samsung"  #Instance variable which are bound to the object
# stephin.color = "Red"   #Instance variable which are bound to the object
# stephin.mobile_purchase(stephin.name,stephin.color)
#
# aya = mobile()
# aya.name = "Apple"
# aya.color = "Rose Gold"
# aya.mobile_purchase(aya.name, aya.color)
#
# class car:
#     def car_purchase(self,name, color):
#         print(f"Thanks for purchasing {name} with {color}  color")
#
# x = car()
# x.name = "Audi"
# x.color = "Red"
# x.car_purchase(x.name,x.color)

# class car:
#
#     def __init__(self,name,color):     #init ()function to assign values to object properties, or other operations. init() method is called first when the class is executed
#         self.name = name                #self act as an object or instance
#         self.color = color                #name and color are instance variables
#
#     def car_purchase(self):
#         print(f"Thanks for purchasing {self.name} with {self.color} color !!")
#
# stephin = car("Audi","Black")
# stephin.car_purchase()
#
# aya = car("BMW","Red")
# aya.car_purchase()



# class car:
#
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def car_purchase(self):
#         print(f"Thanks for purchasing {self.name} with {self.color} color !")
#
# x = car("Audi","Rose Gold")
# x.car_purchase()

# class variable - A variable that is shared by all instances of a class is called class variable
# class mobile:
#     charger = " Charger : Available"  #Class variable which is shared by both instances or objects
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#
#     def mobile_purchase(self):
#         print(f"Thanks for purchasing {self.name} with {self.color} color !")
#
# stephin = mobile("Samsung", "Red")
# stephin.mobile_purchase()
# print(stephin.charger)
#
# aya = mobile("Apple", "Silver")
# aya.mobile_purchase()
# print(aya.charger)

# Instance method - belong to the object of the class, not to the class so they can be called after creating the object of the class
#
# class mobile:
#
#     charger = " Charger : Available"  #Class variable which is shared by both instances or objects
#
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#
#     def mobile_purchase(self):        #instamce method - cannot be accessed outside the class without creating an object
#         print(f"Thanks for purchasing {self.name} with {self.color} color !")
#
# stephin = mobile("Samsung", "Red")
# stephin.mobile_purchase()
# print(stephin.charger)
#
# aya = mobile("Apple", "Silver")
# aya.mobile_purchase()
# print(aya.charger)

# Class methods - doesn't need self as an argument but they do need a parameter called "cls" and this stands for class and like self gets automatically passed in by python
# if we want to access anything assigned in class variable then use class methods
# if we want to access anything assigned in instance variable then use instance methods
# if we  do not want to access anything assigned in class variable or instance variable then use static methods
# class mobile:
#     charger = "Yes"
#
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#
#     def mobile_puchase(self):
#         print(f"Thanks for purchasing {self.name} with {self.color} color !")
#
#     @classmethod                   #Can be accessed without the object by using a decorator "@classmethod above the class method. Can be accessed by using an object. Good in terms of memory management as there is no need to create an object
#     def verification(cls):
#         print("Charger is Available ? ",cls.charger)
#
# mobile.verification()  #class method accesed without using an object
# stephin = mobile("Samsung","Black")
# stephin.mobile_puchase()
# stephin.verification()  # #class method accesed with using an object
#
#
# Static methods - takes neither a self nor a cls parameter but it's free to accept any arbitary number of other parameters. Helpful to access other class objects
#
# class mobile:
#     charger = "Yes"
#
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#
#     def mobile_puchase(self):
#         print(f"Thanks for purchasing {self.name} with {self.color} color !")
#
#     @classmethod                   #Can be accessed without the object by using a decorator "@classmethod above the class method. Can be accessed by using an object. Good in terms of memory management as there is no need to create an object
#     def verification(cls):
#         print("Charger is Available ? ",cls.charger)
#
#     @staticmethod
#     def addition(a,b):
#         print("Result : ",a+b)
#
# mobile.verification()  #class method accesed without using an object
# stephin = mobile("Samsung","Black")
# stephin.mobile_puchase()
# mobile.addition(10,10)  #Static method is accessed using class and even an object
# stephin.addition(10,2)
# stephin.verification()  # #class method accesed with using an object




# ****************************OOPS - PART 2 (ASSOCIATION AND INHERITANCE) **********************************
# INHERITANCE (SINGLE LEVEL, MULTI-LEVEL, MULTIPLE, HIEARCHIAL, HYBRID) - IS A RELATIONSHIP......... ASSOCIATION (COMPOSIITON AND AGGREGATION) - HAS A RELATIONSHIP
#
# COMPOSIITON - IS A "HAS A" RELATIONSHIP - STRONG ASSOCIATION
# IN COMPOSIITON ONE OF THE CLASSES IS COMPOSED OF ONE OR MORE INSTANCE OF OTHER CLASSES. IN OTHER WORDS, ONE CLASS IS CONTAINER AND ANOTHER CLASS IS CONTENT.AND IF YOU DLELETE THE CONTAINER OBJECT THEN ALL OF ITS CONTENTS OBJECTS ARE ALSO DELETED.
#
# AGGREGATION - IS A "HAS A" RELATIONSHIP - WEAK ASSOCIATON
# AGGREGATION IS A WEAK FORM OF COMPOSITION. IF YOU DELETE THE CONTAINER OBJECT, CONTENTS OBJECT CAN LIVE WITHOUT CONTAINER OBJECT.
#
# Code to illustrate COMPOSITION - strong association
#
# class snapdeal:
#
#     def __init__(self):
#         print("Welcome to Snapdeal !")
#
#     class men:
#         def __init__(self):
#             print("Welcome to Men's section.")
#
#         class footwear:
#             def __init__(self, name):
#                 self.name = name
#                 print("Welcome to Men's footwear section !")
#
#             def nike(self):
#                 print(f"Welcome to {self.name} men's footwear.")
#
#             def addidas(self):
#                 print(f"Welcome to {self.name} men's footwear.")
#
#         class clothing:
#             def __init__(self):
#                 print("Welcome to Men's clothing section !")
#
#             def jackjones(self):
#                 print("Welcome to J&J men's clothing.")
#
#             def denim(self):
#                 print("Welcome to Denim men's clothing.")
#
#         class WOmen:
#             def __init__(self):
#                 print("Welcome to Women's section.")
#
#             class footwear:
#                 def __init__(self):
#                     print("Welcome to Men's footwear section !")
#
#                 def nike(self):
#                     print("Welcome to Nike men's footwear.")
#
#                 def addidas(self):
#                     print("Welcome to Addidas men's footwear.")
#
#             class clothing:
#                 def __init__(self):
#                     print("Welcome to Men's clothing section !")
#
#                 def jackjones(self):
#                     print("Welcome to J&J men's clothing.")
#
#                 def denim(self):
#                     print("Welcome to Denim men's clothing.")
# shopping = snapdeal()
# a = snapdeal.men()
# b = snapdeal.men.footwear("Nike")
# b.nike()
# c = snapdeal.men.footwear("Addidas")
# c.addidas()
#
# Code to illustrate the AGGREGATION - WEAK Association - objects can survive even without the container objects
#
# class laptop:
#      def __init__(self, name, color, brand, inch):
#          self.name = name
#          self.color = color
#          self.brand = brand
#          self.inch = inch
#
#      def laptop_info(self):
#          print(f" Name : {self.name}\n Color : {self.color}\n Brand : {self.brand}\n Inch : {self.inch}")
#
# class employee:
#     def __init__(self, name, eno, lap_det):
#         self.name = name
#         self.eno = eno
#         self.lap_det = lap_det
#
#
#     def employee_info(self):
#         print(f"Name : {self.name}\n Employee No. : {self.eno}\n Laptop Details : ")
#         self.lap_det.laptop_info()
#
# a = laptop("HP","Black","Pavilion","15'")
# b = employee("Stephin",100,a)
# b.employee_info()


# class laptop :
#     def __init__(self, name, brand, color, inch):
#         self.name = name
#         self.brand = brand
#         self.color = color
#         self.inch = inch
#
#     def laptop_info(self):
#         print(f"Device Name : {self.name}\n Brand : {self.brand}\n Color : {self.color}\n Inch : {self.inch}")
#
# class employee:
#     def __init__(self, name, eno, lap_details):
#         self.name = name
#         self.eno = eno
#         self.lap_details = lap_details
#
#     def employee_info(self):
#         print(f"Name : {self.name}\n Employee No. : {self.eno}\n Laptop Details : ")
#         self.lap_details.laptop_info()
#
# laptop1 = laptop("HP","Pavilion","Black","15 inch")
# emp1 = employee("Stephin",101,laptop1)
# emp1.employee_info()


# class processor:
#     def __init__(self, name):
#         self.name = name
#     def processor_info(self):
#         print(f"Thanks for purchasing {self.name}!")
#
# class camera:
#     def __init__(self, name):
#         self.name = name
#     def camera_info(self):
#         print(f"Thanks for purchasing {self.name} !")
#
# class mobile_display:
#     def __init__(self, name):
#         self.name = name
#     def mobile_display_info(self):
#         print(f"Thanks for purchasing {self.name}!")
#
# class iphone:
#     def __init__(self):
#         self.processor = processor("Processor")
#         self.camera = camera("Camera")
#         self.mobile_display = mobile_display("Mobile Display")
#     def mobile_info(self):
#         print("Welcome to iPhone !")
#         self.processor.processor_info()
#         self.camera.camera_info()
#         self.mobile_display.mobile_display_info()
#
# getInfo = iphone()
# getInfo.mobile_info()



# class snapdeal:
#     def __init__(self):
#         print("Welcome to Snapdeal !")
#
#     class men:
#         def __init__(self):
#             print("Welcome to Men's section.")
#
#         class footwear:
#             def __init__(self, name):
#                 self.name = name
#                 print("Welcome to Men's footwear section.")
#
#             def reebok(self):
#                 print(f"Thanks for purchasing {self.name}!")
#
#             def nike(self):
#                 print(f"Thanks for purchasing {self.name} !")
#
#         class clothing:
#             def __init__(self, name):
#                 self.name = name
#                 print("Welcome to Men's clothing section.")
#
#             def jackjones(self):
#                 print(f"Thanks for purchasing {self.name} !")
#
#             def denim(self):
#                 print(f"Thanks for purchasing {self.name} !")
#
#     class women:
#
#         def __init__(self):
#             print("Welcome to Men's section.")
#
#         class footwear:
#             def __init__(self, name):
#                 self.name = name
#                 print("Welcome to Men's footwear section.")
#
#             def reebok(self):
#                 print(f"Thanks for purchasing {self.name} !")
#
#             def nike(self):
#                 print(f"Thanks for purchasing {self.name} !")
#
#         class clothing:
#             def __init__(self, name):
#                 self.name = name
#                 print("Welcome to Men's clothing section.")
#
#             def jackjones(self):
#                 print(f"Thanks for purchasing {self.name} !")
#
#             def denim(self):
#                 print(f"Thanks for purchasing  {self.name}!")
#
# stephin = snapdeal.men().footwear("Reebok")
# stephin.reebok()
# stephin = snapdeal.men().footwear("Nike")
# stephin.nike()
#
# class men:
#     def __init__(self):
#         print("Welcome to Men's section !")
#
#     class footwear:
#         def __init__(self, name, price, quantity):
#             self.name = name
#             self.price = price
#             self.quantity = quantity
#             print("Welcome to Men's footwear")
#         def reebok(self):
#             print(f"Name : {self.name}\n Price : {self.price}\n Quantity : {self.quantity} ")
#         def nike(self):
#             print(f"Name : {self.name}\n Price : {self.price}\n Quantity : {self.quantity} ")
#
#     class clothing:
#         def __init__(self, name, price, quantity):
#             self.name = name
#             self.price = price
#             self.quantity = quantity
#             print("Welcome to Men's Clothing")
#
#         def jackandjones(self):
#             print(f"Name : {self.name}\n Price : {self.price}\n Quantity : {self.quantity} ")
#         def handm(self):
#             print(f"Name : {self.name}\n Price : {self.price}\n Quantity : {self.quantity} ")
#
# class women:
#     def __init__(self):
#         print("Welcome to Women's section !")
#
#     class footwear:
#         def __init__(self, name, price, quantity):
#             self.name = name
#             self.price = price
#             self.quantity = quantity
#             print("Welcome to Women's footwear")
#         def reebok(self):
#             print(f"Name : {self.name}\n Price : {self.price}\n Quantity : {self.quantity} ")
#         def nike(self):
#             print(f"Name : {self.name}\n Price : {self.price}\n Quantity : {self.quantity} ")
#
#     class clothing:
#         def __init__(self, name, price, quantity):
#             self.name = name
#             self.price = price
#             self.quantity = quantity
#             print("Welcome to Women's Clothing")
#
#         def jackandjones(self):
#             print(f"Name : {self.name}\n Price : {self.price}\n Quantity : {self.quantity} ")
#         def handm(self):
#             print(f"Name : {self.name}\n Price : {self.price}\n Quantity : {self.quantity} ")
#
# class snapdeal:
#     def __init__(self):
#         self.men = men()
#         self.women = women()
#
#     def cust_detail_info(self):
#         nike = self.men.footwear("Nike", 3500, 2)
#         nike.nike()
#         reebok = self.men.footwear("Reebok", 2500, 5)
#         reebok.reebok()
#         jackandjones = self.men.clothing("Jack and Jones",1284,5)
#         jackandjones.jackandjones()
#         handm = self.men.clothing("H & M",1290,2)
#         handm.handm()
#         nike = self.women.footwear("Nike",2700,3)
#         nike.nike()
#         rebook = self.women.footwear("Reebok",2100,10)
#         rebook.reebok()
#         jackandjones = self.women.clothing("Jack and Jones", 1184, 1)
#         jackandjones.jackandjones()
#         handm = self.women.clothing("H & M", 1190, 3)
#         handm.handm()
#
# getInfo = snapdeal()
# getInfo.cust_detail_info()
#
#
# class camera:
#     def __init__(self, name):
#         self.name = name
#     def camera_info(self):
#         print(f"Thanks for purchasing {self.name}")
#
# class processor:
#     def __init__(self, name):
#         self.name = name
#     def processor_info(self):
#         print(f"Thanks for purchasing {self.name}")
#
# class mobile_display:
#     def __init__(self, name):
#         self.name = name
#     def mobile_display_info(self):
#         print(f"Thanks for purchasing {self.name}")
#
# class iphone:
#     def __init__(self):
#         self.camera = camera("Camera")
#         self.procesor = processor("Processor")
#         self.mobile_display = mobile_display("Mobile Display")
#
#     def iphone_info(self):
#         print("Welcome to iPhone !")
#         self.procesor.processor_info()
#         self.camera.camera_info()
#         self.mobile_display.mobile_display_info()
# getInfo = iphone()
# getInfo.iphone_info()
#
# INHERITENCE - IS A RELATIONSHIP
# When to use Association or Inheritence ?  For "Code Resuability" we will use Association (in case of laptop-employee example the laptop code can be used with any employees )whereas Inheritence is used for code Extensibility (we can extend the code - example - we can add extra features to the code, so basically by using a single function we will be reusing the code written in the parent classes - for example current version of android is 10 and extend the new code to create android 11).
# Code to illustrate the example of Single Inheritence
#
# class parent:
#     def house(self):
#         print("I am a Parent and I own a house !")
#
# class child(parent):
#     def car(self):
#         print("I am a Child and I own a car !")
# stephin = child()
# stephin.house()
# stephin.car()
#
# Code to illustrate the example of Multi-Level Inheritence
#
# class parent:
#     def house(self):
#         print("I am a Parent and I own a house !")
#
# class child(parent):
#     def car(self):
#         print("I am a Child and I own a car !")
#
# class  grand_child(child):
#     def supercar(self):
#         print("I am a Grand child and I own a Super Car !")
#
# stephin = grand_child()
# stephin.house()
# stephin.car()
# stephin.supercar()
#
# Code to illustrate the example of Hiearchial Inheritence
#
# class parent:
#     def house(self):
#         print("I am a Parent and I own a house !")
#
# class child1(parent):
#     def car(self):
#         print("I am a Child and I own a car !")
#
# class child2(parent):
#     def supercar(self):
#         print("I am a Child and I own a supercar !")
#
# stephin = child2()
# stephin.supercar()
#
# Code to illustrate multiple inheritence
#
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
# ***************** ENUMERATE() IN PYTHON ***************
# OFTEN, WHEN WE DEAL WITH ITERATORS WE ALSO NEED TO KEEP A CHECK ON ITERATIONS. PYTHON EASES THE PROGRAMMERS TASK BY PROVIDING A BUILT IN FUNCTION ENUMERATE() FOR THIS. ENUMERATE() ADD COUNTER TO A VARIABLE AND RETURNS AN ENUMERTOR OBJECT AS AN OUTPUT. THIS ENUMERATOR OBJECT CAN BE DIRECTLY USED AS AN OBJECT FOR LOOP OR CONERETED INTO A LIST TUPLE BY USING A LIST() METHOD.

# list1 = ["Red","Blue","Black","Green","Grey","Voilet"]
# list2 = ["Rose","Sunflower","Jasmine","Lotus","Mogra","Tulip"]
# list3 = "Rose"
# list4 = ["Rose"]
#
# a = enumerate(list1)
# b = enumerate(list2)
# print(type(a))
# print(list(enumerate(list1)))
# print(list(enumerate(list2,3)))
# print(list(enumerate(list3,3)))
# print(list(enumerate(list4,3)))

# list1 = ["Red","Blue","Black","Green","Grey","Voilet"]
# list2 = ["Rose","Sunflower","Jasmine","Lotus","Mogra","Tulip"]
# list3 = "Rose"
# list4 = ["Rose"]
# x = enumerate(list1)
# y = enumerate(list2)
# z = enumerate(list3)
# w = enumerate(list4)
# print(type(x))
# print(list(enumerate(list1)))
# print(list(enumerate(list2,1)))
# print(list(enumerate(list3)))
# print(list(enumerate(list4)))
#  ****************************** OOPS - Part 3 (ENCAPSULATION, ABSTRACTION, POLYMORPHISM)****************************************
# ENCAPSULAION - #PUBLIC (GENERALLY MEMBERS DECLARED IN A CLASS) ARE ACCESSIBLE FROM OUTSIDE THE CLASS
# PROTECTED - THE MEMBERS OF A CLASS THAT ARE DECLARED PROTECTED ARE ONLY ACCESSBILE WHICH ARE DERIVED FROM A BASE CLASS DIT. ADDING A SINGLE  UNDERSCORE "_" SYMBOL BEFORE THE DATA MEMBER.
# PRIVATE - THE MEMBERS OF A CLASS THAT ARE DECLARED PRIVATE ARE ACCESIBLE WITHIN THE CLASS ONLY
# PRIVATE ACCESS MODIFIER IS THE MOST SECURE MODIFIER. ADDING A DOUBLE UNDERSCORE '__' SYMBOL BEFORE THE DATA MEMBER.

# class employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self._age = age    #Protected variable --> "_"
#         self.__salary = salary  #Private variable --> "__"
#
#     #Getter method - to access the private variiables
#     def get_salary(self):
#         return self.__salary
#
#     #Setter method - to access the private variables
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
# print(stephin._age)   #To access private variables within the class
# print(stephin._employee__salary) #To access protected variables within the class


# class employee:
#     def __init__(self,name, age, salary):
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
#         print("I am a Private method !")
#
#     def get_verification(self):
#         return self.__verification()
#
#     def set_verification(self, updated_ver):
#         self.__verification = updated_ver
#
# stephin = employee("Stephin",25,45000)
# print("Salary :",stephin.get_salary())
# print("Updated Salary : ",stephin.get_salary())
# print("Verificattion Statement : ",stephin.get_verification())
#
# Abstraction - By default, Python does not provide abstract classes. Python comes with a module which provides the base for defining Abstract Base classes(ABC) and that module name is ABC. ABC works by decorating methods of the base class as abstract and then registering concrete classes as implementations of the abstract base. A method becomes abstract when decorated with the keyword @abstractmethod.

# from abc import ABC, abstractmethod
# class mobile_design:
#     @abstractmethod
#     def camera(self):
#         pass
#     @abstractmethod
#     def screen(self):
#         pass
#     def wireless_charging(self):
#         pass
#
# class test(mobile_design):
#     def camera(self):   #Concrete classes which is implementation of the abstract base
#         print("This is triple camera !")
#     def screen(self):
#         print("This is a screen with 144Hz refresh rate !")
#
# stephin = test()
# stephin.camera()
# stephin.screen()

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
#         return self.num1 - self.num2
#
# x = int(input("Enter Num1 : "))
# y = int(input("Emter Num2 : "))
# stephin = child(x,y)
# print(stephin.addition())

#POLYMORPHISM - The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types. (OPERATOR OVERLOADING)  :
# a=10
# b=20
# x='10'
# y='20'
# print(int.__add__(a,b))
# print(str.__add__(x,y))
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

# class expenses:
#     def __init__(self, exp):
#         self.exp = exp
#
#     def __add__(self, other):
#         print(self.exp + other.exp)
#
# f = expenses(1000)
# m = expenses(3000)
# f+m

# Code to illustrate Abstraction
# from abc import ABC, abstractmethod
# class mobile_design(ABC):
#     @abstractmethod
#     def camera(self):
#         pass                               #Parent class is used for declaration
#     @abstractmethod
#     def mobile_screen(self):
#         pass
#     def wireless_charger(self):
#         pass
#
# class testing(mobile_design):
#     def camera(self):
#         print("Thanks for purchasing Camera !")           #Child class is used for definition
#     def mobile_screen(self):
#         print("Thanks for purchasing Mobile Screen ! ")
#
# x = testing()
# x.camera()

# OPERATOR OVERLOADING
# class expense:
#     def __init__(self, num1):
#         self.number = num1
#
#     def __add__(self, add2):                      #Method Overloading
#         print(self.number + add2.number)
#
#     def __mul__(self, other):                     #Method Overloading
#         print(self.number * other.number)
#
# x = expense(1250)
# y = expense(1250)
# z = expense(1250)
# x + y          # "+" is calling __add__ method from the expense class
# x * y          # "*" is calling __mul__ method from the expense class

# Given below are the render methods :
# + __add__(self, other)
# - __sub__(self, other)
# * __mul__(self, other)
# /  __div__(self, other)
# // __floordiv__(self, other)
# %  __mod__(self, other)
# ** __pow__(self, other)
# += __iadd__(self, other)
# -=__isub__(self, other)
# *=__imul__(self, other)
# /=__idiv__(self, other)
# //=__ifloordic__(self, other)
# **=__ipow__(self, other)
# <__lt____(self, other)
# <=__le__(self, other)
# >__gt__(self, other)
#
# class expense:
#     def __init__(self, num):
#         self.number = num
#
#     def __mul__(self, other):            #method overloading
#         print(self.number * other.number)
#
#     def __add__(self, other):            #method overloading
#         print(self.number + other.number)
#
# x = expense(125)
# y = expense(125)
# x * y
# x + y
#
# DOUBT
# class expenses:
#     def __init__(self, value):
#         self.value = value
#
# def __add__(self, other):
#     print(int(self.value + other.value))
#
# def __str__(self):
#     return f"{self.value}"
#
# a1 = expenses(10)
# a2 = expenses(20)
# a3 = expenses(30)
# a1 + a2 + a3
#
# .format() - he format() method formats the specified value(s) and insert them inside the string's placeholder.
# txt = "My name is {fname}. I am {age}".format(fname = "Stephin", age = 25)
# txt1 = "My name is {0}. I am {1}".format("Stephin",25)
# txt2 = "My name is {}. I am {}".format("Stephin",25)
# print(txt)
# print(txt1)
# print(txt2)

# POLYMORPHISM : 1) OVERLOADING 2) OVER-RIDING <<---->> 1) OVERLOADING : 1) OPERATOR OVERLOADING 2) METHOD OVERLOADING 3) CONSTRUCTOR OVERLOADING <<----->> 2) OVERRIDING - METHOD OVERRIDING 2) CONSTRUCTOR OVERRIDING
#
# METHOD OVERLOADING : IF TWO METHODS ARE HAVING SAME NAME BUT DIFFERENT TYPE OF ARGUMENTS THEN THOSE METHODS ARE SAID TO BE OVERLOADED METHODS. BUT IN PYTHON METHOD OVERLOADING IS NOT POSSBILE. IF WE ARE TRYING TO DECLARE MULTIPLE METHODS WITH SAME NAME AND DIFFRENT NUMBER OF ARGUMENTS THEN PYTHON WILL ALWAYS CONSIDER LAST METHOD.
#
# class Test:
#
#     def __init__(self,a, b):
#         self.a = a
#         self.b = b
#
#     def method(self):
#         print("I am Method 1")
#
#     def method(self):
#         print("I am Method 2",self.a)
#
#     def method(self):
#         print("I am Method 3 !",self.a, self.b)
#
# test = Test(1,2)
# test.method()
#
# class Test:
#     def method(self):
#         print("I am Method 1")
#
#     def method(self,a):
#         print("I am Method 2",a)
#
#     def method(self,a,b):
#         print("I am Method 3 !",a, b)
# test = Test()
# test.method(1,2)
#
# Most of the times if method with variable number of arguments required then we can handle them with default arguments or variable number of argument methods
#
# class Test:
#     def addition(self, a,b,c,d):
#         if a!= None and b!= None and c!= None and d!= None:
#             print("Addition : ",a+b+c+d)
#         elif a!= None and b!= None and c!= None:
#             print("Addition : ",a+b+c)
#         elif a!= None and b!= None:
#             print("Addiiton : ",a+b)
#         else:
#             print("Give 2 or 3 or 4 arguments in Parameter")
#
# test = Test()
# test.addition(1,2,3,4)
#
# *args -  is a special non-keyword feature in python which elimiates the need to write multiple methods with different parameters. Hence, the method overloading isn't possible in Python. Incase if you write multiple methods with different parameters then it will execute the last method.
#
# class Test:
#     def addition(self, *args):
#         total = 0
#         for i in args:
#             total += i
#         print("Total : ",total)
#
# test = Test()
# test.addition(1,2,3,4,5)
# test.addition(1,2,3)
#
# CONSTRUCTOR OVERLOADING - ISN'T POSSIBLE IN PYTHON. IF WE TRY TO DEFINE MULTIPLE CONSTRUCTORS THEN THE LAST CONSTRUCTOR WILL BE CONSIDERED.
# BASED ON OUR REQUIREMENT WE CAN DECLARE CONSTRUCOR WITH DEFAULT ARGUMENTS OR VARIABLE NUMBER OF ARGUMENTS
#
# class Test:
#     def __init__(self):
#         print("I am constructor 1 ")
#
#     def __init__(self,a):
#         print("I am constructor 2 ")
#
#     def __init__(self,a,b):
#         print("I am constructor 3 ")
#
# test = Test(1,2)
#
# class Test:
#     def __init__(self, *num):
#         total = 0
#         for i in n    um:
#             total += i
#         print("Total :",total)
#
# test = Test(1,2,3)
# test = Test(1,2,3,4,5)
#
# ************************ OOPS PART - 4 (OVERRIDING) ******************************************
#
# METHOD OVERRIDING : WHATEVER MEMBER AVAILABLE IN THE PARENT CLASS ARE BY DEFAULT AVAIALABLE TO THE CHILD CLASS THROUGH INHERITENCE.
# IF THE CHILD CLASS NOT SATISFIED WITH PARENT CLASS IMPLEMENTATION THEN CHILD CLASS IS ALLOWED TO REDEFINE THAT METHOD IN THE CHILD CLASS  BASED ON ITS REQUIREMENT. THIS CONCEPT IS CALLED OVERRIDING.
# OVERRIDING IS APPLICABLE TO BOTH CONSTRUCTORS AND METHOD
#
# class parent:
#     def mobile(self):
#         print("I have Nokia 3310")
#
# class child(parent):
#     def mobile(self):
#         print("I have an iPhone")
#
# child = child()
# child.mobile()  #mobile() of child class is overriding mobile() of parent class. This is a classic example of Method Overriding
#
#
# class parent:
#     def mobile(self):
#         print("I have Nokia 3310")
#
# class child(parent):
#     def mobile(self):
#         super().mobile()     #Used to call the method implemented in the parent class
#         print("I have an iPhone")
#
# child = child()  #If child class doesn't contain constructor or method then parent class constructor/method will be executed. From child class constructor we can call parent class construcor by using the "super()" keyword.
# child.mobile()


# class company:
#     def __init__(self, company_name):
#         self.company_name = company_name
#
#     def display(self):
#         print(f"The name of company is {self.company_name}")
#
# class employee(company):
#     def __init__(self, company_name, emp_name):
#         super().__init__(company_name)
#         self.emp_name = emp_name
#
#     def display(self):
#         print("Company Name : ",self.company_name)
#         print("Employee Name : ",self.emp_name)
#
# x = employee("Tredence","Stephin")
# x.display()
#
# we have to use super() if the method of both child and parent class are same. If there is no naming conflict then use "self.mehtod_name()"
#
# class company:
#     def __init__(self, company_name):
#         self.company_name = company_name
#
#     def display(self):
#         print(f"Company Name : {self.company_name}")
#
# class employee(company):
#     def __init__(self, company_name, employee_name):
#         super().__init__(company_name)
#         self.employee_name = employee_name
#
#     def display(self):
#         print(f"Company Name : {self.company_name}")
#         print(f"Employee Name : {self.employee_name}")
#
# test = employee("Flipkart", "Stephin")
# test.display()
#
# WHEN TO USE SUPER : IF YOU HAVE SAME CONSTRUCTOR OR METHOD NAME IN BOTH PARENT AND CHILD CLASS THEN WE HAVE TO USE SUPER().  SUPER() IS USED IN BOTH ML AND DL MODEL
#
# MINOR APPLICATION TO ILLUSTRATE THE USE OF SUPER KEYWORD
#
# class car:
#     def __init__(self, name, model, wheels):
#         self.name = name
#         self.model = model
#         self.wheels = wheels
#
#     def display(self):
#         print(f"Brand Name : {self.name}\nModel : {self.model}\nWheels : {self.wheels}")
#
# class car_info(car):
#     def __init__(self, name, model, wheels, price, payment_type):
#         super().__init__(name, model, wheels)
#         self.price = price
#         self.payment_type = payment_type
#
#     def display(self):
#         super().display()
#         print(f"Price : {self.price}\nPayment Type : {self.payment_type}")
#
# test = car_info("Mercedes","C class",4,4500000,"Debit Card")
# test.display()
#
# class mobile:
#     def __init__(self, name, ram, color):
#         self.name = name
#         self.ram = ram
#         self.color = color
#
#     def display_info(self):
#         print(f"RECEIPT DETAILS : \nBrand Name : {self.name}\nRam : {self.ram}\nColor : {self.color}")
#
# list_of_mobile_sold = []
# while True:
#     name = input("Enter the mobile you want to purchase : ")
#     ram = int(input("Enter required RAM : "))
#     color  = input("Enter color : ")
#     m = mobile(name, ram, color)
#     list_of_mobile_sold.append(m)
#     print("Thanks for purchasing !")
#     opt = input("Want to purchase another mobile ? [Yes or No] : ")
#     if opt.lower() == 'no':
#         break
#
# for mobile in list_of_mobile_sold:
#     mobile.display_info()
#
#
# class mobile:
#     def __init__(self, name, ram, color):
#         self.name = name
#         self.ram = ram
#         self.color = color
#
#     def display(self):
#         print(f"RECEIPT : \nBrand Name : {self.name}\nRAM : {self.ram}\nColor : {self.color}")
#
# list_of_mobile_sold = []
# while True:
#     name = input("Enter the Mobile brand to purchase : ")
#     ram = int(input("Enter the required RAM : "))
#     color = input("Enter the required Color : ")
#     m = mobile(name, ram, color)
#     list_of_mobile_sold.append(m)
#     print(f"Thanks for purchasing {name} !")
#     opt = input("Do you want to make another purchase ? [yes/no] : ")
#     if opt.lower() == 'no':
#         break
#
# for mobile in list_of_mobile_sold:
#     mobile.display()

