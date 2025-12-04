import numpy as np
import sys
from textwrap import wrap

#np.set_priduplicatesntoptions(threshold=sys.maxsize)


myinput="day03_example"
myinput="day03_input"

f = open(myinput, 'r')
lines = f.readlines()

counter=1
nbline=0
mylist=[]
res2=np.array([])

for line in lines:
    a=list(line.strip())
    res=list(map(int,a))
    print(res)
    res2=np.array(res)
    #print(res2)
    #mylist.append(np.sort(res2))
    mylist.append(res2)
print(mylist)

total=0
for bank in mylist:
  print(bank)
  v1=bank[0]
  v2=bank[1]
  banklen=len(bank)
  i=1
  
  while i < banklen-1:
   extra=0
   if bank[i] > v1:
     v1=bank[i]
     v2=0
   if bank[i+1] > v2:
     v2=bank[i+1]
   i+=1
  total+=int(''.join([str(v1),str(v2)]))

    
#  rstart=int(idrange[0])
#  rstop=int(idrange[1])+1
#  for x in range(int(rstart),int(rstop)):
#    xsize=len(str(x))
#    for i in range(1,xsize):
#      if i == xsize/2:
#        if xsize % 2 == 0:
#          #print(i)
#          tmplist=wrap(str(x),width=i)
#          #print(tmplist)
#          unique,counts=np.unique(tmplist,return_counts=True)
#          #print(unique,counts)
#          #print(counts[0],len(tmplist))
#          if counts[0] == len(tmplist):
#            print("Duplicates:", x)
#            total+=x
#            break
#  exit(0)

print("#########")
print(total)
