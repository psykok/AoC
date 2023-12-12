#!/usr/bin/python

import re
import numpy as np
import sys
from  itertools import combinations as comb 



from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

def find_indices_of_substring(full_string, sub_string):
    return [index for index in range(len(full_string)) if full_string.startswith(sub_string, index)]

f = open('day11_input.txt', 'r')
lines = f.readlines()


counter=1
nbline=0
mymap=np.array([])
mylist=np.array([])

for line in lines:
  line=line.strip()
  line=line.replace(".","0")
  tmp=list(line)
  
  nav = 0
  for tag in tmp:
    if tag == "#":
      tmp[nav]=counter   
      counter+=1
    nav+=1
  tmp=list(map(int,tmp))  
  #print(tmp)
  #print(nbline,len(line))
  mylist=np.array(tmp)
  if np.any(mymap) == False:
    mymap=mylist
  else:
    mymap=np.vstack((mymap,mylist)) 
  nbline+=1
counter=0
#print(mymap)

#expand col
nb_rows=np.shape(mymap)[0]
xflat=mymap.sum(axis=0)
pos=0
x_poslist=[]
for x in xflat:
  if x==0:
    x_poslist.append(pos)
  pos+=1

print(xflat)
print(x_poslist)
#print(mymap.sum(axis=0))
#print(mymap)

#expand rows
nb_col=np.shape(mymap)[1]
xflat=np.array([])
xflat=mymap.sum(axis=1)
pos=0
y_poslist=[]
for x in xflat:
  if x==0:
    y_poslist.append(pos)
  pos+=1
#poslist.reverse()
#for i in poslist:
#  for exp in range (2):
#    mymap=np.insert(mymap,i,np.zeros(nb_col),axis=0)
print(xflat)
print(y_poslist)
#print(mymap)
#print(mymap.sum(axis=1))

####################################
#arr=np.transpose(np.nonzero(mymap))
arr=np.stack(np.nonzero(mymap), axis=-1)
cnt=0
total=0

tmp=[]
exp_factor=999999

for a in range(len(arr)):
   x=int(arr[a][1])
   oldx=x
   xexp=0
   for xpos in x_poslist:
     if xpos < x:
        xexp+=exp_factor
   x+=xexp
   #################
   y=int(arr[a][0])
   oldy=y
   yexp=0
   for ypos in y_poslist:
     if ypos < y:
        yexp+=exp_factor
   y+=yexp
   print("(",oldx,",",x,"),(",oldy,",",y,")")
   tmp.append((x,y))
print(tmp)
total=0
for i in list(comb(tmp,2)):
  #print(i)
  total+=sum(abs(np.subtract(i[1],i[0])))
print(total)

