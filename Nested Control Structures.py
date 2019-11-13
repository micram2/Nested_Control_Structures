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

<<<<<<< HEAD
print('\n**************************\n')

'''
Programmer: Miles Cramer
Date: 10/23/19
Program: Average test score

This program asks for the test scores for multiple people
and reports the average test score for each portion
'''

num_people = int(input("How many people are taking the test: "))
test_per_person = int(input('How many tests are going to be averaged: '))

for i in range(num_people):
    name = input("Enter name: ")
    sum = 0
    for j in range(test_per_person):
        score = int(input("  Enter a score: "))
        sum = sum + score
    average = float(sum) / test_per_person
    print("    Average for " + name + ": " + str(round(average, 2)))
=======
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
>>>>>>> Forloop+WhileLoop
