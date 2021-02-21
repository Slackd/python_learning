fhand = open('mbox.txt')

count = 0
for lines in fhand:
    trimLines = lines.strip()
    if trimLines.startswith('X-DSPAM-Confidence:'):
        print(trimLines)
    #count += 1
#print('Line Count:', count)

