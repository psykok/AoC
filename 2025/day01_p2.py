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
#print(mylist)

rescount=50
total=0
count=0
tag=0
print(50,total)
for i in mylist:
  direc,steps=i
#  print(direc)
#  print(steps)
  res=0
  if direc == "L":
    pres=rescount
    rescount-=int(steps)
    print(pres,rescount,total)
    while rescount < 0:
      rescount+=100
      print(pres,rescount,total)
      count+=1
      print(rescount,total)
  else:
    pres=rescount
    rescount+=int(steps)
    print(pres,rescount,total)
    while rescount > 99:
      rescount-=100
      print(pres,rescount,total)
      count+=1
      print(pres,rescount,total)
  if rescount == 0: 
      total+=1 
  tag=0
  print(i,rescount,total)
print("#########")
print(count)
print(total)
print(count-total)
