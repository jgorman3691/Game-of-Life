#! python3

import numpy as np
import scipy as sp
import itertools as it
import board as bd

class EdgeIterator:
   def __init__(self, topology):
      self._topology = topology
      self._xindex = 0
      self._yindex = 0
      self.universe = topology.universe
      self.A = topology.A
      self.B = topology.B
      self.x = topology.x
      self.y = topology.y
      self.height = topology.height
      self.width = topology.width
      self.top = topology.setEdges().top
      self.bottom = topology.setEdges().bottom
      self.left = topology.setEdges().left
      self.right = topology.setEdges().right

   def __next__(self):
      if self.A == 0 and self.B == 0:
         return self.universe
      elif self.A == 1:
         return self.top, self.bottom
      elif self.B == 1:
         return self.right, self.left
      elif self.A == 1 and self.B == 1:
         return self.top, self.bottom, self.right, self.left
      raise StopIteration


class Topology:

   def __init__(self, universe, height, width, A, B, x, y):
      self.universe() = np.array(universe)
      self.height = height
      self.width = width
      self.A = A
      self.B = B
      self.x = x
      self.y = y
      self.c = 0
      self.d = 0

   def setEdges(self, universe, height, width):
      self.top = self.universe([0:self.width,self.height:self.height][,::1], axis=0)
      self.bottom = self.universe([0:self.width,0:0][,::-1],axis=0)
      self.left = self.universe([0:0,0:self.height][::-1,],axis=1)
      self.right = self.universe([self.width:self.width,0:self.height][::1,],axis=1)

   def __iter__(self):
      return EdgeIterator(self)