import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)


#myinput="day03_example.txt"
myinput="day03_input.txt"

f = open(myinput, 'r')
lines = f.readlines()

counter=1
nbline=0
mylist=[]
res2=np.array([])


sub1="mul("
sub2=")"
total=0
for line in lines:
  #indx1=''.join(line.split(sub1)[1].split(sub2)[0])
  indx1=line.split(")")
  for i in indx1:
    tmp=i.split("mul(")
    for el in tmp:
      if el.find(",") > 0:
        val=el.split(",")
        print(val)
        if val[0].isnumeric() and val[1].isnumeric():
          res=int(val[0])*int(val[1])
          print(res)
          total+=res
print("########")
print(total)  
