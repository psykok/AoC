#!/usr/bin/python

import re
from num2words import num2words

mydic = {
  'oneight':18,
  'twone':21,
  'threeight':38,
  'fiveight':58,
  'sevenine':79,
  'eightwo':82,
  'eighthree':83,
  'nineight':98
}

f = open('input.txt', 'r')
lines = f.readlines()

total=0
for line in lines:
  print(line)
  for key, value in mydic.items():
    line = line.replace(key, str(value))
  for i in range(1,10):
    line = line.replace(num2words(i), str(i))
  print(line)

  numbers = re.findall(r'\d+', line)
  res=''.join(numbers)
  print("\n###"+res)
  if len(res) == 1:
    out=res+res
  else:
    out=res[0]+res[-1]
  print("###"+out)
  total=total + int(out)
print(total)
