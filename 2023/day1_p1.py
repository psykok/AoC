#!/usr/bin/python

import re
f = open('input.txt', 'r')
lines = f.readlines()

total=0
for line in lines:
  numbers = re.findall(r'\d+', line)
  res=''.join(numbers)

  if len(res) == 1:
    out=res+res
  else:
    out=res[0]+res[-1]
  total=total + int(out)
print(total)
