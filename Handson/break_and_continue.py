i=0
while(True):
    if i<10:
        i+=1
        continue
    print(i, end=" ")
    if i==50:
        break
    i+=1

i = 0
while(True):
    if i+1<5:
        i=i+1
        continue
    print(i+1,end = " ")
    if(i==44):
        break
    i = i+ 1



# while(True):
#     x = int(input("Emter number: "))
#     if(x>100):
#         print("Congrats you've printed a number greater than 100 !")
#         break
#     else:
#         continue


sum=0
count=0;
while True:
  n = input("Enter Number ")
  n = int (n)
  if n==-1:
    break
  else:
    count += 1
    sum += n
print ("sum using while loop ", sum)
average = sum / count
print("Average using a while loop ", average)

for i in "welcome":
    if i=="o":
        break
    print(i)

i=0
while(True):
    if i<10:
        i+=1
        continue
    print(i, end=" ")

    if i ==100:
        break
    i+=1