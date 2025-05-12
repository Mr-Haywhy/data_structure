# .................Introduction..............
# In the Rabin-Karp algorithm, we use hashes of strings to find the matching pattern.
# Rabin-Karp approach compare the pattern with the subtext only if they have equal hash values.

# Let's see how it works next.

# ..............Working of Rabin-Karp Algorithm..............
# Suppose we need to find a pattern of length m in the text string.

# Here is how it works:
    # *Find the hash of the pattern.
    # *Calculate the hash of the substring of the length m in text, starting from the first character.
    # *Compare the hash of the pattern with the hash of the substring to find the match.
    # *Calculate the hash of the next substring of the length m in text, starting from the second character.
    # *Compare the hash of the pattern with the hash of this substring to find the match.
    # *Repeat this process for all substrings of length m in the text string.
# In this algorithm, we compare the entire pattern only after the hash value is matched. This approach reduces redundant comparisons.

# Let's explore this process in detail.

# Before going further, let's look at hashing as it is essential for the Rabin-Karp algorithm.
# We have already covered hashing in the previous chapter. Rabin-Karp uses hashing slightly differently; it uses the concept of rolling hash.

# Next, we'll learn how rolling hash works.

#...................Rolling hash..........................
# Rolling hashing (also known as recursive hashing) is a hashing technique that involves the continuous recalculation of the hash values for the substrings within a text.

# Consider the following example.
# Suppose we have the following text: 
#                 "ABCD".

# Our task is to calculate the hash values of all the substrings of length three.
# To achieve this, we will first assign a hash function to each character of the string.
# Let's assume our hash function assigns the following ASCII values to each character:
#                 65 66 67 68
#                 "A B  C  D".

# Next, we'll calculate the hash value for the initial substring.

# Let's begin by calculating the hash value of the substring "ABC".

#                 65 66 67
#                  A  B  C 

# Hash(ABC) = Hash(A) + Hash(B) + Hash(C) = 65 + 66 + 67 = 198

# Next, we will shift the substring one character to the right. This results in another substring, "BCD".

#                 66 67 68
#                  B  C  D

# Once we have the hash value of one substring, we can easily compute the hash value of a different substring of the same length. Here's how:

# Hash(BCD) = (Hash(ABC) - Hash(A))  + Hash(D) = (198 - 65)  + 68 = 133 + 68 = 201

# In this way, we can calculate the hash values of all substrings of length three.

# Since we are not recalculating the hash value of each character in subsequent steps, using the rolling hash technique improves the performance of string matching algorithms.
# The central purpose of the rolling hash technique is to recalculate hash values for substrings efficiently.
# The rolling hashing method improves the performance by removing redundant calculation of hash values.

#......................The Hash Function......................
# For the Rabin-Karp algorithm, the hash function is defined such that:

#     *The hash value of a string is as unique as possible.
#     *The function can undergo rolling hash.

# We will use this hash function to compute a unique hash value.

    # Hash value = ∑(character_value*base^length-1) mod prime_number

# Here, we select the base value of 256 to include all the characters and a prime number of 101 to reduce the risk of hash collisions.

# Now, let's calculate the hash value for the following substring.

    # Hash value=(65*256^2)+(66*256^1)+(67*256^0)mod101
    # = (65*65536)+(66*256)+67 mod 101
    # = 4259840+16896+67 mod 101
    # = 4276803 mod 101
    # = 59

# So, the hash value for the substring "ABC" is 59.
# Next, we will write a working program to implement hashing.

#................Source code: Rolling Hashing........................
def compute_hash(string, base = 256, prime_number = 101):
   
    # initialize the hash value to 0
    hash_value = 0
    
    # iterate over each character in the string
    for index,char in enumerate(string):
        # get the ASCII value 
        ascii_value = ord(char)
        # calculate the exponent for each character
        exponent = len(string) - index - 1
        # calculate the term for the current character
        term = (ascii_value * pow(base, exponent)) % prime_number
        # update the hash value
        hash_value = (hash_value + term) % prime_number

    return hash_value

string_to_hash = "ABC"

hash_result = compute_hash(string_to_hash)
print(f"The hash value of '{string_to_hash}' is: {hash_result}")


#..................Working of Rabin-Karp Algorithm...............
# Suppose we have the following text:

#       [ABCCDDAEFG]

# And we have to search for the following pattern:
#       [CDD]

# Let's see how we can search for the requied pattern in the text.
# To find the required pattern, we first assign an ASCII value to each character that we will be using in the problem.

# 65 66 67 68 69 70 71 72 73 74
# A  B  C  D  E  F  G  H  I  J

# After this, we align the pattern with the same length of the text.

# Text:  [ABCCDDAEFG]
# Pattern:  [CDD]

# Now, we need to compare the pattern with the first three characters of text, i.e., "ABC".
# The hash value of pattern "CDD" is calculated as:

        # Hash value = (67×256^2)+(68×256^1)+(68×256^0)mod 101
        # =(67×65536)+(68×256)+68mod101
        # =4390912+17408+68mod101
        # =4408488mod101
        # =41

# Here, the hash value for the pattern "CDD" is 41 but that of "ABC" is 59.
# Since the hash values don't match, we then move to the next character.
# Here, the hash value for the pattern "BCC" is 100, but that of "CDD" is 41.
# next character
# Here, the hash value for the pattern "CDD" is 41, but that of "CCD" is 88.
# next character
# Here, the hash values for both the pattern "CDD" and the substring "CDD" is 41, resulting in a match.
# Now, we compare the pattern and the substring just like we did with the brute-force algorithm. As a result, we find that strings do indeed match.
# However, a string can have multiple matches to the same pattern. Therefore, we continue our search and move on to the next character.
# Here, the hash value for the pattern "CDD" is 41, but that of the "DDA" is 25.
# next character
# Here, the hash value for the pattern "CDD" is 41, and that of the "DAE" is 69.
# next character
# Here, the hash values for the pattern "CDD" is 41, and that of "AEF" is 22.
# next character
# Here, the hash value of the pattern "CDD" is 41, and that of "EFG" is 25.
# In this way, we search for the pattern from the given string.