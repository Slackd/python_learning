#! /usr/bin/env python3

import itertools

# main
aoclist = open("input.txt")

#tests
numlist = [
    1721,
    979,
    366,
    299,
    675,
    1456
]

# part 1
for (a,b) in itertools.combinations([int(n) for n in aoclist], 2): 
        if a+b == 2020: 
            print(a*b)

# part 2
for (a,b,c) in itertools.combinations([int(n) for n in aoclist], 3): 
        if a+b+c == 2020: 
            print(a*b*c)

