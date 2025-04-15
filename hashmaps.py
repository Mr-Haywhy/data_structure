# Introduction to Hashmaps
# A hashmap is a data structure that stores key-value pairs in a way that allows for efficient lookup, insertion, and deletion of elements.
            # key        value 
            #  |           |
            # {101, "Jacqueline"}
    
# A hashmap is a more advanced data structure that builds on top of a hash table to provide better performance and efficiency, especially in situations where collisions are common.

# To understand the benefits of hashmaps, let's explore why they're useful.

#............Why Use a Hashmap?.......................
# 1. Avoiding Collisions
# The primary advantage of hashmaps over traditional hash tables is that they can effectively avoid collisions, which reduces the likelihood of data loss or corruption.

# Hashmaps avoid collisions through techniques such as chaining, where multiple values are stored at the same index using data structures like linked lists or trees.

# 2. Faster Operations
# The use of linked lists or trees enables hashmaps to provide faster lookup, insertion, and deletion.

# In other words, hashmaps can efficiently manage and retrieve data, making them a popular choice for applications that require fast data access and manipulation.

# 3. Ability to Handle Large and Complex Datasets
# The ability of hashmaps to avoid collisions and provide fast data access makes them scalable and reliable, thus making them ideal for processing large and complex datasets.

# As a result, hashmaps are often the go-to data structure for applications such as databases, caching systems, and data processing pipelines, where data integrity and performance are critical.

#..............Working of a Hashmap
# Like every other map, hashmaps store data in key-value pairs.
            # key        value 
            #  |           |
            # {101, "Jacqueline"}

# What makes them more efficient is their implementation, which is accomplished with a combination of hash tables and linked lists.
    # The linked lists store keys and values, where each node in a linked list contains a key-value pair.
    # The hash table stores the indices of the linked lists, where each index points to the head of a linked list.

# Hash Table
    # 1
    # 2
    # 3
    # 4
    # 5 ----->{5,"MIra"}----->{18,"Paul"}
    # 6              (linked list)
    # 7
    # 8
    # 9
    # 10
    # 11
    # 12
    # 13

# As the image shows, each index of the hash table (potentially) points to the head of a corresponding linked list.

#...............Working: Inserting Into a Hashmap...........
# We can use any hash function to map keys to indices in the hash table.

# To insert a new key-value pair into the hashmap,
    # 1 We hash the key using the hash function to get the hash table index.
    # 2 Traverse the linked list at the resulting index of the hash table.
    # 3 Add a new node to the end of the list if the key is not already present.

# Say we have to insert a new key-value pair, {5, "Mira"}, into a hash table of size 13.


#...............Working: Inserting Into a Hashmap
# Let's proceed with inserting {5, "Mira"} into our hash table of size 13.

# Step 1: Hash the key to get the hash table index.

# We'll first get the hash of the key 5. For this example,

# We'll use a modular hash function, i.e., key % table_size.
# So, we get the hash value of 5 (5 % 13).
# Steps 2 and 3: Insert the key-value pair.

# Now, we'll use the hash value 5 as an index in the hash table.

# Currently, there's no linked list associated with this index. So, we insert {5, "Mira"} into a new linked list and connect it to the hash table at index 5.

            # Hash Table
                # 1
# {5,"MIra"}    # 2
    #   |       # 3
    #   |       # 4
#[5 % 13 = 5]   # 5 ----->{5,"MIra"}
                # 6              
                # 7
                # 8
                # 9
                # 10
                # 11
                # 12
                # 13


# Next, let's see how we deal with collisions by adding a new key-value pair at the same index.

#..............Working: Dealing with Collisions
# Now, we'll insert a new key-value pair: {"18", "Paul"}.

# 1. Get the hash of the key to get the hash table index.
    # Using the modular hash function, we get the hash value 5 (18 % 13). So, we'll store this key-value at index 5.

# 2. Traverse the linked list associated with the index.
    # The key-value pair {5, "Mira"} is already present at index 5 of the hash table. So, a collision occurs.

# 3. Resolve the collision by adding the pair as a new node in the linked list.
    # To resolve the collision, we add {"18", "Paul"} as the next node (after {5, "Mira"}) to the list with the key 5.


            # Hash Table
                # 1
#{18,"Paul"}    # 2
    #   |       # 3
    #   |       # 4
#[18 % 13 = 5]  # 5 ----->{5,"MIra"}---->{18, "Paul"}
                # 6              
                # 7
                # 8
                # 9
                # 10
                # 11
                # 12
                # 13


#..........Working: Fetching a Value From a Hashmap............
# To fetch a value from the hashmap,
    # 1 We hash the key using the hash function to find the index in the hash table.
    # 2 Traverse the linked list at the resulting index until you find the key.
    # 3 Return the value associated with the key.
# Next, we'll demonstrate this operation with an example.

# Let's say we have to fetch a value with a key 18.

# Step 1: Hash the key to find the hash table index.
#     We'll first get the hash of the key 18. Using the same hash function, we get the hash value of 5 (18 % 13).

# Step 2: Traverse the linked list at the index until the key is found.
#     We start traversing the list from the head at index 5 of the hash table. We then compare the keys until the key we are looking for is found.
# The head node doesn't have the key 18, so the match is not found.
# We therefore move to the next node, which is the node with the key 18. This is the required node, and the key is thus found.
# Step 3: Return the associated value.
#     Having found the required key (18), we can now return the value Paul.

# Next, we'll learn how to remove data from the hashmap.

# ......................Working: Removing Data From a Hashmap
# To remove a key-value pair from the hashmap,

# We hash the key using the same hash function to get the hash table index.
# Traverse the linked list at the resulting index.
# Remove the node containing the key-value pair if it is found.
# Let's say we have to remove a value with a key 18. Here's how we can implement the steps above:

# Step 1: Hash the key.
#     We'll first get the hash of the key 18. Using the same hash function, we get the hash value of 5 (18 % 13).

# Next, we'll implement steps 2 and 3.

# Step 2: Traverse the linked list at the resulting index.
#     We start traversing the list from the head at index 5 of the hash table. We then compare the keys until the key we are looking for is found.
# Here, the head node doesn't have the key 18, so the match is not found.

# We therefore move to the next node, which is the node with the key 18 (the one we're looking for).

# Step 3: Delete the key.

# Now, we delete the node from the associated list.


# ................Thought Process: Hashmap
# Now that we've learned how hashmaps work in theory, let's implement the data structure in Python.
# 1. Define a class to represent a key-value pair.
# Since a hashmap is all about key-value pairs, we'll define first a class KeyValuePair.

#         class KeyValuePair:
#             def __init__(self, key, value):
#                 self.key = key
#                 self.value = value

#             def __str__(self):
#                 return f"{self.key}:{self.value}"

# 2. Define a class to represent a hashmap.
# Next, we'll define the HashMap class, which will have the following components:

# A table_size member variable to define the size of the hash table.
# A doubly linked list of KeyValuePair objects.
# Various helper functions to perform insertion, lookup, and deletion.
# class HashMap:
#     def __init__(self):
#         # Initial table size
#         self.table_size = 128
#         # List of key-value pairs (buckets)
#         self.table = [[] for _ in range(self.table_size)]

#     def __str__(self):
#         map_str = ""
#         for i, bucket in enumerate(self.table):
#             if bucket:  # Only print non-empty buckets
#                 map_str += f"Bucket {i}: {', '.join(str(pair) for pair in bucket)}\n"
#         return map_str
# Internally, our hashmap uses a list, which is basically the Python implementation of a linked list.

# We'll define the helper functions a little bit later. For now, let's shift our focus to defining other crucial components.

# 3. Define the hash function.
# We'll use the modular hashing technique in our hash function:
#             # Hash function
#             def _hash(self, key):
#                 return key % self.table_size

# Our hash function takes in the key as an input parameter and returns key % table_size as the hash value.

# We'll use this hash as an index for lookup in the array.

# 4. Inserting into the hashmap.
# To insert a value into the hashmap,
#     * We generate a hash for the given key and use it as an index in the array.
#     * Next, we traverse the list of key-value pairs stored at that index.
#     * If we find an existing key that matches the one we're trying to insert, we simply update the associated value.
#     * If no matching key is found, we append the new key-value pair to the list, effectively adding it to the data structure.

#         # Insert a key-value pair into the hashmap
#         def insert(self, key, value):
#             index = self._hash(key)
#             for pair in self.table[index]:
#                 if pair.key == key:
#                     pair.value = value  # Update the value if key already exists
#                     return
#             # Insert new key-value pair
#             self.table[index].append(KeyValuePair(key, value))

# 5. Retrieving a value from the hashmap.
# To retrieve the value associated with a key,
#     * We generate a hash for the given key and use it as an index in the array.
#     * Next, we traverse the list of key-value pairs stored at that index.
#     * If we find a matching key in the list, we return the associated value.
#     *  Otherwise, we return None.
#         # Retrieve the value associated with a key
#         def get(self, key):
#             index = self._hash(key)
#             for pair in self.table[index]:
#                 if pair.key == key:
#                     return pair.value
#             return None  # If key is not found

# 6. Removing key-value pairs from the hashmap.
# To remove the value associated with a key,
#     * We generate a hash for the given key and use it as an index in the array.
#     * Next, we traverse the list of key-value pairs stored at that index.
#     * If we find a matching key in the list, we remove the associated value from the list.
#         # Remove a key-value pair from the hashmap
#         def remove(self, key):
#             index = self._hash(key)
#             for i, pair in enumerate(self.table[index]):
#                 if pair.key == key:
#                     del self.table[index][i]
#                     return


#.......................Source Code......................
class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return f"{self.key}:{self.value}"

class HashMap:
    def __init__(self):
        # Initial table size
        self.table_size = 128
        # List of key-value pairs (buckets)
        self.table = [[] for _ in range(self.table_size)]

    def __str__(self):
        map_str = ""
        for i, bucket in enumerate(self.table):
            if bucket:  # Only print non-empty buckets
                map_str += f"Bucket {i}: {', '.join(str(pair) for pair in bucket)}\n"
        return map_str

    # Hash function
    def _hash(self, key):
        return key % self.table_size

    # Insert a key-value pair into the hashmap
    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair.key == key:
                pair.value = value
                return
        # Insert new key-value pair
        self.table[index].append(KeyValuePair(key, value))

    # Retrieve the value associated with a key
    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair.key == key:
                return pair.value
        return None  # If key is not found

    # Remove a key-value pair from the hashmap
    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair.key == key:
                del self.table[index][i]
                return


# Create a hashmap instance
student_map = HashMap()

# Insert values into map
student_map.insert(1, "James")
student_map.insert(2, "Paul")
student_map.insert(3, "Mira")

# Add key that collides with existing key 1
student_map.insert(129, "Stuti")

# Retrieve values
print(f"Student with ID 1 is {student_map.get(1)}")
print(f"Student with ID 2 is {student_map.get(2)}")
print(f"Student with ID 3 is {student_map.get(3)}")
print(f"Student with ID 129 is {student_map.get(129)}")

# Remove student with ID 2
student_map.remove(2)

print("After removal")

# Attempting to get a removed student will return None
print(f"Student with ID 2 is {student_map.get(2)}")  # Should print None

print("Hashmap Contents")
print(student_map)