# .................Open Addressing...........................
# Open addressing resolves collisions by finding alternative locations within the existing hash table for collided elements.

# We will explore three open addressing methods in this lesson:
#     *Linear Probing
#     *Quadratic Probing
#     *Double Hashing

# .......................Linear Probing.........................#
# When a collision occurs, linear probing searches for the next available slot in the hash table, moving linearly until an empty slot is found.
# The objective is to find the closest unoccupied position for the colliding item.

#.................Working of Linear Probing................
# Consider the hash function: H(x) = x mod 10 and the following keys 12, 17, 15, 4, 27, 14, and 37.

# Hash Values   |   Key
    # 0         |   
    # 1         |   
    # 2         |   12
    # 3         |   
    # 4         |   4   <------14
    # 5         |   15
    # 6         |   
    # 7         |   17    <----27  <----37
    # 8         |   
    # 9         |   

# The linear probing technique resolves these collisions by inserting these keys into the next empty slot.
# Hash Values   |   Key
    # 0         |   
    # 1         |   
    # 2         |   12
    # 3         |   
    # 4         |   4 
    # 5         |   15
    # 6         |   14
    # 7         |   17
    # 8         |   27
    # 9         |   37

    # *Key 14 maps to slot 4(occupied), so it moves to the next empty slot(slot 6 since slot 5 is also occupied).
    # *Key 27 maps to slot 7(occupied), so it moves to the next empty slot(slot 8).
    # *Similarly, key 37 moves to slot 9.

#...................Thought Process: Linear Probing
# The insertion process in linear probing can be broken down into two main steps:

# *Attempt to insert the value at its corresponding key.
# *If the key is already occupied, probe to the next index.
# Here's how it can be implemented in Python:
# 
# .............insert data to hash table............

        # def put(self, key):
        #     i = 0
        #     hash_value = self.hash_function(key)
        #     while self.table[hash_value]:
        #         # move to next slot until empty space is found
        #         i += 1
        #         hash_value = (self.hash_function(key) + i) % 10
        #     # insert into empty slot
        #     self.table[hash_value] = key


class HashData:

    # initialize a list of 10 items
    def __init__(self):
        self.table = [None] * 10

    # compute hash
    def hash_function(self, key):
        return (key) % 10

    # insert data to hash table
    def put(self, key):
        i = 0
        hash_value = self.hash_function(key)
        while self.table[hash_value]:
            # move to next slot until empty space is found
            i += 1
            hash_value = (self.hash_function(key) + i) % 10
        # insert into empty slot
        self.table[hash_value] = key 
    
    # display hash table
    def display(self):
        for hash_value, key in enumerate(self.table):
            print(f"{hash_value}: {key}")    

            
# keys
keys = [12, 17, 15, 4, 27, 14, 37]

hash1 = HashData()

# apply hash function to each key
for key in keys:
    hash1.put(key)

hash1.display()