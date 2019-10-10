# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:32:09 2019

@author: bhuwan.madhikarmi
"""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""        
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""        
        hv = self.calculate_hash_value(string)
#        print("hash:"+str(hv))
        if hv != -1:
#            print("not minus 1")
            if self.table[hv] != None:
#                print("manual print self.table[hv]"+str(self.table[hv]))
                if string in self.table[hv]:
                    return hv
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""        
        value = ord(string[0])*100 + ord(string[1])
        return value
    def print_table(self):
        for row_num in range (len(self.table)):
            if self.table[row_num] != None:
                print(str(row_num) + ":" +str(self.table[row_num]))
        
        
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print (hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print (hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print (hash_table.lookup('UDACITY'))

# Test store
hash_table.store('VODACITY')
# Should be 8568
print (hash_table.lookup('VODACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print (hash_table.lookup('UDACIOUS'))

hash_table.print_table()