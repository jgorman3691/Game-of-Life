#! python3
import numpy as np
import torch
import torn.nn as nn

class Board:

   def __init__(self, height, width, A=None, B=None):
      self.height = height
      self.width = width
      self.A = 0
      self.B = 0
      self.x = 0
      self.y = 0
      self.near = []
      self.universe = []
      self.top = []
      self.side = []
      
   def background(self):
      self.universe = np.zeros((self.width,self.height ), dtype=int)
      return self.universe

#   def connected(self, universe=None, A=0, B=0):
#      pass
#      top = [0 for n in range(width)]
#      if A = 0 and B = 0:
#         break
#      elif A = -1 and B = 0:
#         top[::-1]
#         map(lambda x, y: y)
#         return universe
#
#      side = [0 for m in range(height)] 

   def location(self):
      return self.universe[self.x, self.y]
   
   def topology(self, universe, height, width, A, B, x, y):
      self.universe = universe
      self.A = A
      self.B = B
      for A in range(-1, 2, 1):


   def setPosition(self, x=None, y=None):
      self.x = x
      self.y = y
      if(x == None or y == None):
         return [self.x][self.y]
      elif(x != None):
         self.x = x
         return [self.x][self.y]
      elif(y != None):
         self.y = y
         return [self.x][self.y]
      else:
         self.x = x
         self.y = y
         return [self.x][self.y]

   def view(self,universe):
      return print('\n'.join([str(view) for view in universe]))

   def neighbor(self, x, y):
      i, j =  x, y
      if((0 < x < width-1) and (0 < y < height-1)):
         self.near = [[i for i in range(i-1,i+2,1)] for j in range(j-1,j+2,1)]
         self.near.delete([i][j])
      return self.near