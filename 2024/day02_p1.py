import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)


#myinput="day02_example.txt"
myinput="day02_input.txt"

f = open(myinput, 'r')
lines = f.readlines()

counter=1
nbline=0
mylist=[]
res2=np.array([])

for line in lines:
  line=line.strip()
  res=list(map(int, line.split()))
  res2=np.array(res)
  #print(res2)
  mylist.append(res2)
#print(mylist)

rescount=0

#print(mylist)
for i in mylist:
  tt=np.diff(i)
  print(i)
  res=0
  if np.all(tt >0):
    if np.all(tt <4):
      res=1
  elif np.all(tt <0):
    if np.all(tt>-4):
      res=1
  print(res)
  rescount+=res

print(rescount)
