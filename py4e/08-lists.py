#! /usr/bin/env python3

fileName = input("Enter Filename to Open: ")

try:
    fileHandle = open(fileName)
except:
    print('File Does not Exist:', fileName)
    exit()


wList = list()

for line in fileHandle:
    word = line.split()
    for element in word:
        if element not in wList:
            wList.append(element)

print(sorted(wList))


