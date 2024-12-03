import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)


#myinput="day02_example2.txt"
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
  print("#########")
  print(i)
  print(tt)
  ttpos=np.shape(tt)[0]
  pos=np.where(tt>0)
  neg=np.where(tt<0)
  zero=np.where(tt==0)
  nbpos=np.shape(pos)[1]  
  nbneg=np.shape(neg)[1]  
  nbzero=np.shape(zero)[1]  
  print(pos,nbpos)
  print(neg,nbneg)
  print(zero,nbzero)
  res=0
  mod=0 
  if (ttpos==nbpos) or (ttpos==nbpos+1):
    print(tt)
    if(nbneg == 1):
      tt=np.delete(tt,neg[0],0)
      mod=1
    elif(nbzero == 1):
      tt=np.delete(tt,zero[0]+1,0)
      mod=1
    print(tt)

    if np.all((tt <4) & (tt>0)):
      res=1
    else:
      todel=np.where(tt>3)
      if (np.shape(todel)[1] == 1) & (mod == 0):
        tmp=np.delete(i,todel[0]+1,0)
        tt=np.diff(tmp)
        print(tmp)
        print(tt)        
        if np.all((tt <4) & (tt>0)):
          res=1
        else:
          tmp=np.delete(i,todel[0],0)
          tt=np.diff(tmp)
          print(tmp)
          print(tt)
          if np.all((tt <4) & (tt>0)):
            res=1
  elif ttpos==nbneg or (ttpos==nbneg+1):
    print(tt)
    if(nbpos == 1):
      tt=np.delete(tt,pos[0],0)
      mod=1
    elif(nbzero == 1):
      tt=np.delete(tt,zero[0],0)
      mod=1
    print(tt)
    if np.all((tt >-4)&(tt<0)):
      res=1
    else:
      todel=np.where(tt<-3)
      if (np.shape(todel)[1] == 1) & (mod == 0):
        tmp=np.delete(i,todel[0]+1,0)
        tt=np.diff(tmp)
        print(tmp)
        print(tt)
        if np.all((tt >-4) & (tt<0)):
          res=1
        else:
          tmp=np.delete(i,todel[0],0)
          tt=np.diff(tmp)
          print(tmp)
          print(tt)
          if np.all((tt >-4) & (tt<0)):
            res=1
  print(res)
  rescount+=res

print(rescount)
