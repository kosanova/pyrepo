#!/usr/bin/python

t = int(raw_input())

results = []

while(t > 0 and t < 100):
    t -= 1
    
    n = raw_input()
    n = int(n)
    
    nums = raw_input()
    table = map(int, nums.split(' '))

    results.append(sum(table))

for r in results:
    print r
    
