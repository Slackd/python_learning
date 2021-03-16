largest = None
print('Before: ', largest)
for itervar in [12, 40, 55, 65, 73, 18, 100]:
    if largest is None or itervar > largest:
        largest = itervar
    print('Loop:', itervar, largest)
print("Largest:", largest)


total = 0
for itervar in [3, 4, 5, 6, 7, 8, 100]:
    total += itervar
print("Total:", total)
