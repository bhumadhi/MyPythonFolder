# -*- coding: utf-8 -*-
"""
Created on Fri May  3 08:32:17 2019

@author: bhuwan.madhikarmi
"""

class Element(object):
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head_element=None):
        self.head_element = head_element

    def insert_first(self, new_element):
        new_element.next = self.head_element
        self.head_element = new_element
    
    def delete_first(self):
        if self.head_element:
            deleted_element = self.head_element #first element
            temp = deleted_element.next #2nd element
            self.head_element = temp
            return deleted_element
        else:
            return None
    def get_list(self):
        current = self.head_element
        if self.head_element:
            while current.next: # this will print upto 2nd last
                print(current.value)
                current = current.next
            print(current.value) # to print the last one
        else:
            return None
        
    
class Stack(object):
    def __init__(self, top_element):
        self.L1 = LinkedList(top_element)
    
    def push(self, new_element):
        self.L1.insert_first(new_element)
    
    def pop(self):
        return self.L1.delete_first()
    
    def print_stack(self):
        return self.L1.get_list()

        
#test cases
#create elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

#set up stack
s1 = Stack(e1)

#test stack functionality
s1.push(e2)
s1.push(e3)
#print(s1.pop().value)
s1.print_stack()