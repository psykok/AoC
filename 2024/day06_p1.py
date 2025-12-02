import numpy as np
import sys
import re
from scipy.ndimage import rotate

np.set_printoptions(threshold=sys.maxsize)


#myinput="day06_example.txt"
myinput="day06_input.txt"

f = open(myinput, 'r')
lines = f.readlines()

counter=1
nbline=0
mylist=np.array([])
res2=np.array([])
mypages=[]
total=0
start_pos=()

def getmiddle(myarray):
  asize=len(myarray)
  return(int(myarray[asize//2]))

switch=0
linenb=0
for line in lines:
  line=line.strip()
  line=line.replace(".","0")
  line=line.replace("#","2")
  res=re.search('\^',line)
  if res:
    start_pos=(linenb,res.start())
    print(start_pos)
  line=line.replace("^","9")
  res=list(map(int, list(line)))
  res2=np.array(res)
  #print(res2)
  if np.any(mylist) == False:
    mylist=res2
  else:
    mylist=np.vstack((mylist,res2))
  linenb+=1
print(mylist)

direc=(-1,0)

def navigation(start,direction,mymap):
  x,y=start
  dirx, diry=direction
  pos=()
  nextpos=()

  pos=start
  limit=np.shape(mymap)
  print(limit)
  while True:
    if (mymap[pos] == 9) | (mymap[pos] == 0) | (mymap[pos] ==1) :
      print(pos,mymap[pos])
      mymap[pos]=1
      pos=pos[0]+dirx,pos[1]+diry
      if(mymap[pos] == 2 ):
        #print("DEBUG:", pos)
        pos=pos[0]-dirx,pos[1]-diry
        if (dirx == -1) & (diry == 0):
          dirx=0
          diry=1
        elif (dirx == 0) & (diry == 1):
          dirx=1
          diry=0  
        elif (dirx == 1) & (diry == 0):
          dirx=-0
          diry=-1 
        elif (dirx == 0) & (diry == -1):
          dirx=-1
          diry=0  
        pos=pos[0]+dirx,pos[1]+diry
        
        print("turn")
        print(pos,dirx,diry)



    if(pos[0]==limit[0]-1) | (pos[1]==limit[1]-1) | (pos[0]==0) | (pos[1]==0): 
      print("exit")
      return

navigation(start_pos,direc,mylist)
print(mylist)

for line in mylist:
  total+=len(re.findall('1',np.array2string(line)))




print("########")
print(total+1)  
