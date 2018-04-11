# CSCI 310 Organization of Programming Languages, Spring 2018
# Program #3: Procedural/Object-Oriented Assignment
# Author: Zack Maguffin
# Date Due: 9 April 2018
# This assignment simulates life in the real world, specifically at your first job.

 
def hlbackwards(myList):
  newList = []
  for x in reversed(myList):
    newList.append(x)
  return newList
  
def llbackwards(myList):
  newList = []
  for x in reversed(myList):
    if isinstance(x, list):
      newList.append(llbackwards(x))
    else:
      newList.append(x)
  return newList
  
def palindrome(myList):
  newList = []
  newList = llbackwards(newList)
  if myList == newList:
    print("This is a panlindrome")
  else:
    newList.append(myList)
  tempList = newList
  tempList = tempList[0]
  return tempList

def permutations(myList):
  from itertools import permutations
  tempList = permutations(myList)
  for x in list(tempList):
    print(x)
  
def ionah(num):
  ionahHelper(num, 1, 2, 3)

def ionahHelper(num, beg, mid, end):
  if num > 0:
    ionahHelper(num-1, mid, end, beg)
    ionahPrint(mid, end)
    ionahHelper(num-1, end, mid, beg)

def ionahPrint(first, second):
  print("Move Peg from '{}' to '{}' ".format(first, second))

def sequence(num):
  result = []
  if num  == 1:
    return [0]
  elif num == 2:
    return [1]
  elif num > 2:
    X = [sequenceMath(num)]
    result = X + sequence(num-1)
  return sorted(result)
  
def sequenceMath(num):
  if num == 1:
    return 0
  elif num == 2:
    return 1
  else:
    x = sequenceMath(num - 1)
    y = sequenceMath(num - 2)
    z = (2 * x) + y
    return z
    
def argue(line):
  for x in range(0, len(line)):
    if line[x] == 'i':
      line[x] = 'you'
    elif line[x] == 'I':
      line[x] = 'you'
    elif line[x] == 'you':
      line[x] = 'i'
    elif line[x] == 'does':
      line[x] = 'does not'
    elif line[x] == 'does not':
      line[x] = 'does'
    elif line[x] == 'are':
      line[x] = 'am not'
    elif line[x] == 'is':
      line[x] = 'is not'
    elif line[x] == 'is not':
      line[x] = 'is'
    elif line[x] == 'my':
      line[x] = 'your'
    elif line[x] == 'your':
      line[x] = 'my'
    elif line[x] == "am":
      line[x] = 'are not'
    elif line[x] == 'are not':
      line[x] = 'am'
  return line 

def bubblesort(tempList):
    for X in range(len(tempList)-1,0,-1):
        for i in range(X):
            if tempList[i]>tempList[i+1]:
                swap  = tempList[i]
                tempList[i] = tempList[i+1]
                tempList[i+1] = swap
    return tempList
  
