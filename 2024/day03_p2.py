import numpy as np
import sys
import re

np.set_printoptions(threshold=sys.maxsize)


#myinput="day03_example_p2.txt"
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
res2=0
#print(lines)
active=1
for line in lines:
  #indx1=''.join(line.split(sub1)[1].split(sub2)[0])
  indx1=re.findall('mul\(\d+,\d+\)|do\(\)|don\'t\(\)',line)
  for i in indx1:
    if (i.find("mul") >=0) & (active ==1):
      res=re.findall('\d+,\d+',i)
      val=res[0].split(",")
      res2=int(val[0])*int(val[1])
      total+=res2
      print(i)
    elif (i.find("do(") >=0):
      active=1
      print(i)
    elif (i.find("don") >=0):
      active=0
  print("#### line")
print("########")
print(total)  
