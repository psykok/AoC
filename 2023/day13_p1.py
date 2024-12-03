#!/usr/bin/python

import re
import numpy as np
import sys
import  itertools



from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

def find_indices_of_substring(full_string, sub_string):
    return [index for index in range(len(full_string)) if full_string.startswith(sub_string, index)]

def getmirror(myarray,direction):
  print("#########:")
  #print(myarray)
  res=0
  if direction == "x":
    xflat=myarray.sum(axis=0)
    print("x:",xflat)
    array_len=myarray.shape[1]
    for i in range(2,(array_len-1)):
      if np.array_equal(myarray[:,i],myarray[:,i-1]):
        r=i
        l=i-1
        while l >=0 and r < (array_len):
          if np.array_equal(myarray[:,r],myarray[:,l]):
            res=(i)
          else:
            res=0
            print("break : ",i,r,l,myarray[:,r],myarray[:,l])
            break
          r+=1
          l-=1
        if res>0:
          break
  else:
    xflat=myarray.sum(axis=1)
    print("y:",xflat)
    array_len=myarray.shape[0]
    for i in range(2,(array_len-1)):
      #print(i,np.array_equal(myarray[i,:],myarray[i-1,:]))
      if np.array_equal(myarray[i,:],myarray[i-1,:]):
        r=i
        l=i-1
        while l >=0 and r < (array_len):
          if np.array_equal(myarray[r,:],myarray[l,:]):
            res=(i*100)
          else:
            res=0
            print("break :",i,r,l,myarray[r,:],myarray[l,:])
            break
          r+=1
          l-=1        
        if res>0:
          break 
  print(res)
  return res

f = open('day13_input.txt', 'r')
lines = f.readlines()

total=0
counter=1
nbline=0
myxmap=np.array([])
myymap=np.array([])
myxlist=np.array([])
myylist=np.array([])
allarray={}
second=0
for line in lines:
  line=line.strip()

  if line:
    line=line.replace(".","0")
    line=",".join(line)
    xline=line
    yline=line
    

    yline=yline.split(",")
    for i in range(len(yline)):
      if yline[i] == "#":
        yline[i]=str(i+1)
    #print("col:", yline)      
    
    xline=xline.replace("#",str(counter))
    xline=xline.split(",")
    #print("line:", xline)      
    
    xtmp=list(map(int,xline))
    ytmp=list(map(int,yline))
    myxlist=np.array(xtmp)
    myylist=np.array(ytmp)
    if np.any(myxmap) == False:
      myxmap=myxlist
    else:
      myxmap=np.vstack((myxmap,myxlist))

    if np.any(myymap) == False:
      myymap=myylist
    else:
      myymap=np.vstack((myymap,myylist))
    
  else:
    print(myxmap)
    print(myymap)
    total+=getmirror(myxmap,"x")
    total+=getmirror(myymap,"y")
    #allarray[nbline]=mymap
    myxmap=np.array([])
    myymap=np.array([])
    myxlist=np.array([])
    myylist=np.array([])
    nbline+=1
    if second==1:
      second=0
    else:
      second=1
    counter=0
  counter+=1

print("total:",total) 
    
    
    
    
