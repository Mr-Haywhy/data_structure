#..............Modulus Hash Function...............
# The hash function you've learned so far is the modulus hash function. You take a value and perform the modulus operation with the table size.

#     H(x) = x % n
# where,
#     n is the table size.

# NOTE: To minimize collisions, it's advisable to use a prime number as the table size.
# Next, we will learn about the mid-square hash function.


#................Mid-Square Hash Function................
# The mid-square hash function involves squaring a given number, extracting a portion of the resulting square, and using that portion as the hash value.

# Typically, the extracted portion is from the middle of the square, which is why it's called the mid-square hash function. This technique aims to distribute hash values more uniformly and reduce clustering.

# Let's apply the mid-square hash function to our dataset 12, 14, 2, 6, 9, 26 using a hash table size of 12:

#.................Hashing the Numbers..............
# 12: The square of 12 is 144. Choosing the middle digit, we get 4.
# 14: The square of 14 is 196. Middle digit: 9.
# 2: The square of 2 is 4. Middle digit: 4.

# NOTE: Since this causes collision, we can use any collision resolution techniques. Let's probe it to index 5 (using linear probing).

# 6: The square of 6 is 36. Middle digit: 3.

# NOTE: Since it has no middle digit, we take the first digit.

# 9: The square of 9 is 81. Middle digit: 8.
# 26: The square of 26 is 676. Middle digit: 7.

        #_keys_ | _Hash_value_
        #   0   |   
        #   1   |
        #   2   |   
        #   3   |   6
        #   4   |   12
        #   5   |   2
        #   6   |   
        #   7   |   26
        #   8   |   9
        #   9   |   14
        #   10   |
        #   11   |



#................Folding Hash Function
# The folding hash function involves dividing a given number into segments, summing these segments, and using the resulting sum as the hash value.

# This technique spreads data more uniformly across hash table slots, reducing clustering and improving data storage efficiency.

# Let's apply the folding hash function to our dataset (12, 14, 2, 6, 9, 26) using a hash table size of 12:

# Hashing the Numbers:
# 12: Splitting into segments: 1 and 2. Adding segments: 1 + 2 = 3.
# 14: Splitting into segments: 1 and 4. Adding segments: 1 + 4 = 5.
# 2: Splitting into segments: 0 and 2. Adding segments: 0 + 2 = 2.
# 6: Splitting into segments: 0 and 6. Adding segments: 0 + 6 = 6.
# 9: Splitting into segments: 0 and 9. Adding segments: 0 + 9 = 9.
# 26: Splitting into segments: 2 and 6. Adding segments: 2 + 6 = 8.

#         #_keys_ | _Hash_value_
#         #   0   |   
#         #   1   |
#         #   2   |   2
#         #   3   |   12
#         #   4   |   
#         #   5   |   14
#         #   6   |   6
#         #   7   |   
#         #   8   |   26
#         #   9   |   9
#         #   10   |
#         #   11   |


# This is how the folding hash function works. Like the previous hash functions, all collision resolution and other operations are the same as those used in the modulus hash function.

# As you can see, the folding hash function distributes the keys more evenly than the previous hash function.

# Now, let's explore another example of using the folding hash method.

# Consider the following data 123347:

# Let's divide the number into sets of two digits.
#         123347 -> 12 + 33 + 47 = 92 
 
# Since our table of size 12 doesn't have a key 92, we can fold it further.
#         9 + 2 = 11

# Alternatively, we can also take modulus from here.
#         92 % 14 = 8
# The choice is entirely yours.


#.............Custom Hash Functions
# All the techniques and functions mentioned above are commonly used hash functions, but you're not limited to them.

# Every problem is unique and might require a different hash function tailored to its characteristics.

# Let's revisit the problem we started with:

# 1 | Apple
# 2 |
# 3 | Cactus
# 4 |
# 5 |
# 6 |
# 7 | Grasshopper
# 8 |
# 9 | Iron
