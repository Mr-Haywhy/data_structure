
#..................Quadratic Probing..................#
# When collisions happen, quadratic probing searches for the next available slot by using a quadratic term, like i^2, to place items farther apart compared to linear probing.

# Here, instead of probing by i, we probe by i ** 2.

#.......................Thought Process: Quadratic Probing.............#
# Implementing quadratic probing is straightforward; instead of using a linear increment for the probing index, you use a quadratic increment (i^2).

# The put() method becomes:
        ## insert data to hash table
        # def put(self, key):
        #     i = 0
        #     hash_value = self.hash_function(key)
        #     while self.table[hash_value]:
        #         i += 1
        #         hash_value = (self.hash_function(key) + i**2) % 10 # use i ** 2
        #     self.table[hash_value] = key 

# Similarly, the retrieve() method becomes:
## retrieve data from hash table
        # def retrieve(self, key):
        #     hash_value = self.hash_function(key)
        #     i = 0
        #     while self.table[hash_value]:
        #         if self.table[hash_value] == key:
        #             return {"hash_value": hash_value, "key": key}
        #         i += 1
        #         hash_value = (self.hash_function(key) + i**2) % 10 # use i ** 2
        #     return {"hash_value": hash_value, "key": None}  


#..................Source Code: Quadratic Probing...............#
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
            i += 1
            hash_value = (self.hash_function(key) + i**2) % 10 # use i ** 2
        self.table[hash_value] = key   
    
    # display hash table
    def display(self):
        for hash_value, key in enumerate(self.table):
            print(f"{hash_value}: {key}")    
    
    # retrieve data from hash table
    def retrieve(self, key):
        hash_value = self.hash_function(key)
        i = 0
        while self.table[hash_value]:
            if self.table[hash_value] == key:
                return {"hash_value": hash_value, "key": key}
            i += 1
            hash_value = (self.hash_function(key) + i**2) % 10 # use i ** 2
        return {"hash_value": hash_value, "key": None}

# keys
keys = [12, 17, 15, 4, 27, 14, 37]

hash1 = HashData()

# apply hash function to each key
for key in keys:
    hash1.put(key)
    
hash1.display()

print()
print("Retrieving Values: ")

print(hash1.retrieve(27))
print(hash1.retrieve(13))



#.................Limitations of Quadratic ..................#
# While quadratic probing does address _primary_clustering_ better than linear probing, it still faces challenges.
# The deletion operation still remains_complex.
# Additionally, quadratic probing introduces the_possibility_of_secondary_clustering_, where items still cluster together despite using the quadratic increment.
# In the next topic, we will explore _double_hashing_ as a_collision_resolution_technique_, which aims to further improve upon the limitations of linear and quadratic probing.