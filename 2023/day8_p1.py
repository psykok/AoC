#!/usr/bin/python

import re
f = open('day8_input.txt', 'r')
lines = f.readlines()

nav=lines[0]
nav=nav.strip()
navlen=len(nav)
print(navlen)

counter=0

mymap = {}
for line in lines[2:]:
  key, value=line.split('=')
  value=value.replace("(","")
  value=value.replace(")","")
  value=value.strip()
  
  mymap[key.strip()]=tuple(map(str, value.split(', ')))

niak='AAA'

pos=0
while niak != "ZZZ":
  cursor=mymap[niak]
  print(cursor)
  direction=nav[pos]
  print(direction)
  if direction == "L":
    niak=cursor[0]
  elif direction == "R":
    niak=cursor[1]
  counter+=1
  print("###",pos,navlen)
  if pos==(navlen-1):
    pos=0
  else:
    pos+=1


print(counter)

