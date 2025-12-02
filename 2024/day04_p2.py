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
  print(dshape) 
  ftotal=0
  for x in range(dshape[0]-xlimit):
    for y in range(dshape[1]-ylimit):
      cursa=myarray[x,y] + myarray[x+a[0],y+a[1]] + myarray[x+b[0],y+b[1]]
      xb=x+2
      cursb=myarray[xb,y] + myarray[xb-a[0],y+a[1]] + myarray[xb-b[0],y+b[1]]
      print(cursa,cursb) 
      if (cursa == "MAS") | (cursa == "SAM"):
        if (cursb == "MAS") | (cursb == "SAM"):
          ftotal+=1
          #print(curs,"ok")
  return ftotal 

total+=checkdata(mylist,2,2,(1,1),(2,2),(3,3)) 
#1911
print("########")
print(total)  
