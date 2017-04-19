"""

Name : Word Count
Author: Benjamin Wacha
Email: bmwachajr
Disc: A python app that counts the occurrence of a word in a string

"""

def words(string):
  dict = {}
  list = string.split()
  list.sort()
  
  for word in list:
    if word.isdigit():
      word = int(word)
    if word in dict:
      dict[word] = dict[word] + 1
    else:
      dict[word] = 1
  
  return (dict)    
