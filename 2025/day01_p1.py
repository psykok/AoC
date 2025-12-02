import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)


myinput="day01_example"
myinput="day01_input"

f = open(myinput, 'r')
lines = f.readlines()

counter=1
nbline=0
mylist=[]
res2=np.array([])

for line in lines:
  line=line.strip()
  res2=np.array([line[:1],line[1:]])
  #print(res2)
  mylist.append(res2)
print(mylist)

rescount=50
total=0
#print(mylist)
for i in mylist:
  direc,steps=i
#  print(direc)
#  print(steps)
  res=0
  if direc == "L":
    rescount-=int(steps)
    while rescount < 0:
      rescount+=100
  else:
    rescount+=int(steps)
    while rescount > 99:
      rescount-=100
  if rescount == 0:
    total+=1 
  print(rescount,total)
print(total)
