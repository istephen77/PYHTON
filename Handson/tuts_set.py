"""x = set()
print(x)"""

x = [1,2,3,4,5]
set_from_list = set(x)
print(type(set_from_list))
print(set_from_list)
set_from_list.add(1)
set_from_list.add(1)
set_from_list.add(22)
print((set_from_list))  #set() maintains unique value

