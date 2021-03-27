#! /usr/bin/python3

# Write another program that prompts for a list of 
# numbers as above and at the end prints out both the maximum 
# and minimum of the numbers instead of the average.

userNums = input("Enter Numbers Separated by spaces: ")
inputNums = userNums.split()

for i in range(len(inputNums)):
    inputNums[i] = int(inputNums[i])

largest = None
smallest = None

for itervar in inputNums:
    if largest is None or itervar > largest :
        largest = itervar
print("Largest:", largest)

for itervar in inputNums:
    if smallest is None or itervar < smallest :
        smallest = itervar
print("Smallest:", smallest)

print("Sum:", sum(inputNums))
