#File IO Basics

"""
"r" - Open file for reading
"w" - Open file for writing
"x" - Creates file if not exist
"a" - Add more content to a file
"t" - text mode
"b" - binary mode
"+" - both read + write (used for updating)

#r and t are default mode

"""
#Open(), Read() and Readline()

# x= open("stephin", "r")  #rt - default mode and rb - read and binary mode
# contents = x.read(1000)
# print("1) ",contents)
# contents = x.read(1000)
# print("2) ",contents)
# x.close()

# x = open("stephin")
# # contents = x.read()                #read() can access all characters contained in the file
# # for i in contents:
# #     print(i, end ="")
# print(x.readline())                 #readline() can access all the characters contained in the line 1


# a = open("stephin")
# #contents = a.read()
# # for x in contents:
# #     print(x,end="")
# print(a.readline())

# x = open("stephin2.txt", "a")
# y = x.write("I love Data Science \n")
# print(y)
# x.close()

#Handles both read and write
# x = open("stephin2.txt", "r+")
# print(x.read())
# x.write("Thank You !!")
# x.close()

# x= open("stephin2.txt", "r+")
# print(x.read())
# x.write("Byeee \n")
# x.close()


# b = open("stephin", "r")
# contents = b.read()
# print(contents)
# b.close()

# x = open("stephin","r")
# contents = x.read()
# for i in contents:
#     print(i, end="")

# x = open("stephin","rt")
# contents1 = x.readline()
# print(len(contents1))
# x.close()


# f = open("stephin")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())

# f = open("stephin")
# f.seek(10)      #seek() helps to set the pointer at a specified index position
# print(f.tell())    #tell()  helps to find the current position (starting index) of the pointer
# print(f.readline())

#Code to illustrate the use of "with" block
# with open("stephin") as f:    #"with" block is used as an alternative to ease the process of opening and closing of file
#     x = f.readline()
#     print(x)
# a = open("stephin")
# y = a.read()
# print(y)
# a.close()

#Start from video 33

