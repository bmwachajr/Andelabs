class BinarySearch(list):
  def __init__(self, a, b):
    binary_list = []
    binary_list.append(b)
    list_length = 1
    
    while list_length < a:
      binary_list.append(binary_list[list_length -1] + b)
      list_length += 1
      
    super(BinarySearch,self).__init__(binary_list)
    self.length = len(binary_list)
      
  def search(self, value):
    dict = {'count':'','index':''}

    self.length = len(self)
    
    first_index = 0
    last_index = self.length - 1
    midpoint = int((last_index)/2)
    count = 0
    
    if self.length == 0:
      return ("Empty List")
    else:
      while first_index < midpoint:
        if self[midpoint] == value:
          dict['count'] = count 
          dict['index'] = midpoint
          return dict
          
        elif self[first_index] == value:
          dict["count"] = count
          dict["index"] = first_index
          return dict
          
        elif self[last_index] == value:
          dict["count"] = count
          dict["index"] = last_index
          return dict
          
        elif self[first_index] == value:
          
          if value < self[midpoint]:
            last_index = midpoint -1
          else:
            first_index = midpoint -1
            
        elif (first_index == midpoint) and (self[first_index] > value):
          dict["count"] = self.length
          dict["index"] = 0
          return dict
          
        else:
          if self[midpoint] > value:
            last_index = midpoint - 1
            first_index += 1
            midpoint = (first_index + last_index)//2
          else:
            first_index = midpoint + 1
            last_index = last_index - 1
            midpoint = ((last_index + first_index)//2) + 1
        count += 1
      dict = {'count':count,'index':-1}	
      return dict
        
      
