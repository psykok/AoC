import numpy as np
import sys
import re
from scipy.ndimage import rotate

np.set_printoptions(threshold=sys.maxsize)


#myinput="day04_example.txt"
myinput="day04_input.txt"

f = open(myinput, 'r')
lines = f.readlines()

counter=1
nbline=0
mylist=np.array([])
res2=np.array([])

for line in lines:
  line=line.strip()
  res=list(map(str, list(line)))
  res2=np.array(res)
  #print(res2)
  if np.any(mylist) == False:
    mylist=res2
  else:
    mylist=np.vstack((mylist,res2))
print(mylist)

total=0



#XMAS
xlimit=0
ylimit=4
def checkdata(myarray,xlimit,ylimit,a,b,c):
  dshape=np.shape(myarray)
  ftotal=0
  for x in range(dshape[0]-xlimit):
    for y in range(dshape[1]-ylimit):
      curs=myarray[x,y] + myarray[x+a[0],y+a[1]] + myarray[x+b[0],y+b[1]] + myarray[x+c[0],y+c[1]]
      #print(curs) 
      if (curs == "XMAS") | (curs == "SAMX"):
         ftotal+=1
         #print(curs,"ok")
  return ftotal 
print("###### vert")
#check vert
total+=checkdata(mylist,0,3,(0,1),(0,2),(0,3)) 
print("###### hor")

#check honrizontal 
#total+=checkdata(4,0) 
total+=checkdata(mylist,3,0,(1,0),(2,0),(3,0)) 
print("###### diag right")
total+=checkdata(mylist,3,3,(1,1),(2,2),(3,3)) 
flip=np.fliplr(mylist)
total+=checkdata(flip,3,3,(1,1),(2,2),(3,3)) 

print("########")
print(total)  
