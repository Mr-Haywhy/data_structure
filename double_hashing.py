#.................Double Hashing.....................#
# In double hashing, two hash functions are used to determine the probing sequence.
# The primary hash function calculates the initial index, while the secondary hash function determines the step size for probing.

# Double hash function:
#         H(x) = (H1(x) + i * H2(x)) % table_size(n)
# where,
#     i = 0, 1, 2, …
#     H1(x) = primary hash function
#     H2(x) = secondary hash function

# Primary hash function:
# H1(x) = x % table_size(n)

# The second hash function can be anything you like. However, you must meet two conditions:

#     1. H2(x) should never be zero.
#     2. H2(x) should cover all remaining cells.

# When double hashing a modulus hash, our second function generally takes the form of:

#     H2(x) = n - x % n(table_size)
        #     or
#     H2(x) = 1 + x % (n - 1) table_size - 1

#....................Working of Double Hashing
# Consider the hash function: H(x) = x mod 12 and the following keys 12, 17, 15, 4, 27, 14, and 37.

# For this example, let our secondary hash function be H2(x) be:
        # H2(x) = 1 + x % (n - 1)
        # H2(x) = 1 + x % (10-1) = 1 + x % 9
# Insert into hash table

# Let's hash the value 12.
#   *Primary Hash: H1(12) = 12 % 12 = 0
#   *Secondary Hash: H2(12) = 1 + (12 % 11) = 2

        # H(12) = (0 + 0 * 2) % 12 = 0

# Similarly, the rest of the numbers are hashed as:

# Hashing value: 14
#   *Primary Hash: H1(14) = 14 % 12 = 2
#   *Secondary Hash: H2(14) = 1 + (14 % 11) = 4

        # H(14) = (2 + 0 * 4) % 12 = 2

# Hashing value: 2
#   *Primary Hash: H1(2) = 2 % 12 = 2
#   *Secondary Hash: H2(2) = 1 + (2 % 11) = 3

        # H(3) = (2 + 0 * 3) % 12 = 2 (Collision with 12)
        # H(3) = (2 + 1 * 3) % 12 = 5 

# Hashing value: 6
#   *Primary Hash: H1(6) = 6 % 12 = 6
#   *Secondary Hash: H2(6) = 1 + (6 % 11) = 7
        # H(6) = (6 + 0 * 7) % 12 = 6 

# Hashing value: 9
#   *Primary Hash: H1(9) = 9 % 12 = 9
#   *Secondary Hash: H2(9) = 1 + (9 % 11) = 10
        # H(9) = (9 + 0 * 10) % 12 = 9 

# Hashing value: 26
#   *Primary Hash: H1(26) = 26 % 12 = 2
#   *Secondary Hash: H2(26) = 1 + (26 % 11) = 5
        # H(26) = (2 + 0 * 5) % 12 = 2 (Collision with 12 and 2)
        # H(26) = (2 + 1 * 5) % 12 = 7 
# This is the final form of the hash table:

        #_keys_ | _Hash_value_
        #   0   |   12
        #   1   |
        #   2   |   14
        #   3   |
        #   4   |
        #   5   |   2
        #   6   |   6
        #   7   |   26
        #   8   |
        #   9   |   9
        #   10   |
        #   11   |

#............Working of Double Hashing..............#
#.....Retrieve values from the hash table

# Retrieving a value using Double Hashing is the same as probing; here, the step size is determined by the second function. 
# Follow these steps:
    # Hash the value using the primary hash function.
    # If the value is found at its expected index, return it.
    # If not, use the secondary hash function to calculate the step size and move to the next slot.
    # Repeat until you find an empty slot or the desired value.