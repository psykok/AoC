import numpy as np
import sys
import re
from scipy.ndimage import rotate

import itertools as it
from itertools import product

np.set_printoptions(threshold=sys.maxsize)


#myinput="day09_example.txt"
myinput="day09_input.txt"

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
  res=list(map(int, list(line)))
  #res2=np.array(res)
  #tmp[1]=res
  mylist=res
print(mylist)
#print(mylist[1])
print("#####")

id=0
#for i in range(0,len(mylist),2):
#  print(i,mylist[i])
#  print("".join(map(str,list(it.repeat(id,mylist[i])))))
#  if ((i+1)<len(mylist)):
#    print(list(it.repeat(".",mylist[i+1])))
#  id+=1a
res=[]
for i in range(len(mylist)):
  #print(i,mylist[i] )
  if (i % 2 == 0):
    #print("".join(map(str,list(it.repeat(id,mylist[i])))))
    #res(list(it.repeat(id,mylist[i])))
    res += list(it.repeat(id,mylist[i]))
    id+=1
  else:
    res += list(it.repeat(".",mylist[i]))
print(res)

#myres ="".join(map(str,res))

ressize=len(res)-1
revpos=ressize
for i in range(ressize):
  if res[i] == '.':
    while (res[revpos] == '.') & (revpos>i):
      revpos-=1
    res[i]=res[revpos]
    res[revpos]="."
    revpos=ressize
    

print(res) 

pos=0
total=0
for i in res:
  print()
  if i != ".":
    
    print(pos, i)
    total+=pos * i
    pos+=1

print("########")
print(total)  
