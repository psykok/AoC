import numpy as np
import sys
import re
from scipy.ndimage import rotate

import itertools as it
from itertools import product

np.set_printoptions(threshold=sys.maxsize)


#myinput="day11_example.txt"
myinput="day11_input.txt"

f = open(myinput, 'r')
lines = f.readlines()

total=0
counter=1
nbline=0
mylist=[]
res2=np.array([])

for line in lines:
  line=line.strip()
  #tmp=line.split(':')
  #tmp=tmp[1].strip()
  res=list(map(str, line.split()))
  #res2=np.array(res)
  #tmp[1]=res
  mylist=res
print(mylist)
#print(mylist[1])
print("#####")

def stonecheck(mystone):
  res=[]
  nbdigit=len(mystone)
  if mystone == '0':
    res.append('1')
  elif (nbdigit % 2) == 0:
  #  print(mystone,nbdigit,mystone[:nbdigit-1])
    half=nbdigit // 2
    res.append(str(int(mystone[:half])))
    res.append(str(int(mystone[half:])))
  else:
    res.append(str(int(mystone) * 2024)) 
  return res

for i in range(25):
  print(i)
  tmp=[]
  for pos in mylist:
    #print(pos)
    tmp+=stonecheck(pos)
  mylist=tmp
  #print(tmp)

#for i in ['253000', '1', '7']:
#  tmp+=stonecheck(i) 

print(mylist)
total=len(mylist)
    





print("########")
print(total)  
