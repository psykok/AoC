import numpy as np
import sys
import string
from textwrap import wrap

#np.set_priduplicatesntoptions(threshold=sys.maxsize)


myinput="day03_example"
#myinput="day03_input"

f = open(myinput, 'r')
lines = f.readlines()

counter=0
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
  banklen=len(bank)
  print(bank,banklen)
  resbank=np.copy(bank[banklen-12:])
  #resbank=np.zeros((12,), dtype=int)
  i=0
  pos=0
  tmp=0
  counter=0
  while len(bank) > 12:
  #  print(i,pos,bank[i], bank[i+1],bank)
       
    if bank[i] <= bank[i+1]:
#      print('in',i,pos,bank)
      bank=np.delete(bank,i)
      i-=1
 #     print('in',pos,bank)
    if i<10:
      i+=1
 
  tmp=int(''.join(map(str,bank)))
  print(tmp)
  total+=tmp
#  exit(0)    

print("#########")
print(total)
