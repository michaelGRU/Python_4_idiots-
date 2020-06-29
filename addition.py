#add numbers
import numpy as np
count = 0
sum = 0
isfloat = True
isflaot2= True
plz = "Please enter a number!"
while isfloat:
    many = input("How many numbers do you want to enter? : ")
    try:
        many = float(many)
        isfloat = False
    except ValueError:
        print(plz)
while count < many:
    in_num = input("Enter num {} : ".format(count+1))
    try:
        in_num = float(in_num)
        sum = np.add(sum,in_num)
        count += 1
    except ValueError:
        print(plz)
print("\nYour result is {}.".format(sum))
