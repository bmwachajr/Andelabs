"""
You are presented with two arrays, all containing positive integers. 
One of the arrays will have one extra number, see below:

[1,2,3] and [1,2,3,4] should return 4

[4,66,7] and [66,77,7,4] should return 77

"""

def find_missing(array1, array2):
  if len(array1) == len(array2):
    return 0
  else:
    if len(array1) > len(array2) :
      for number in array1:
        if number not in array2:
          return number
    else:
      for number in array2:
        if number not in array1:
          return number