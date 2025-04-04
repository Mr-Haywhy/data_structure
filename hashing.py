# #.......................Hashing.............................#
# Hashing is the process of transforming data, such as text, numbers, and files, into a unique string of characters and numbers.
# The data we are trying to convert is referred to as a key.
# The string we get after hashing is known as a hash value or hash code.

# .........................Hash function........................
# The function used to convert keys into hash values is called a hash function.

# Let's start with a simple example of a hash function:

#         H(x) = x mod 5
# Here:
#     1. x is the key
#     2. H(x) is the hash function, which gives the remainder when x is divided by 5.

# Suppose we have these keys: 2, 9, 10.
#     * The hash value of 2 will be 2.
#     * The hash value of 9 will be 4.
#     * The hash value of 10 will be 0.

# In hashing, we create a hash table (a data structure) to store keys and their respective hash values.

# ........................Hash Table...........................
# Here's what a hash table looks like for the previous example.

#             Hash Value  | Key
#                 0       | 10
#                 1       |
#                 2       | 2
#                 3       |
#                 4       | 9

# Our function H(x) = x mod 5 creates unique hash values for 10, 2, and 9 keys.

# However, it might not create unique hash values for a different set of keys. We will learn to handle this problem later in this chapter.

# For now, let's examine another example of hashing.

# ........................Example: Hashing....................
# In this example, we will hash a set of strings based on the ASCII value of their first character.

# ASCII is the numerical representation of characters. The ASCII value of 'A' is 65, 'B' is 66, 'C' is 67, and so on.

# Consider we have these keys: "Apple", "Cactus", "Grasshopper" and "Iron".

# We will use this hash function, H(x) = ASCII(x[0]) - 64, for hashing.

# In this case, our hash table will look like this:

#         1   |   Apple
#         2   |
#         3   |   Cactus
#         4   |   
#         5   |
#         6   |
#         7   |   Grasshopper
#         8   |
#         9   |   Iron

# In this example, each key is mapped to a value equal to the alphabetic position of their first letter.

# Here, the hash function is H(x) = ASCII(x[0]) - 64.

# .....................Why Hashing........................
# Hashing is utilized in computing for various applications. Two of the commonly used applications are:

# 1. Searching

# Hashing is used to retrieve data efficiently. By using hashing, we can create a unique index for each value (key).

# Now, if we have to search for a value, we can use this unique index instead of the value itself. This approach results in a constant time complexity, O(1).

# 2. Security

# In general, passwords should not be stored in plain text because if the database is compromised, the password will be exposed.

# Instead, passwords are hashed before being stored in a database. This way, even if the database is hacked, your password remains secure.

# ........................Hashing Techniques......................
# In the last lesson, one of the hash functions we used was 
#     H(x) = x mod 5.

# This function uses modulus (remainder when divided by a number) to compute a key's hash value, a technique known as modular hashing.

# Modular hashing ensures that the hash values are distributed within a fixed range. For example,

# Suppose we have this hash function H(x) = x mod 10. Let's examine its hash table for keys 1005, 12, 7, 99999, 4556, and 7838.

# Hash Values |   Key
#     0       |   
#     1       |   
#     2       |   12
#     3       |      
#     4       |
#     5       |   1005
#     6       |   4556
#     7       |   7
#     8       |   7838
#     9       |   99999

# As you can see, the hash values for this function will be in a fixed range, 0 to 9, no matter how large the number is. This helps to utilize the hash table space efficiently.
      

# ...............Thought Process: Modular Hashing...............
# Now, let's learn to implement hashing in our code.

# Suppose we have this hash function H(x) = x mod 10. Here are the steps to implement it:

# 1. Create a list to store hash values.

# Since this hash function gives hash values between 0 and 9, we will initialize a list of 10 elements.

#             # a list of ten elements
#             # all elements are initialized to None
#             table = [None] * 10

# NOTE: The values stored in the table will be keys, and their indexes will represent the hash values.
# 2. Find the hash of a key.

#             hash_value = key % 10

# 3. Insert data into the hash table.

#             table[hash_value] = key

# 4. Repeat steps 2 and 3 for all the keys to populate the hash table.

# After we perform these steps, we will get a hash table where:
#     * the elements represent the keys,
#     * their indexes represent the hash values.