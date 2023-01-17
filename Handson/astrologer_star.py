# one= int(input('Enter the number of prints you want: '))
# print("Type 1 Or 0 ")
# two = int(input())
# new =bool(two)
#
#
# if new == True:
#     for i in range(1, one+1):
#         for j in range(1, i + 1):
#             print('*', end = '')
#         print()
# elif new == False:
#     for i in range(one,1,- 1):
#         for j in range(1, i + 1):
#             print('*', end= '')
#         print()

#Code tp print the astrologer's star
num1 = int(input("Enter the number of starts to be printed : "))
new = int(input("Type 1 or 0 : "))
bool1 = bool(new)
if bool1 == True:
    for i in range(1, num1+1):
        for j in range(1,i+1):
            print("*",end="")
        print()
else:
    for i in range(num1+1,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()