# Introduction
# In all of our previous examples, we have selected keys so that the hash values are always unique.

# Now, let's see an example where hash values are not unique.

# Hash Function: H(x) = x % 10
# Keys: [11, 12, 6, 22, 6]

# In this case, the first three values can be entered into the hash table without any issues.

# # However, the fourth value, 22, causes a problem because its hash value is also 2.
# If two keys map to the same hash value, a collision occurs. This can lead to data loss or corruption.

# .......................Hash Collision Resolution...............
# There are several strategies we can use to avoid collision:
# 1. Using a larger hash table
    # If we use a larger hash table, we can accommodate more values without clashing.
# 2. Modifying the hash function itself.
    # We can modify the hash function itself to ensure that the hash values are unique.

# .......................Load Factor.........................
# Before we learn how to avoid collisions, we need to understand the load factor.
# The load factor is a measure of how full the hash table is.

# It is calculated as:
    # Load Factor (LF) = Number of items stored / Total Number of Slots 
# A load factor value close to 1 indicates that the hash table is nearly full.
# Similarly, a load factor close to 0 indicates that the hash table is nearly empty.
# Let's illustrate this concept using a hash table.

# 0 | 5
# 1 | 15
# 2 | 25
# 3 | 35
# 4 | 45
# 5 | 55
# 6 | 65
# 7 |
# 8 | 85
# 9 |

# In this example, our hash table has 10 available slots and 8 elements stored in it. Hence, the load factor is:
        # LF = 8 / 10 = 0.8

# The load factor of 0.8 indicates that the hash table is nearly full.

# .....................Good Load Factor......................
# The load factor shouldn't be too high or too low.

# If the load factor is very low, there is less chance of a collision. However, it also means there are many unused slots, making hashing inefficient.
# If the load factor is very high, hashing will be efficient, but there will be a chance of collisions.

# So, what is the ideal load factor?
# There is no hard and fast rule for the ideal load factor. Generally, the load factor around 0.7 - 0.75 is considered good.

# .....................Rehashing..................
# Rehashing means creating a new hash table with an increased size.

# We generally use rehashing if the load factor is greater than a certain value (let's say 0.75). This helps to optimize the hash table's performance.

# ....................Working of Rehashing................
# Suppose we are using the H(x) = x % 10 function to hash items. Let's assume the load factor threshold is 0.75.

#..........Hashing seven elements or less...........
# If we need to hash seven or fewer elements, the load factor threshold will not trigger.
# In this case, we don't need to create a new hash table.

#..........Hashing eight elements or more...........
# If we need to hash more than eight or more elements, the load factor threshold will be triggered.
# In this case, we create a new hash table.

# NOTE: Rehashing alone will not solve collisions. However, it will create a new hash table with a new size. We will learn about collision resolution after we learn to resize our hash table.

# ....................Thought Process: Rehashing...............#
# Suppose we have this hash function H(x) = X mod 10.
# If the load factor threshold is reached during hashing, we will rehash the values in a new hash table using H(x) = X mod 20 as the hash function.

# 1. Create a list to store hash values.

# Since this hash function gives hash values between 0 and 9, we will initialize a list of 10 elements.

# # all elements are initialized to None
# size = 10
# table = [None] * size
# 2. Define the load factor threshold.

# lf_threshold = 0.7
# 3. Find the hash of a key.

# hash_value = key % size
# 4. Insert data into the hash table.

   
#  # insert into table
# hash_value = self.hash_function(key)
# self.table[hash_value] = key
# 5. Compute threshold during each insertion

# # current lf = occupied slot/total slots
# current_lf = sum(1 for slot in self.table if slot) / (self.size)
# 6. Rehash if the load factor exceeds the threshold.

# if current_lf > lf_threshold:
#     # create a new hash table
#     self.size = 2 * self.size
#         new_table = [None] * self.size 

#     # insert data from old table into new hashtable
#     for data in self.table:
#         if(data):
#             hash_value = self.hash_function(data)
#             new_table[hash_value] = data

#     # update table
#     self.table = new_table