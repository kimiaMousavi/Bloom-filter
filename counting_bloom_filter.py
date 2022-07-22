import math
from fnvhash import fnv1a_32
from bitarray import bitarray
from bitarray.util import ba2int,int2ba

class counting_bloom_filter():
  def __init__(self, n,Counter_size,bucket_size,no_hashfn):

    self.n=n
    self.N=Counter_size
    self.m=bucket_size
    self.k=no_hashfn

    self.bit_array = []
    for i in range(self.m):
      count=bitarray(self.N)
      count.setall(0)
      self.bit_array.append(count)

  def hash(self,item,seed):
    return fnv1a_32(item.encode(),seed) % self.m
    

  def add(self, item):

    for i in range(self.k):
      index = self.hash(item,i)

      cur_val=ba2int(self.bit_array[index])
      new_array=int2ba(cur_val+1,length=self.N)
      
      self.bit_array[index]=new_array
  def check(self, item):
    for i in range(self.k):
      index = self.hash(item,i)
      cur_val=ba2int(self.bit_array[index])

      if(not cur_val>0):
        return False
    
    return (True , cur_val)
  
  def remove(self,item):
    if(self.check(item)):
      for i in range(self.k):
        index = self.hash(item,i)
        
        cur_val=ba2int(self.bit_array[index])
        new_array=int2ba(cur_val-1,length=self.N)
        self.bit_array[index]=new_array

      print('Element Removed')
    else:
      print('Element is probably not exist')

