import numpy as np
import sys
from textwrap import wrap
import re

#np.set_priduplicatesntoptions(threshold=sys.maxsize)


myinput="day06_example"
myinput="day06_input"

f = open(myinput, 'r')
lines = f.readlines()

counter=1
nbline=0
inglist=[]
operator=[]
res2=np.array([])
mylist=np.array([])
tag=0
total=0

for line in reversed(lines):
  line=line.rstrip('\n')
  print(line)
  if nbline == 0:
    matches=re.finditer("[+*]",line)
    for match in matches:
      operator.append([match.start(),match.group()])
    print(operator)
    nbline+=1
  else:
    pos=0
    res=[]
    while pos < len(operator):
      if pos < len(operator)-1:
        item=line[operator[pos][0]:operator[pos+1][0]-1]
      else:
        item=line[operator[pos][0]:]
      #item=item.replace(' ','0')
      res.append(item)
      pos+=1
    #mylist.append(res)    
    if np.any(mylist) == False:
      mylist=np.array(res)
    else:
      mylist=np.vstack((mylist,np.array(res))) 
print(mylist)


#i=0
nbcol = np.shape(mylist)[1]
#
print(nbcol)
#tmp=''
i=0
#newlist=np.array([])
while i < nbcol:
  datacol=mylist[:,i]
  print('col',datacol) 
  tmp2=np.sort(list(map(int,datacol[:-1].copy())))
  maxlen=len(str(tmp2[-1]))
  z=0
  newlist=[]
  while z <  np.shape(datacol)[0] :
    #newlist=np.vstack((newlist,list(datacol[z])))
    toto=list(datacol[z])
    print('toto',toto)
    if np.any(newlist) == False:
      newlist=toto
    else:
      newlist=np.vstack((newlist,toto))
    #total+=eval(datacol[-1].join(datacol[:-1]))
    z+=1
  
  resnbcol = np.shape(newlist)[1] 
  n=0
  res=[]
  while n < resnbcol:
    print('newlist',newlist)
    print(newlist[:,n])
    #total+=eval(operator.join(list(map(str,newlist[:,n]))))
    indice=''.join(list(map(str,newlist[:,n])))
    indice=indice[::-1]
    res.append(indice.lstrip('0'))
    print(res)

    n+=1
  op=operator[i][1]
  total+=eval(op.join(res))
  print(op.join(res))
  print(eval(op.join(res)))

  #print(list(map(str,newlist)))
  #total+=eval(operator.join(newlist))
  i+=1

print("#########")
print(total)
