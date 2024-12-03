#!/usr/bin/python

import re
import numpy as np
import sys
import  itertools



from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

def find_indices_of_substring(full_string, sub_string):
    return [index for index in range(len(full_string)) if full_string.startswith(sub_string, index)]

f = open('day13_input.txt', 'r')
lines = f.readlines()


counter=1
nbline=0
mymap=np.array([])
mylist=np.array([])
allarray={}
second=0
for line in lines:
  line=line.strip()
  if line:
    line=line.replace(".","0")
    line=",".join(line)
    if second==1:
      line=line.split(",")
      for i in range(len(line)):
      	if line[i] == "#":
          line[i]=str(i+1)
      #print("col:", line)      
    else:
      second=0
      line=line.replace("#",str(counter))
      line=line.split(",")
      #print("line:", line)      
    tmp=list(map(int,line))
    mylist=np.array(tmp)
    if np.any(mymap) == False:
      mymap=mylist
    else:
      mymap=np.vstack((mymap,mylist))
  else:
    allarray[nbline]=mymap
    mymap=np.array([])
    mylist=np.array([])
    nbline+=1
    if second==1:
      second=0
    else:
      second=1
    counter=0
  counter+=1
#print(allarray)

total=0
for curs in range(len(allarray)): 
  print("#########:",curs)
  print(allarray[curs])
  if (curs+1) % 2:
    xflat=allarray[curs].sum(axis=0)
  else:
    xflat=allarray[curs].sum(axis=1)
  print(xflat)
  h=[]
  res=[]
  s=set()
  list_name=xflat
  for i in list_name:
      if i in s:
          continue
      h.append(np.where(list_name==i))
      s.add(i)
      for pos in h:
        if len(pos[0])==2:
          if int(pos[0][0])+1==int(pos[0][1]):
            res.append(pos[0])
  #          a=(pos[0][0])*100
  #          b=(len(xflat)-pos[0][1]+1)
  #          total=a+b
  if (curs+1) % 2:
    total+=(res[0][0]+1)*100
  else:
    total+=res[0][0]+1
  print(res)
print(total)
