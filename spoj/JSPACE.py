#!/usr/bin/python

lines = []

while True:
    line = raw_input()
    if line:
        if line.startswith(' '):
            line = line.title().replace(' ','')
        else:
            idx = line.find(' ')
            line = line[:idx] + line[idx:].title().replace(' ','')
        lines.append(line)
    else:
        break

result = '\n'.join(lines) # result is str
print result


