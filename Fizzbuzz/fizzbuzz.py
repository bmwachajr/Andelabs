"""

File      : fizzbuzz.py
Date      : April 18 2017
Author(s) : Benjamin Wacha <bmwachajr@gmail.com>
Desc      : fizz_buzz lab

"""
def fizz_buzz(arg):
  if isinstance(arg, int):
    if (arg % 3 == 0 ) and (arg % 5 == 0 ):
      return "FizzBuzz"
    if (arg % 3 ==0 ):
      return "Fizz"
    if (arg % 5 ==0 ):
      return "Buzz"
    else:
      return arg
  else:
    raise ValueError("Argument has to be an integer")
