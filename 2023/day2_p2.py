#!/usr/bin/python

import re
import json
import numpy as np

f = open('day2_input.txt', 'r')
lines = f.readlines()

myrecords={}
content=np.array([])
mylist=[] #red,gree,blue
total=[]
for line in lines:
  compat=1
  line=line.replace("\n","")
 #Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green  
  key, value=line.split(":")
  keyname, keyid=key.split(" ")

  for i in value.split(";"):
    red=blue=green=0
    mylist=[]
    for j in i.split(","):
      j=j.strip()
      nb, color=j.split(" ")
      nb=int(nb)
      if color == "red":
        red=int(nb)
        if nb > 12:
          compat=0
      elif color == "blue":
        blue=int(nb)
        if nb > 14:
          compat=0
      elif color == "green":
        green=int(nb)
        if nb >13:
          compat=0
    mylist=np.append(mylist,red)
    mylist=np.append(mylist,green)
    mylist=np.append(mylist,blue)
    if np.any(content) == False:
      content=mylist
    else:
      content=np.vstack((content,mylist))
    
 #   print(keyid,mylist,content)
  total.append(np.prod(content.max(axis=0)))
  myrecords[keyid.strip()]=content
  content=[]
print(myrecords)
print(total)
print(sum(total))
