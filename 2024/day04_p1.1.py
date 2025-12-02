import numpy as np
import sys
import re

np.set_printoptions(threshold=sys.maxsize)


myinput="day04_example.txt"
#myinput="day04_input.txt"

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

for line in mylist:
  tmp=np.array2string(line)
  print(tmp)
  #indx1=''.join(line.split(sub1)[1].split(sub2)[0])
  #indx1=re.findall('(XMAS)|)SAMX',line)
  indx1=re.findall('83 65 77 88',tmp)
  total+=len(indx1)
  indx2=re.findall('88 77 65 83',tmp)
  total+=len(indx2)
  print(indx1)
  print(indx2)
print("#####90#####")
rot90=np.rot90(mylist)
for line in rot90:
  tmp=np.array2string(line)
  print(tmp)
  #indx1=''.join(line.split(sub1)[1].split(sub2)[0])
  #indx1=re.findall('(XMAS)|)SAMX',line)
  indx1=re.findall('83 65 77 88',tmp)
  total+=len(indx1)
  indx2=re.findall('88 77 65 83',tmp)
  total+=len(indx2)
  print(indx1)
  print(indx2)

print("##### diag")
nbsteps=np.shape(mylist)[0]
for i in range(-nbsteps,nbsteps,1):
  diag=np.diagonal(mylist,i)
  tmp=np.array2string(diag)
  #indx1=''.join(line.split(sub1)[1].split(sub2)[0])
  #indx1=re.findall('(XMAS)|)SAMX',line)
  indx1=re.findall('83 65 77 88',tmp)
  total+=len(indx1)
  indx2=re.findall('88 77 65 83',tmp)
  total+=len(indx2)
  print(indx1)
  print(indx2)


print("##### diag")
nbsteps=np.shape(rot90)[0]
for i in range(-nbsteps,nbsteps,1):
  diag=np.diagonal(rot90,i)
  tmp=np.array2string(diag)
  #indx1=''.join(line.split(sub1)[1].split(sub2)[0])
  #indx1=re.findall('(XMAS)|)SAMX',line)
  indx1=re.findall('83 65 77 88',tmp)
  total+=len(indx1)
  indx2=re.findall('88 77 65 83',tmp)
  total+=len(indx2)
  print(indx1)
  print(indx2)
print("########")
print(total)  
