#!/usr/bin/python

import re
import json

f = open('day2_input.txt', 'r')
lines = f.readlines()

myrecords={}
content=[]
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
    mylist.clear()
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
    mylist.append(red)
    mylist.append(green)
    mylist.append(blue)
    content.append(json.dumps(mylist))
 #   print(keyid,mylist,content)
  myrecords[keyid.strip()]=json.dumps(content)
#  print(content)
  content.clear()
  if compat==1:
    total.append(int(keyid.strip()))
#print(myrecords)
print(total)
print(sum(total))
