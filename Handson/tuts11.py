"""d1 = {"name":"stephin","age":"23","salary":"55000","location":"oslo","nationality":"indian"}
d2=d1.copy()
del d2["nationality"]
print(d2)
print(d1)

d1 = {"name":"stephin","age":"23","salary":"55000","location":"oslo","nationality":"indian"}
d2 = 2

thisdict = dict.fromkeys(d1,d2)
print(thisdict)


print("Welcome to DICTIOANRY !!")
dict1 = {"abase":" cause to feel shame", "benefit":"advantage", "callow":"young and inexperienced", "dally":"waste time", "endear":"make attractive"}
word = input("Enter word : ")
print(dict1[word])

print("Example of get()")
dict1 = {"abase":" cause to feel shame", "benefit":"advantage", "callow":"young and inexperienced", "dally":"waste time", "endear":"make attractive"}
x = dict1.get("callow")
print(x)


print("Example of fromkeys()")
x = "abase", "benefit", "callow", "dally"
y = 5
thisdict = dict.fromkeys(x,y)
print(thisdict)

#difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.



dict1 = {"Abase":" cause to feel shame", "Benefit":"advantage", "Callow":"young and inexperienced", "Dally":"waste time", "Endear":"make attractive"}
word = input("Enter word : ")
x = word.capitalize()
if x in dict1:
    print(x,"=",dict1[x])
else:
    print("Invalid Entry !")

dict1 = {"Abase":" cause to feel shame", "Benefit":"advantage", "Callow":"young and inexperienced", "Dally":"waste time", "Endear":"make attractive"}
word = input("Enter the word :")
x = word.capitalize()
if x in dict1:
    print(x,"=",dict1[x])
else:
    print("Invalid Emtry !!")"""

age = int(input("Enter age :"))
if age<=1 or age>=100:
    print("Enter VALID AGE !!")
elif age>18:
    print("Eligible to vote !")
elif age==18:
    print("Eligible to vote after shoiwng upto authorities")
else:
    print("Not eligible to vote!")