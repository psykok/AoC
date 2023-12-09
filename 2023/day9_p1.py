#!/usr/bin/python

import numpy as np
from itertools import groupby


f = open('day9_input.txt', 'r')
lines = f.readlines()
x = {}
pos = 0
total=[]
start=0

for line in lines:
  line=line.strip()
  x[pos]=list(map(int, line.split()))
  print(line)
  print(x[pos])
  res = np.array(x[pos])
  resdiff=np.diff(res)
  
  #print("resdiff:",resdiff)
  #result = all(element == resdiff[0] for element in resdiff) 
  #print("result:",result) 
  while  all(element == 0 for element in resdiff) == False:
    pos+=1
    x[pos]=resdiff
    res = np.array(x[pos])
    resdiff=np.diff(res)
  x[pos+1]=np.append(resdiff,0)
  print(x)
  
  while pos != -1:
    res=x[pos+1][-1]+x[pos][-1]
    #print(pos,res)
    x[pos]=np.append(x[pos],res)
    pos-=1
  
  print(x)
  total.append(res)
  print("####")
  x.clear()
  pos=0
print(total)
print(sum(total))
