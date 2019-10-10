# -*- coding: utf-8 -*-
"""
Created on Fri May 10 13:20:38 2019

@author: bhuwan.madhikarmi
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = root
    
    def print_tree(self):
        self.print_inOrder( t1.root)
        return self.print_preorder(t1.root,"")[:-1]

    def print_inOrder(self,root):
        if root:            
            self.print_inOrder(root.left) 
            print(root.value, end = ",") 
            self.print_inOrder(root.right)   
    def print_preorder(self,root,traverse):
        if root:
            traverse +=(str(root.value)+"-")
            traverse = self.print_preorder(root.left,traverse)
            traverse = self.print_preorder(root.right,traverse)
        return traverse
# Set up tree
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

t1 = BinaryTree(n1)
t1.root.left = n2
t1.root.right = n3
t1.root.left.left = n4
t1.root.left.right = n5
t1.root.left.left.left = n6

t1.print_tree()

#t1.printTree(t1.root)



tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
#tree.root.left.right = Node(5)
tree.printTree(tree.root)

class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key
def printInorder(root):   
    if root: 
        printInorder(root.left) 
        print(root.val), 
        printInorder(root.right)   
# Driver code 
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 
printInorder(root) 
       
        