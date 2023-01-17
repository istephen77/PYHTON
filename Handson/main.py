# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import  pandas as pd

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    List = [1,2,3,4,5]
    List[2]=69
    print(List[1:5])
    set = {8,3,5,2,3,5,67,1}
    set.add(69)
    print(set)

    dict1 = {'name':['stephin','stefani','stefi'], 'age':[26,18,20], 'salary':[66000,45000,45000]}
    data = pd.DataFrame(dict1)
    print(data)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
