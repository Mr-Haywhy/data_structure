# ..................Retrieve Value from a Hash Table........................
# We have this hash table from our last example:

#         0: 300
#         1: 1
#         2: 12
#         3: None
#         4: None
#         5: None
#         6: None
#         7: 117
#         8: None
#         9: 209
# Suppose we need to find an item (let's say 117) from this hash table. Here's how we can achieve it:

# Apply the hash function to find the hash value. For the key 117, the hash is 7.
# Then, look into the hash table with this hash. The key with hash 7 is 117.
# Let's add a method to implement this in our code and see how it works next.

#         # retrieve key from hash table
#         def retrieve(self, item):

#             hash_value = self.hash_function(item)
        
#             # return key from the hash table
#             key = self.table[hash_value]

#             return {"hash_value": hash_value, "key": key}


#......................Source Code: Retrieve Value..................#
class HashData:

    # initialize a list of 10 items
    def __init__(self):
        self.table = [None] * 10

    # compute hash
    def hash_function(self, key):
        return key % 10

    # insert data to hash table
    def put(self, key):

        hash_value = self.hash_function(key)
        self.table[hash_value] = key

    # retrieve key from hash table
    def retrieve(self, item):

        hash_value = self.hash_function(item)
        key = self.table[hash_value]

        return {"hash_value": hash_value, "key": key}
            
keys = [1, 300, 209, 117, 12]

hash1 = HashData()

# apply hash function to each key
for key in keys:
    hash1.put(key)

# retrieve values
print(hash1.retrieve(117))
print(hash1.retrieve(13))