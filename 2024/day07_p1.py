import numpy as np
import sys
import re
from scipy.ndimage import rotate

import itertools
from itertools import product

np.set_printoptions(threshold=sys.maxsize)


#myinput="day07_example.txt"
myinput="day07_input.txt"

f = open(myinput, 'r')
lines = f.readlines()

total=0
counter=1
nbline=0
mylist=[]
res2=np.array([])

for line in lines:
  line=line.strip()
  tmp=line.split(':')
  tmp2=tmp[1].strip()
  res=list(map(int, tmp2.split()))
  #res2=np.array(res)
  tmp[1]=res
  print(tmp)
  mylist.append(tmp)
#print(mylist)

print("#####")

def operations(opsize):
  tmp=list(product(['+','*'], repeat=opsize))
  return tmp

def myeval(val1):
  #print(val1)
  mysum=0
  res=re.search('\d+.\d+',val1)
  mysum+=eval(res[0])
  tmp=val1[len(res[0]):]
  toremove=len(res[0])

  res=re.findall('.\d+',tmp)
  #print(res)
  for step in res:
    toremove+=len(step)
    tmp=val1[toremove:]
    #print("##########",mysum,step)
    #print("##########",eval(str(mysum)+step))
    mysum=eval("".join(str(mysum)+step))
    #print(mysum)
    
  #res=eval(val1[deb:fin])
  ##print(res)

  return mysum


for prob in mylist:
  tag=0
  for task in operations(len(prob[1])-1):
    task=task + ("-",)
    print(prob[1])
    print(task)
    res="".join(map(str, np.ravel([prob[1],task],'F')))
    #print(prob,task,myeval(res[:-1]))
    if (myeval(res[:-1]) == int(prob[0])) & (tag == 0):
      print(prob,task)
      total+=int(prob[0])
      tag=1
rescount=0
#print(mylist)

print("########")
print(total)  
