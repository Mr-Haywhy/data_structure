# .................Retrieve Value from a Hash Table................
# We have this hash table from our last example:

#         0: None
#         1: None
#         2: 12
#         3: None
#         4: 4
#         5: 15
#         6: 14
#         7: 17
#         8: 27
#         9: 37
# Suppose we need to find an item (let's say 27) from this hash table. Here's how we can achieve it:

#     Apply the hash function to find the hash value. For the key 27, the hash is 7.
#     Then, look into the hash table with this hash. The key with hash 7 is 17.
#     Then, we move on to the next index. The key at slot 8 is 27.
# Suppose we need to find another item (let's say 13) from this hash table. Here's how we can achieve it:

#     Apply the hash function to find the hash value. For key 13, the hash is 3.
#     Then, look into the hash table with this hash. There is no key with hash 3.
# Thus, the retrieval function linearly searches the hash table until the key is found or an empty slot is found.

# Let's add a method to implement this in our code and see how it works next.

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
    
    # retrieve data from hash table
    def retrieve(self, key):
        hash_value = self.hash_function(key)
        i = 0
         # continue searching until an empty slot is found
        while self.table[hash_value]:
             # uf the required key is found, return its hash value and key
            if self.table[hash_value] == key:
                return {"hash_value": hash_value, "key": key}
            # move to next slot
            i += 1
            hash_value = (self.hash_function(key) + i) % 10
            
        # if key not in table, return None
        return {"hash_value": hash_value, "key": None}

# keys
keys = [12, 17, 15, 4, 27, 14, 37]

hash1 = HashData()

# apply hash function to each key
for key in keys:
    hash1.put(key)

print(hash1.retrieve(27))
print(hash1.retrieve(13))



# ..................Limitations of Linear Probing
# While linear probing offers a simple approach to handle hash collisions, it comes with the following limitations:

# 1. Difficulty in deleting values
# In order to delete an item after linear probing, we need to take out all other elements and rehash them again. This is not very feasible.
# Thus, we don't implement deletion operations at all from linear probing.

# 2. Primary clustering
# Every time a collision happens, the position of the item is shifted one position down. When there are a lot of collisions around a small area, the position of items can shift a lot.
# In such cases, the hash table may no longer provide constant time search operations. This is known as primary clustering.
# To address the primary clustering problem, we use quadratic probing.

