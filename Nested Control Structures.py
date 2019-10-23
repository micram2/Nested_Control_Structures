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