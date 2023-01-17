# def sqnum(x):
#   return x * x
# num1 = [4, 5, 2, 9]
# print("Original List: ",num1)
# result = map(sqnum, num1)
# print("Squares :")
# print(list(result))


# def function2(a , b):
#   average = (a+b)/2
#   print(average)
# function2(3,7)               #Simple illustration of a user defined function !
#
# def func1():
#   print("Function 1")
# func1()
#
# def average(a,b):
#   """This is a function which calculates average of two numbers !"""
#   x = (a+b)/2
#   print("1",x)
#   return x              #For returning a value, the return keyword along with the variable is returned !
# x = average(3,7)           #If we store the function value in a variable and if a return statenent isn't defined then it will return "none" in the o/p
# print("2)",x)
#
# print(average.__doc__)       #Doc_String to know the purpose for which the function was written !


# def average(a,b,c):
#   """This is a function to calculate the average of three numbers !"""
#   x = (a+b+c)/3
#   print("1 )",x)
#   return x
# x = average(3,3,3)
# print("2) ",x)
# print(average.__doc__)

# def average(a,b):
#   average = (a+b)/2
#   print("Average : ",average)
# average(3,7)


# def greet():
#   print("Hello !")
#
# greet()
#
# def greet(first_name, last_name):              #Parameters are input that we give to the function
#   print(f"Hello, {first_name} {last_name} !!")
#
# greet("Stephin", "Sebastian")           #Arguments are actual values of the parameter

# def greet(first_name, last_name):
#   print(f"Hello, {first_name} {last_name}")
#
# greet("Stephin", "Sebastian")

#Type of function : 1) Which performs a task ..... 2) Return a value
#Example of Type 1
# def greet(first_name, last_name):
#   print(f"Hello, {first_name} {last_name}")
#
# print(greet("Stephin", "Sebastian"))  #It will give "None" as output because none is the retur value of the function

#Example of Type 2
# def get_greeting(first_name, last_name):
#   return f"Hello, {first_name} {last_name} !"
#
# message = get_greeting("Peddler", "Pushpa")
# file = open("write.txt","w")
# file.write(message)
# file.close()

#Keyword Arguments
# def incr(num, by=3):  #optional parameter should come before the required parameter
#   return num+by
# print(incr(2))  #Here by=2 acts as a keyword argument   #If we don't pass any value in the argumennt then it will take default value as parameter but if we pass the argument then it will ignore the default value and give priority to the argument passed in the parameter

#Defualt arguments


#  *args, wait, what ?
#Code to illustrate the example of *args
# def multiply(*numbers):    # In *args the python packages the arguments in the form of tuple pair
#   total=1
#   for n in numbers:
#     total*=n
#   return total
#
# print(multiply(2,3,4,5))


#Code to illustrate the example of **args
# def save_user(**user):     # In **args the python packages the arguments in the form of dictinary (key:value) pair
#   print("ID: ",user["id"])
#   print("Name: ", user["name"])
#   print("Age: ", user["age"])
#
# save_user(id=10, name="Stephen", age=25)

# def save_user(**user):
#   print("ID: ",user["id"])
#   print("Name: ", user["name"])
#   print("City: ", user["city"])
#
# save_user(id=101, name="Sammy", city="Mumbai")

#Code to illustrate the use of scope by using local and global variables. "Scope" refers to the region of the code where the variable is defined

#Interpreter alllocates the memory for the local variable which is defined in the function but later releases the memory when it finds that the local variable is not used or assigned in any other part of the function]
#In case of the global variable, it can be accessed in any function within that particular file
#Global keyword is used to access the local variable inside the function as globally but the global keyword is not realy recommended to use
#
# message = "A"

# def greet(name):
#   message = "B"
#   print("1)",message)
#
# def get_greet(name):
#   message = "C"
#   print("2) ",message)
#
# greet("Stephin")
# print("3) ",message)

# message = "X"
# def greet(name):
#   global message
#   message = "W"
#   print("1) ",message)
#
# greet("Stephin")
# print(message)

#Global keyword is used inside a function and if it is accessed outside that function then the output will be the global keyword itself even if another global keyword is defined above all the other functions


# message = "X"
# def greet(name):
#   message = "W"
#   print("1) ",message)  #In this case first the interpreter interprets and prints the local variable and later it prints the global variable
#
# greet("Stephin")
# print(message)

# def fizz_buzz(input):
#   if input%3==0 and input%5==0:
#     result1 = "FizzBuzz"
#     print(result1)
#   elif input%3 == 0:
#     result2 = "Fizz"
#     print(result2)
#   elif input%5 ==0:
#     result3 = "Buzz"
#     print(result3)
#   else:
#     result4 = input
#     print(result4)
#
# fizz_buzz(7)

# def fizz_buzz(input):
#   if (input%3==0) and (input%5==0):
#     return "Fizz Buzz"
#   if input%3==0:
#     return "Fizz"
#   if input%5==0:
#     return  "Buzz"
#   return input
# print(fizz_buzz(97))

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


# def average(a,b,c):
#   average1 = (a+b+c)/3
#   return  average1
#
# num1 = int(input("Enter number 1 : "))
# num2 = int(input("Enter number 2 : "))
# num3 = int(input("Enter number 3 : "))
#
# print("Result : ", average(num1,num2,num3))








