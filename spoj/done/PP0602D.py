#!/usr/bin/python

s = raw_input()

lines = s.split()

n = int(lines[0])
k = int(lines[1]) # o tyle przesuniecie

if k > 1 and n > k and n < 10000:
    nums = raw_input()
    nums_l = nums.split()
    
    for i in range(1,k+1):
        nums_l += [nums_l.pop(0)]

    print ' '.join(nums_l)

