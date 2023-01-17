"""operators in python

Arithmetic operator
Assignment operator
Comparsion operator
Logical operator
Indentity operator
Membership operator
Bitwise operator"""

#Arithmetic operators
#print("5 + 6 is ",5+6)
#print("5 - 6 is ",5-6)
#print("5 * 6 is ",5*6)
#print("5 / 6 is ",5/6)        #division which gives the exact divided value of the division
#print("12 // 5 is ",12//5)   #double floor diivsion - rounds up values to nearest integers

#Assigment operators
#x=6
#print(x)
#x+=10 #shorthand operators
#print(x)
#y=20
#print(y%2)   #modulus gives the remainder as the result


#Comparison operators
#i = 50
#if i==50:
  #  print(i==50)

#Logical operator
x = True
y = False
print(x and y)
print(x or y)
print(not(x or y))

#Indentity operator

x = True
y = False
print(x is y)
print(x is not y)

#Membership operators
x = [1,2,3,4,5]
y = [1,4,3,6,7,8]
print("membership",x in y)
print(x not in y)

#Bitwise operators

#And, or, xor, not, left shift, right shift

x = 1
y = 3
print(x &y)
print(x | y)
print(x^y)
print(~x and ~y)
print(x>>2)
print(x<<2)





