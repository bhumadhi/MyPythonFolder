# -*- coding: utf-8 -*-
"""
Created on Mon May  6 08:45:20 2019

@author: bhuwan.madhikarmi
"""

"""
Recursion is a way of programming or coding a problem, in which a function calls itself one or more times in its body.
A recursive function has to terminate to be used in a program. A recursive function terminates, 
if with every recursive call the solution of the problem is downsized and moves towards a base case. A base case is a case, 
where the problem can be solved without further recursion. A recursion can lead to an infinite loop, if the base case is not met in the calls. 
Recursion in computer science is a method where the solution to a problem is based on solving smaller instances of the same problem. 
"""


    
class factorial(object):
#    def __init__(self,number):
#        self.number = number
    def factorial(self,number):
        self.number = number
        if self.number == 1:
            return 1
        else:
            result = self.number * self.factorial(self.number-1)
            return result
        
def main():
    fac = factorial()
    print(fac.factorial(5))
    
if __name__ == "__main__":
    main()
#accepted solution 1 
class Fac(object):
    def __init__(self,number):
        self.number = number
    def fac(self):
        if self.number == 1:
            return 1
        else:
            result = self.number * Fac(self.number-1).fac()
            return result
        
def main():
    fac = Fac(5)
    print(fac.fac())
    
if __name__ == "__main__":
    main()    
    
    
#####################################
#**self.number -= 1**

class factorial2(object):
    def __init__(self,number):
        self.number = number
    def factorial2(self):
      if self.number == 0:
        return 1 
      else:
        temp_n = self.number
        self.number -= 1
        return temp_n * self.factorial()
def main():
    fac = factorial2(5)
    print(fac.factorial2())

if __name__ == "__main__":
  main()
###################################
  #accepted solution 2
def factorial3(number):
    if number == 1:
        return 1
    else:
        result = number * factorial3(number-1)
        return result  
print(factorial3(5))  

##################################
