#Program to built a faulty calculator

operator = input("Enter operator : ")
num1 = input("Enter Num1 : ")
num2 = input("Enter Num2 : ")
expression = num1+operator+num2
reverse = num2+operator+num1
faultyCalc = {"45*3":"555","56+9":"77","56/6":"4"}
if expression in faultyCalc:               #condition to print the expression
    print(faultyCalc[expression])
elif reverse in faultyCalc:                 #condition to print the expression in reverse order
    print(faultyCalc[reverse])
else:
    print(eval(num1+operator+num2))        #condition to print the un-restricted expressions





