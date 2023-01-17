#dir()  - dir() is a powerful inbuilt function in Python3, which returns list of the attributes and methods of any object (say functions , modules, strings, lists, dictionaries etc.)
"""
dir() tries to return a valid list of attributes of the object it is called upon. Also, dir() function behaves rather differently with different type of objects, as it aims to produce the most relevant one, rather than the complete information.

For Class Objects, it returns a list of names of all the valid attributes and base attributes as well.

For Modules/Library objects, it tries to return a list of names of all the attributes, contained in that module.

If no parameters are passed it returns a list of names in the current local scope.

Applications :

The dir() has it’s own set of uses. It is usually used for debugging purposes in simple day to day programs, and even in large projects taken up by a team of developers. The capability of dir() to list out all the attributes of the parameter passed, is really useful when handling a lot of classes and functions, separately.

The dir() function can also list out all the available attributes for a module/list/dictionary. So, it also gives us information on the operations we can perform with the available list or module, which can be very useful when having little to no information about the module. It also helps to know new modules faster.

"""

# Without importing external libraries

# print(dir())
# import random
# import math
# print(dir())

# With importing external libraries

# import random
# print(dir(random))

# Object is passed as parameters

# geeks = ["geeksforgeeks", "gfg", "Computer Science", "Data Structures", "Algorithms"]
# d = {}
# print("1) ",dir(geeks))
# print("2) ",dir(d))

# User Defined – Class Object with an available __dir()__ method is passed as parameter.

# class parent:
#     def __dir__(self):
#         return ["geeksforgeeks", "gfg", "Computer Science", "Data Structures", "Algorithms"]
#
# test = parent()
# print(dir(test))

# class parent:
#     def __dir__(self):
#         return ["geeksforgeeks", "gfg", "Computer Science", "Data Structures", "Algorithms"]
# test = parent()
# print(dir(test))
