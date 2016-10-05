#!/usr/bin/python

t = raw_input()
t = int(t)

i = 0

while(t > 0 and t < 100 and i < t):
    i += 1
    n = raw_input()
    n = int(n)
    for num in range(1,n+1):
        nums = raw_input()
        table = nums.split(' ')
        print table
