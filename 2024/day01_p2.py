import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)


#myinput="day01_example.txt"
myinput="day01_input.txt"

f = open(myinput, 'r')
lines = f.readlines()

counter=1
nbline=0
mylist=np.array([])
res2=np.array([])

for line in lines:
  line=line.strip()
  res=list(map(int, line.split()))
  res2=np.array(res)
  #print(res2)
  if np.any(mylist) == False:
    mylist=res2
  else:
    mylist=np.vstack((mylist,res2))
print(mylist)

total=0
for i in mylist[:,0]:
  pos=np.count_nonzero(mylist[:,1] == i)
  val=i * pos
  total+=val

print(total)
