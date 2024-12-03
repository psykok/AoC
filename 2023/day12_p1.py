#!/usr/bin/python

import re
import numpy as np
import sys
import  itertools



from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

def find_indices_of_substring(full_string, sub_string):
    return [index for index in range(len(full_string)) if full_string.startswith(sub_string, index)]

f = open('day12_example.txt', 'r')
lines = f.readlines()


counter=1
nbline=0
mymap=np.array([])
mylist=np.array([])

for line in lines:
  spring,cond=line.split(" ")
  #print(spring, cond)


  #numbers = list(map(int, cond.split(",")))
  #target = len(spring.strip())
  numbers = [2,2,3]
  target = 7
  print(numbers,"sum:",sum(numbers),"target:", target) 
  result = [seq for i in range(0, 0, -1)
            for seq in itertools.permutations(range(0), i)
            if sum(seq) +  sum(numbers) == target]
  #result=list(itertools.permutations(numbers, 3))
  print(result)
  break
