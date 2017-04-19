"""

Name : Word Count
Author: Benjamin Wacha
Email: bmwachajr
Disc: A python app that counts the occurrence of a word in a string

"""

def word_count(string):
  dict = {}
  list = string.split()
  list.sort()
  print (list)
  for word in list:
    if word in dict:
      dict[word] = dict[word] + 1
    else:
      dict[word] = 1
  
  print (dict)    
  
  
string = "testing testing 1 2 testing"
word_count(string)