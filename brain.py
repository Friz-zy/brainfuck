#!/usr/bin/env python3

# write by Filipp Frizzy <filipp.s.frizzy@gmail.com> and google translate

def brain(n, code):
  program=[]
  memory=[0]*int(n)
  i=0 # number of the current cell
  j=0 # number of char in code
  out = '' # str to output
  open_b=[]
  close_b=[]

  for ch in code:	# string in list of characters
    program.append(ch)
  while j < len(program):	# find all brackets
    if program[j] == '[':
      open_b.append(j)
    if program[j] == ']':
      close_b.append(j)
    j+=1
  j=0
  while j < len(program):
    c = program[j]
    if c == '>':   #next bit
      if i == n:
        i = 0
      else:
        i+=1
      
    if c == '<':   #previous bit
      if i == 0:
        i = n
      else:
        i-=1
      
    if c == '+':   #increase in value in the current memory cell
      memory[i]+=1 
  
    if c == '-':   #decrease in value in the current memory cell
      if memory[i] > 0:
        memory[i]-=1
      
    if c == '.':   #the output value of the current cell
      out += chr(memory[i])
      
    if c == ',':   #input values ​​and safe in the current cell
      memory[i] = input('write something')
    
    if c == '[':	 #if current cell = 0: go to ]
      if memory[i] == 0:
        ob = open_b.index(j)
        cb = close_b[ob]
        j = cb
      
    if c == ']':	 #if current cell != 0: go to [
      if memory[i] != 0:
        cb = close_b.index(j)
        ob = open_b[cb]
        j = ob
     
    j+=1
 
  return out	 # output resalt