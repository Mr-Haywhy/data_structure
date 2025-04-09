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