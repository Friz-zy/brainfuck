#!/usr/bin/python
# coding=utf-8
"""
Copyright (c) by Filipp Kucheryavy aka Frizzy <filipp.s.frizzy@gmail.com>
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:

a. Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer. 

b. Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution. 

c. Neither the name of the nor the names of its contributors may be used to endorse or promote 
products derived from this software without specific prior written permission. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS 
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY 
AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE 
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

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