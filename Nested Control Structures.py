'''
Programmer: Miles Cramer
Date: 10/18/2019
Program: Double for loop

This program will nest a for loop inside of another
For loop
'''

for i in range(3):
    print('Outer_for_Loop: ' + str(i))
    for l in range(2):
        print("     inner for loop: " + str(l))

'''
Programmer: Miles
Date: 10/24/19
Program: For loop + While loop

This program will create a for loop with a while loop embedded into it'''

for i in range(4):
    print("Outer for loop: " + str(i))
    x = 6
    while x >= 0:
        print("    While loop: + str(x))
        x = x - 1
