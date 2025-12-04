import numpy as np
import sys
from textwrap import wrap

#np.set_priduplicatesntoptions(threshold=sys.maxsize)


myinput="day02_example"
myinput="day02_input"

f = open(myinput, 'r')
lines = f.readlines()

counter=1
nbline=0
mylist=[]
res2=np.array([])

for line in lines:
  for item in line.split(','):
    res2=np.array(item.split('-'))
    #print(res2)
    mylist.append(res2)
print(mylist)


def datasort(total,x,myrange,pos):
  #print(i)
  i=myrange[pos]
  tmplist=wrap(str(x),width=i)
  #print(tmplist)
  unique,counts=np.unique(tmplist,return_counts=True)
  #print(unique,counts)
  #print(counts[0],len(tmplist))
  if pos <len(myrange)-1:
    if counts[0] == len(tmplist):
      print("Duplicates:", x)
      return(x)
      total+=datasort(total,x,myrange,pos)
      pos+=1
  else:
    return(x)

total=0
for idrange in mylist:
  print(idrange)
  rstart=int(idrange[0])
  rstop=int(idrange[1])+1
  for x in range(int(rstart),int(rstop)):
    xsize=len(str(x))
    myrange=range(1,xsize)
    pos=0
    datasort(total,x,myrange,pos)
    
#  exit(0)

print("#########")
print(total)
