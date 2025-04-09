# Introduction to Hashmaps
# A hashmap is a data structure that stores key-value pairs in a way that allows for efficient lookup, insertion, and deletion of elements.
            # key        value 
            #  |           |
            # {101, "Jacqueline"}
    
# A hashmap is a more advanced data structure that builds on top of a hash table to provide better performance and efficiency, especially in situations where collisions are common.

# To understand the benefits of hashmaps, let's explore why they're useful.

#............Why Use a Hashmap?
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