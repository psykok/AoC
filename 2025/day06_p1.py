import numpy as np
import sys
from textwrap import wrap
import re

#np.set_priduplicatesntoptions(threshold=sys.maxsize)


myinput="day06_example"
#myinput="day06_input"

f = open(myinput, 'r')
lines = f.readlines()

counter=1
nbline=0
inglist=[]
res2=np.array([])
mylist=np.array([])
tag=0
total=0

for line in lines:
  line=line.strip()

  #print(line)
  res=list(map(str, re.split(r' +',line)))
  res2=np.array(res)
  #print(res2)
  if np.any(mylist) == False:
    mylist=res2
  else:
    mylist=np.vstack((mylist,res2))
print(mylist)


#  exit(0)
i=0
nbcol = np.shape(mylist)[1]

print(nbcol)

newlist=np.array([])
while i < nbcol:
  datacol=mylist[:,i]
  print(datacol)

#    newlist=np.vstack((newlist,list(datacol[z])))
  total+=eval(datacol[-1].join(datacol[:-1]))
  i+=1

print("#########")
print(total)
