#!/usr/bin/python

import re
f = open('day2_example.txt', 'r')
lines = f.readlines()

total=0
for line in lines:
 #Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green  
  tmp=line.replace(";",",")
  key, value=split(":")
  print(tmp)
