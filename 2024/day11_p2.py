import numpy as np
import sys
import re
from scipy.ndimage import rotate
import functools


import itertools as it
from itertools import product

np.set_printoptions(threshold=sys.maxsize)
sys.setrecursionlimit(1000000)

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

@functools.cache
def stonecheck(mystone,pos):
  if(pos == -1): 
    return 1
  
  nbdigit=len(mystone)
  print(mystone,nbdigit,pos)
  
  if mystone == '0':
    #print("titi")
    res='1'
    tmp=stonecheck(res,pos-1)
    return tmp
  elif (nbdigit % 2) == 0:
    #print("toto")
    half=nbdigit // 2
    res=str(int(mystone[:half]))
    tmp1=stonecheck(res,pos-1)
    res=str(int(mystone[half:]))
    tmp2=stonecheck(res,pos-1)
    return tmp1 + tmp2 
  else:
    res=str(int(mystone) * 2024)
    tmp=stonecheck(res,pos-1)
    #print(res)
    return tmp 
  #print(res,pos) 

 
#tmp=stonecheck('125',2)
#print(tmp)

#for i in ['253000', '1', '7']:
#  tmp+=stonecheck(i) 
for i in mylist:
  total+=stonecheck(i,74)
    





print("########")
print(total)  
