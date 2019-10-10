# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:11:02 2019

@author: bhuwan.madhikarmi
"""

class node:
    def __init__(self,value):
        self.value = value
        self.next = None
class linked_list:
    def __init__(self,head=None):
        self.head = head
    def insert(self, node):
        cur = self.head
        print("cur.value :"+str(cur.value))
        print("cur.nex t:"+str(cur.next))
        if self.head:
            print("inside the if")
            while cur.next:
                print("inside the while")
                cur = cur.next
            cur.next = node
        else:
            self.head = node
n1 = node(1)
#print("n1.value:" + str(n1.value))
#print("n1.next:" + str(n1.next))
n2 = node(2)
#print("n2.value:"+str(n2.value))
#print("n2.next:"+str(n2.next)  )      
n3=node(3)
l1 = linked_list(n1)

l1.insert(n2)
l1.insert(n3)
print("l1.value:"+str(l1.head.value))
print("l1.next:"+str(l1.head.next.value) ) 

print("l1.value:"+str(l1.next.value))
print("l1.next:"+str(l1.next.next))
