#! python3
import numpy as np
import scipy as sp
import scikit-learn
import board as bd

class Cell:

   def __init__(self, x=None, y=None, alive=None, dead=None, bd.universe):
      self.x = x
      self.y = y
      self.alive = True
      self.dead = False
      self.amount = 0
      self.universe = bd.universe

   def state(self, universe, x, y):
      self.universe = universe
      self.x = x
      self.y = y
      if self.universe[self.x,self.y] == True:
         return self.alive
      elif self.universe[self.x,self.y] == False:
         return self.dead
      else:
         return print("Incorrect state")

   def neighbors(self, x, y, universe):
      self.m = x
      self.n = y
      self.universe = universe
      self.amount = 0
      self.i, self.j = self.m, self.n
      for self.i in range(self.i-1:self.i+2):
         for self.j in range(self.j-1:self.j+2):
            if self.universe[self.i,self.j] == True:
               self.amount = self.amount + 1
      return self.amount
   
   def nextStep(self, amount):
      self.amount = amount
      if(self.universe[self.x,self.y] == True):
         if(self.amount == 2 or self.amount == 3):
            return self.universe[self.x,self.y] = True
         else:
            return self.universe[self.x,self.y] = False
      elif(self.universe[self.x,self.y] == False):
         if(self.amount == 3):
            return self.universe[self.x,self.y] = True
         else:
            return self.universe[self.x,self.y] = False
      
      return self.universe[self.x,self.y] = False