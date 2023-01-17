# try:
#     num1 = int(input("Num 1: "))
#     num2 = int(input("Num 2: "))
#     print("Result: ", num1+num2)
#
# except Exception as e:
#     print(e)



try:
    age = int(input("Enter Age: "))
    if(age>18): print("Eligible to vote !")
    elif (age<18): print("Not eligible to vote !")
    else: print("Need to visit physically with AAdhar card !")
except Exception as e:
    print(e)