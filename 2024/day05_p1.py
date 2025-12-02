import numpy as np
import sys
import re
from scipy.ndimage import rotate

np.set_printoptions(threshold=sys.maxsize)


myinput="day05_example.txt"
#myinput="day05_input.txt"

f = open(myinput, 'r')
lines = f.readlines()

counter=1
nbline=0
mylist=np.array([])
res2=np.array([])
mypages=[]
total=0


def getmiddle(myarray):
  asize=len(myarray)
  return(int(myarray[asize//2]))

switch=0
for line in lines:
  line=line.strip()
  if line == "":
    switch = 1
  if switch==0:
    res=list(map(str, list(line.split('|'))))
    res2=np.array(res)
    #print(res2)
    if np.any(mylist) == False:
      mylist=res2
    else:
      mylist=np.vstack((mylist,res2))
  elif (switch==1) & (len(line) > 0):
    res=list(map(str, line.split(',')))
    res2=np.array(res)
    #print(res2)
    mypages.append(res2)
print(mylist)
print(mypages)

for pline in mypages:
  status=0
  for i in range(len(pline)):
    for rule in mylist:
      if rule[0]==pline[i]:
        for chkpos in range(i):
          #print(pline[chkpos],rule[1])
          if pline[chkpos]==rule[1]:
            print("########BAD")
            print(pline)
            print(rule)
            tmp=np.delete(pline,int(chkpos))
            pline=np.insert(tmp,i,pline[chkpos])
            print(tmp)
            print(pline)
            #print("########")
            i-=1
            status=1
  print(pline,status) 
  if status==1:
    total+=getmiddle(pline)
#6385 to low
print("########")
print(total)  
