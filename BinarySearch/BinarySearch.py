class BinarySearch(object):
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
    newlist = self.binary_list
    var_len = self.variablelength
    
    first_index = 0
    last_index = var_len - 1
    midpoint = last_index//2
    count = 0
    
    if var_len == 0:
      return ("Empty List")
    else:
      midpoint = var_len//2
      while first_index < last_index:
        if newlist[midpoint] == value:
          dict['count'] = count 
          dict['index'] = midpoint
          return dict
        else:
          if value < newlist[midpoint]:
            last_index = midpoint -1
          else:
            first_index = midpoint -1
        count += 1 
      
    
