import numpy as np
import sys
from textwrap import wrap

#np.set_priduplicatesntoptions(threshold=sys.maxsize)


myinput="day04_example"
myinput="day04_input"

f = open(myinput, 'r')
lines = f.readlines()

counter=1
nbline=0
mylist=[]
res2=np.array([])

for line in lines:
  line = line.replace('.', '0')
  line = line.replace('@', '1')


  a=list(line.strip())
  res=list(map(int,a))
  print(res)
  res2=np.array(res)
  #print(res2)
  #mylist.append(np.sort(res2))
  mylist.append(res2)
#print(mylist)

listsize=len(mylist)

linesize=len(mylist[0])
total=0
for i in range(0,listsize):
  status=0
  pos=0
  print(mylist[i])
  while pos < linesize:
    if mylist[i][pos] == 1:
       if pos < linesize - 1:
         if  mylist[i][pos+1] == 1:
           status+=1
       if pos > 0 :
         if mylist[i][pos-1] == 1:
           status+=1
       if i < listsize-1:
         if mylist[i+1][pos] == 1:
           status+=1
       if i > 0: 
         if mylist[i-1][pos] == 1:
           status+=1
       if pos < linesize-1 and i < listsize-1:
         if mylist[i+1][pos+1] == 1:
           status+=1
       if pos < linesize-1 and i > 0:
         if mylist[i-1][pos+1] == 1:
           status+=1
       if pos > 0 and i < linesize-1:
         if mylist[i+1][pos-1] == 1:
           status+=1
       if pos > 0 and  i > 0:
         if mylist[i-1][pos-1] == 1:
           status+=1
       if status < 4:
         print(i,pos)
         total+=1
    pos+=1  
    status=0 



#  exit(0)

print("#########")
print(total)
