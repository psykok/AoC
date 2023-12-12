#!/usr/bin/python

import re
import numpy as np
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(50000)
print(sys.getrecursionlimit())

def navigate(counter,x,y,x_prev,y_prev):
  position=mymap[y][x]
  if counter==0:
    for cursor in [(1,0),(-1,0),(0,1),(0,-1)]:
      counter+=1
      navigate(counter,x+cursor[0],y+cursor[1],x,y)
  else:
    counter+=1
    prevpos=mymap[y_prev][x_prev]
    #print(counter, "pos", position,x,y)
    #print(counter,"    prev",prevpos,x_prev,y_prev)
    dead=0
    match position:
      case "|":#south and north
        if x_prev == x:
          if y_prev > y:
            navigate(counter,x,y-1,x,y) 
          else:
            navigate(counter,x,y+1,x,y) 
        else:
          print("### DEBUG |:",x_prev,y_prev,x,y)
          dead=1
      case "-":#east and west
        if y_prev == y:
          if x_prev > x:
            navigate(counter,x-1,y,x,y) 
          else:
            navigate(counter,x+1,y,x,y) 
        else:
          print("### DEBUG -:",x_prev,y_prev,x,y)
          dead=1
      case "L":#north and east
          if y_prev < y:
            navigate(counter,x+1,y,x,y) 
          elif x_prev > x:
            navigate(counter,x,y-1,x,y) 
          else:
            print("### DEBUG L:",x_prev,y_prev,x,y)
            dead=1
      case "J":#north and west
          if y_prev < y:
            navigate(counter,x-1,y,x,y) 
          elif x_prev < x:
            navigate(counter,x,y-1,x,y) 
          else:
            print("### DEBUG J:",x_prev,y_prev,x,y)
            dead=1
      case "7":#south and west
          if y_prev > y:
            navigate(counter,x-1,y,x,y) 
          elif x_prev < x:
            navigate(counter,x,y+1,x,y) 
          else:
            print("### DEBUG 7:",x_prev,y_prev,x,y)
            dead=1
      case "F":#south and east
          if y_prev > y:
            navigate(counter,x+1,y,x,y) 
          elif x_prev > x:
            navigate(counter,x,y+1,x,y) 
          else:
            print("### DEBUG -F:",x_prev,y_prev,x,y)
            dead=1
      case ".":#stop
        dead=1
      case "S":#stop
        dead=10
    if((dead==1) and (counter >2)):
      print("dead")
      return counter
    elif dead==10:
      print("finish",(counter-1)/2)
      return counter
   

f = open('day10_input.txt', 'r')
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
counter=0
print(mymap)
print(nav)
navigate(counter,nav[0],nav[1],nav[0],nav[1])
      
