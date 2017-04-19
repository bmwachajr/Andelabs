"""

Name : Min Max app
Author: Benjamin Wacha
Email: bmwachajr
Disc: A python app that that returns the min and max number from a list.

"""

def find_max_min(list):
  max_min = []
  
  list.sort()
  min = list[0]
  max = list[-1]
  
  if(min == max):
    max_min.append(len(list))
    return (max_min)
  else:
    max_min.append(min)
    max_min.append(max)
    return (max_min)
  
