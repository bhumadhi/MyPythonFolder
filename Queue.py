# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:39:48 2019

@author: bhuwan.madhikarmi
"""

"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
class Queue(object):
    def __init__(self, head=None):
        self.head = head

    def enqueue(self, new_element):
        current = self.head
        print("new_element: "+str(new_element.value))
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def peek(self):
        print (self.head.value)

    def dequeue(self):
        delete_head = self.head
        temp = self.head.next
        self.head = temp
        print(delete_head.value)
    
    def get_list(self):
        current = self.head
        if self.head:            
            while current.next:
                print(current.value)
                current = current.next
            print(current.value)                
        else:
            return None
   
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)

q1 = Queue(e1)
q1.peek()
q1.get_list()
q1.enqueue(e2)
q1.get_list()
q1.enqueue(e3)
q1.enqueue(e4)
q1.get_list()
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print (q.peek())

# Test dequeue
# Should be 1
print (q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print (q.dequeue())
# Should be 3
print (q.dequeue())
# Should be 4
print (q.dequeue())
q.enqueue(5)
# Should be 5
print (q.peek())