#!/usr/bin/python

t = int(raw_input())

nums = []

while t > 0 and t <=100:
    t -= 1
    nums.append(raw_input())

for num in nums:
    num = num.split()
    
    if int(num[0]) <= 100:
        del num[0]
        num.reverse()
        print ' '.join(num)
