"""

First, you are to create a BinarySearch class, that inherits from the list class the following:

the __init__() takes two integers as parameters, a and b. a is the length of the list to be 
created and b is the step or difference between consecutive values. It should also initialize
 an instance variablelength`, that returns the number of elements in the array

Once you are done, create another method called search, it will take just one argument which 
is the value you are to find. The search function should return a dictionary object, which contains

count, the number of times you function iterated to find the index of the number in question index, 
the index of the number in question

The search method should implement the binary search algorithm, each time you iterate, 
you should increase the count, to test how efficient your implementation is.

"""

class BinarySearch():
  def __init__(self, a, b):
    if isinstance(a, str) and isinstance(a, int):
    
      binary_list = []
      list_length = 0
      while list_lengtht < a:
        binary_list.append(b)
        b += b
        list_length += 1
      self.variablelength = len(binary_list)
      
    else:
      raise TypeError("Arguments have to be intergers")
      
  def search(self, value):
    dict = {'count':'','index':''}
    count = 0
    newlist = self.binary_list
    var_len = self.variablelength
    
    if self.variablelength == 0:
      midpoint = self.variablelength//2
      if [midpoint] == value:
        dict['count'] = 0 
        dict['index'] = 0 
      else:
        if item < self[midpoint] :
          return
    
    else:
    
    dict{count} = no_iterations
    dict{index} = no_iterations - 1
    
