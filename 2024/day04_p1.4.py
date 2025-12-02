import numpy as np
import sys
import re
from scipy.ndimage import rotate

np.set_printoptions(threshold=sys.maxsize)


#myinput="day04_example2.txt"
myinput="day04_input.txt"

f = open(myinput, 'r')
lines = f.readlines()

counter=1
nbline=0
mylist=np.array([])
res2=np.array([])
patern=list(map(ord, list('XMAS')))
rpatern=list(map(ord, list('SAMX')))


print(patern)
print(rpatern)

for line in lines:
  line=line.strip()
  res=list(map(ord, list(line)))
  res2=np.array(res)
  #print(res2)
  if np.any(mylist) == False:
    mylist=res2
  else:
    mylist=np.vstack((mylist,res2))
print(mylist)


total=0
res2=0
active=1

def checktarget(diag):
  tmp=np.array2string(diag)
  print(tmp)
  ltotal=0
  #indx1=''.join(line.split(sub1)[1].split(sub2)[0])
  #indx1=re.findall('(XMAS)|)SAMX',line)
  indx1=re.findall('83 65 77 88',tmp)
  ltotal+=len(indx1)
  indx2=re.findall('88 77 65 83',tmp)
  ltotal+=len(indx2)
  print(indx1,len(indx1))
  print(indx2,len(indx2))
  return ltotal


for line in mylist:
  total+=checktarget(line)

print("#####90#####")
rot90=np.rot90(mylist)
for line in rot90:
  total+=checktarget(line)


print("##### diag45")
pos=np.shape(mylist)
for i in range(-pos[0]-1,pos[1]+1,1):
  diag=np.diag(mylist,i)
  total+=checktarget(diag)

print("##### diag-45")
flip=np.fliplr(mylist)
pos=np.shape(flip)
for i in range(-pos[0]-1,pos[1]+1,1):
  diag=np.diag(flip,i)
  total+=checktarget(diag)

print("########")
print(total)  
