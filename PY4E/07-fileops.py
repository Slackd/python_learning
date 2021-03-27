#! /usr/bin/python3


fileName = input("Enter Filename to Open: ")

try:
    fileHandle = open(fileName)
except:
    print('File Does not Exist:', fileName)
    exit()

spamFilter = []

for lines in fileHandle:
    if lines.strip().startswith('X-DSPAM-Confidence'):
        fltNums = float(lines.split(":")[1].strip())
        spamFilter.append(fltNums)

avergeConfidence = sum(spamFilter) / len(spamFilter)

print("Average spam confidence:", avergeConfidence)
        

        
 
