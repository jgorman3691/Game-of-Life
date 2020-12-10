#! python3

import numpy as np
import itertools as it

class Topology:
   
   def __init__(self, universe, height, width, A, B, x, y):
      self.universe = universe
      self.height = height
      self.width = width
      self.A = A
      self.B = B
      self.x = x
      self.y = y
      self.c = 0
      self.d = 0
      self.top = self.universe([,self.height:self.height][,::1], axis=0)
      self.bottom = self.universe([0:self.width,0:0][,::-1],axis=0)
      self.left = self.universe([0:0,0:self.height][::-1,],axis=1)
      self.right = self.universe([self.width:self.width:0,0:self.height][::1,],axis=1)
      
   def __iter__(self):
      # self.top = self.universe([0:self.width:1,self.height:self.height:0][,::1],axis=0)
      # self.bottom = self.universe([0:self.width:1,0:0:0][,::-1],axis=0)
      # self.left = self.universe([0:0:0,0:self.height:1][::-1,],axis=1)
      # self.right = self.universe([self.width:self.width:0,0:self.height:1][::1,],axis=1)
      yield self
   
   def __next__(self):
      if self.A == 0 and self.B == 0:
         return self.universe
      if self.A == 1:
         if self.row == self.row[0] or self.row == self.row[-1]:
            self.row[0] = 
            self.row[height] = self.row[0]
      if self.B == 1:
         if self.column == self.column[self.d] or self.column == self.column[-1]:
            self.column[d-1] = self.column[-1]
            self.column[width] = self.column[0]