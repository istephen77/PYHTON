#List and Tuple

# list1 = [1,2,3,4,5,6,7,8,9]
# print(list1)
#
# list2 = list((1,2,3))
# print(list2)

# Can store data of different data-type
# List are ordered
# You can access the elements of the list by using the index
# List can be nested
# List are mutable
# Lists are Dynamic

# tuple1 = tuple((1,2,3))
# print(tuple1)

# # To create a Tuple of single element use a comma
# tuple3 = (2,)
# print(type(tuple3))

# Tuples are comma seperated elements enclosed within the parathensis
# The values seperated by the commas are called tuples
# Tuples are immutable
# You can access the elements of the tuple by using the index
# Tuple can be nested because tuples are ordered

# Tuple is faster than list and as the tuple is immutable, the data stored inside the tuple cannot be modified

#Set and Dictionary

# Dictionary is defined using key:value pairs, seperated by comma and ecclosed by curly braces. The key:value pair are seperated by colons.
# Keys will be unique and only immutable object as key
# Values can be both mutable and immutable
# Dictionary is un-ordered
# Dictinaries are mutable

# d= {}
# print(d)

# d = {"stephin", "stephin.sebastian96@gmail.com"}
# print(d)

# d = dict()
# print(type(d))

# dictionary = {"j":1,"k":2,"j":3}
# print(dictionary)

# tuple1 = (2,3)
# dict = {tuple1:"stephin"}
# print(dict)

# Set is the collection of unique elements. No items can be repeated
# Set is un-ordered. Like dictionary
# Set is mutable
# Set can contain only immmutable type of elements, so set cannot be nested
# Set is un-ordered so we cannot access the value by using the index


# s1 = set()
# print(type(s1))
#
# s1 = set("Hello")
# print(s1)
#
# s3 = {1,2,3,4,3,3,3,4,4,4,4,4,5,5,5}
# print(set(s3))

# --4 : User-Defined Data Structure

# Stack is an ordered collection of items where the addition of new items and removal of items always takes place at the same end.
# One of the end is top and the opposite end to it is called as Base


# Stacks stores the items in LIFO (Last In First Out) or FILO (First In Last Out) manner

#Example : Bunch of plates that are placed inside a kitchen

# Operations performed by the stack : Push, Pop, Peek or Top, isEmpty

# Push : Adds the elements to the Stack
# Pop : Removes the elements to the Stack'
# Peek or Top : returns the element at the top
# isEmpty : returns whether stack is empty or not

# print("""Hello everyone, i'm Stephen and welcome to my youtube channel.
# Today we are discussing about Python programming tutorials.
# In that we are discussing about Matplotlib.""")

# Stack is used to reverse a string and it is used in expression evaluation and expression conversion -
# in-fix to post-fix, in-fix to pre-fix, post-fix to in-fix, pre-fix to in-fix
# Used for forward and backward feature in web browsers
# Used in Tower of Hanoi algorithm

# --5 : Implementing stacks using List : Two ways - by list and by other modules

# 1) Implement stacks using Lists : push : append, pop : pop

# stack = []
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack)
# stack.pop()
# stack.pop()
# stack.pop()
# print(stack)
# LIFO = Last in first out operation is performed

# To check whether the list is empty or not
# stack = []
# print(len(stack) == 0)
# print(not stack)
# Means list is empty

# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack[-1])

# Implementation of stack by using List

# stack = []
# def push():
#     if len(stack) == n:
#         print("Stack limit exceeded out of memory")
#     else:
#         element = int(input("Enter the element : "))
#         stack.append(element)
#         print(stack)
#
# def pop_operation():
#     if not stack:
#         print("Stack is empty !")
#     else:
#         e = stack.pop()
#         print("Element Removed : ", e)
#         print(stack)
#
# n = int(input("Enter the stack limit : "))
#
# while True:
#     choose = int(input("Choose : 1) Push. 2) Pop. 3) Quit : "))
#     if choose == 1:
#         push()
#     elif choose ==2:
#         pop_operation()
#     elif choose ==3:
#         break
#     else:
#         print("Enter a valid input from the option !!")


# --6 : Implementation of stack by using Modules

# 1) By using collections module using class caled deqeue (double ended queue). Here we can add the element from both the side
# There are different methods to add the element from both the sides
# Push : append Pop: pop

# import collections
# stack = collections.deque()
# print(stack)
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack)
# stack.pop()
# stack.pop()
# stack.pop()
# print(stack)
# print(not stack)

# import collections
# stack = collections.deque()
# def push():
#     if len(stack) == n:
#         print("Stack limit exceeded out of memory !")
#     else:
#         elements = int(input("Enter the elements : "))
#         stack.append(elements)
#         print(stack)
#
# def pop_operation():
#     if not stack:
#         print("Stack is empty !")
#     else:
#         e = stack.pop()
#         print("Removed Element : ", e)
#         print(stack)
#
# n = int(input("Enter the stack limit : "))
# while True:
#     choose = int(input("1) Push 2) Pop 3) Quit : "))
#     if choose == 1:
#         push()
#     elif choose == 2:
#         pop_operation()
#     elif choose == 3:
#         break
#     else:
#         print("Enter valid input from the option")


# 2) Using the Queue module we can create the stack. There is a class called LifoQueue. For push : put, pop : get

# import queue
# stack = queue.LifoQueue(3)
# stack.put(11)
# stack.put(12)
# stack.put(13)
# stack.put(14, timeout=1)
# stack.get()
# stack.get()
# stack.get()
# stack.get(timeout=1)
# print(stack)

# --7: Introduction to Queue

# Queue is a linear Data Structure where the element is inserted from one side and removed from the another side
# Queue is open at both the end as elements are added and removed from both the ends
# The end where elements are added is called the back/rear/tail - Process of adding an element is called "enqueue"
# The end where elements are removed is called the front/end - Process of removing an element is called "dequeue"
# Queue follows FIFO (First In First Out) or LILO (Last In Last Out) method
# Ex : Standing in a queue to buy tickets or grocery
# Used to implement the loosely coupled architecture. Ex: Price from NYSE stock exachange is produced and it's consumed by google/yahoo finance etc.

# Operation of Queue :
# enqueue (adding element),
# dequeue(removing element)
# isFull (to check whether the queue is full or not)
# isEmpty (to check whether the queue is empty or not)

# Queues are used whenever we want to process items that comes one at a time as they come in
#Ex : Uploading a photo, printing documents, call-center phone systems uses queue.

# --8: Queue implementation using List Data Structure
# enqueue : append
# dequeue : pop - In pop() mention the index while removing the element

# Insert from Back/rear/tail and removing the element from Front/end
# queue = []
# queue.append(11)
# queue.append(12)
# queue.append(13)
# print(queue)
# queue.pop(0)
# print(queue)

# Insert from Front/end and removing the element from Back/rear/tail

# queue = []
# queue.insert(0,10)
# queue.insert(0,20)
# queue.insert(0,30)
# print(queue)
# queue.pop()
# print(queue)

# To check whether the queue is empty or mot
# queue = []
# print(not queue)

# To check elements present in the front and rear side

# queue = []
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print(queue)
# print(queue[-1])  #Back/Rear/Tail
# print(queue[0])   #Front/End

# Insertion from back and deletion from front

# queue = []
# def enqueue():
#     if len(queue) == queue_limit:
#         print("Limit exceeded, Queue memory is full !! ")
#     else:
#         element = int(input("Enter the element : "))
#         queue.append(element)
#         print(queue)
#
# def dequeue():
#     if not queue:
#         print("Queue is empty")
#     else:
#         removed_element = queue.pop(0)
#         print("Removed Element : ", removed_element)
#         print(queue)
#
# queue_limit = int(input("Enter the Queue limit : "))
# while True:
#     choose = int(input("1) Enqueue 2) Dequeue 3) Quit : "))
#     if choose == 1:
#         enqueue()
#     elif choose == 2:
#         dequeue()
#     elif choose == 3:
#         break
#     else:
#         print("Enter a valid input")


# Insertion from front and deletion from back

# queue = []
# def enqueue():
#     if len(queue) == queue_limit:
#         print("Limit exceeded, Queue memory is full !!")
#     else:
#         element = int(input("Enter the element : "))
#         queue.insert(0,element)
#         print(queue)
#
# def dequeue():
#     if not queue:
#         print("Queue is empty")
#     else:
#         removed_element = queue.pop()
#         print("Removed Element : ", removed_element)
#         print(queue)
#
# queue_limit = int(input("Enter the queue limit : "))
# while True:
#     choose = int(input("1) Enqueue 2) Dequeue 3) Quit : "))
#     if choose == 1:
#         enqueue()
#     elif choose == 2:
#         dequeue()
#     elif choose == 3:
#         break
#     else:
#         print("Choose valid option ")

# --9: Queue implementation using Classes
# 1) dequeue class from collection modules. It provides us with methods to enter the data from both the ends
# append() to insert the element from right side and pop() to remove the element from right side
# appendleft() to insert the element from left side and popleft() to remove the element from left side

# import collections
# queue = collections.deque()
# queue.appendleft(10)
# queue.appendleft(20)
# queue.appendleft(30)
# print(queue)
# queue.pop()
# print(queue)


# queue = collections.deque()
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print(queue)
# queue.popleft()
# print(queue)
# queue.popleft()
# print(queue)

# queue = collections.deque()
# def enqueue_operation():
#     if len(queue) == queue_limit:
#         print("Memory exeeded the queue limit")
#     else:
#         elements = int(input("Enter the elements : "))
#         queue.appendleft(elements)
#         print(queue)
# def dequeue_operation():
#     if not queue:
#         print("Qeueue is emoty")
#     else:
#         removed_element = queue.pop()
#         print("Removed Element : ", removed_element)
#         print(queue)
#
# queue_limit = int(input("Enter the queue limit : "))
# while True:
#     choose = int(input("1) Enqueue 2) Dequeue 3) Quit : "))
#     if choose == 1:
#         enqueue_operation()
#     elif choose == 2:
#         dequeue_operation()
#     elif choose ==3:
#         break
#     else:
#         print("Choose the valid options")


# module : queue, class queue
# Queue module contains different classes like Queue, LifoQueue, PriorityQueue
# To get size of the Queue - use qsize()
# To check whether the Queue is empty or not - use queue.Empty()
# To check whether the Queue is full or not - use queue.Full()
# To insert an item in the Queue - use Put(item, block = True, timeout)
# It will put an item into the Queue and if block is True and timeout is none then it will block untill the free-slot is available
# It will put an item into the Queue and if block is False and timeout is none then....
# It will not give the Queue is full message instead of that it will wait till the free-slot is available
# put_nowait(item) is similar to put(item, block = False, timeout = 2)
# To get an element : 1) get() 2) get_nowait()
# get(items, block = True, timeout = None)
# get_nowait() or get(items, block = False, timeout = 2)

# import queue
# q = queue.Queue()
# q.put(10)
# q.put(20)
# q.put(30)
# print(q)
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get(block=False, timeout=2))

# --10: Priority Queue Data Structure :  2 ways to implement : 1) seeting priority accordinf to value of elements 2) Priority Queue module in Queue class

# Priority Queue is the modified version of thw queues in which each element is associated with the priority and it's served
# according to its priority

# The best method to implement the Priority Queue is by using the binary heap. In the priority queue class, the entries are sorted by using the heap queue module.
# It will use the binary data structure and the lowest entry value will be retrieved first.
# Priority Queue class will take the lowest value as highest priority and it will remove it first.

# Added



