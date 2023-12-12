#!/usr/bin/python

import re
import numpy as np
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)
print(sys.getrecursionlimit())

def navigate(counter,x,y):
  position=mymap[y][x]
  counter+=1

  for cursor in [(1,0),(-1,0),(0,1),(0,-1)]:
    x_pos=x+cursor[0]
    y_pos=y+cursor[1]
    if ((x_pos<0) or (y_pos<0) or (x_pos==len(mymap[y_pos])) or (y_pos==len(mymap))): 
      continue
    nextpos=mymap[y_pos][x_pos]
    print(counter, "cur",cursor)
    print(counter, "pos", position)
    print(counter,"next",nextpos)
    dead=0
    match nextpos:
      case "|":#south and north
        if cursor[1] == 0:
          dead=1
        else:
          navigate(counter,x+cursor[0],y+2*cursor[1]) 
      case "-":#east and west
        if cursor[0] == 0:
          dead=1
        else:
          navigate(counter,x+2*cursor[0],y+cursor[1]) 
      case "L":#north and east
        if cursor[0] == -1:
          navigate(counter,x+cursor[0],y+cursor[1]+1)
        elif cursor[1] == -1:
          navigate(counter,x+cursor[0]+1,y+cursor[1])
        else:
          dead=1
      case "J":#north and west
        if cursor[1] == -1:
          navigate(counter,x+cursor[0]-1,y+cursor[1])
        elif cursor[0] == +1:
          navigate(counter,x+cursor[0],y+cursor[1]+1)
        else:
          dead=1
      case "7":#south and west
        if cursor[0] == 1:
          navigate(counter,x+cursor[0],y+cursor[1]-1)
        elif cursor[1] == 1:
          navigate(counter,x+cursor[0]-1,y+cursor[1])
        else:
          dead=1
      case "F":#south and east
        if cursor[0] == -1:
          navigate(counter,x+cursor[0],y+cursor[1]-1)
        elif cursor[1] == 1:
          navigate(counter,x+cursor[0]+1,y+cursor[1])
        else:
          dead=1
      case ".":#stop
        dead=1
    if((dead==1) and (counter >2)):
      return counter
      print("dead")
   

f = open('day10_example.txt', 'r')
lines = f.readlines()

nav=np.array([])

counter=0
start=[]
mymap = {}
for line in lines:
  line=line.strip()
  mymap[counter]=line
  pos=line.find("S")
  if pos != -1:
    #start=list(pos,counter)
    nav=np.array([pos,counter])
  counter+=1
print(mymap)
print(nav)
navigate(counter,nav[0],nav[1])
      
