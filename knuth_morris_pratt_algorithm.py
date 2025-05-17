#.................Introduction....................
# The Knuth-Morris-Pratt (KMP) algorithm is another string-matching algorithm.
# It improves the process by using a precomputed table (often called a prefix table) to skip unnecessary comparisons.
# Before jumping into the technical aspects of the algorithm, let's first learn about the basics.

#...................KMP Basics....................
# The prefix table in the Knuth-Morris-Pratt (KMP) algorithm is used to determine the number of characters to be skipped when a mismatch occurs between the pattern and the text.

# Let's consider a simple scenario to understand how the prefix table works.

# Consider the text "ABDABC" and the pattern "ABC".

# In a brute-force approach, we compare the pattern with the text sequentially:

#           A B D A B C
# 1st Comp. A B C
# 2nd Comp.   A B C 
# 3rd Comp.     A B C 
# 4th Comp.       A B C 

# After comparison 1, we already know that the second character of the text is "B", and the third character of the text is "D".

# Since our pattern starts with "A", we can skip comparison 2 and comparison 3 because the substrings start from "B" and "D" respectively.

#           A B D A B C
# 1st Comp. A B C
# 2nd Comp.       A B C 

# With this approach, we can skip two unnecessary comparisons.

#......................KMP Basics........................#
# Our optimization becomes even more noticeable in cases of texts with repeating patterns.

# Take the text "ABABABAC" and the pattern "ABABAC". The algorithm compares the pattern (length 6) with a substring of the same length.

#           A B A B A B A C
#           A B A B A C

# As you can see, the last character "C" of the pattern does not match. And, we can also notice from the comparison that the third character in the text is "A".

# So, our pattern can start directly from the third character of the text, thus skipping one unnecessary comparison.

#           A B A B A B A C
#               A B A B A C

# Previously, we skipped an unnecessary comparison in our algorithm:
# Now, let's skip even more characters.
# From the initial comparison (refer to the previous page), we find that the first three characters of the pattern ("ABA") have already matched with the text.
# Therefore, we can skip these three comparisons as well.
# In the KMP algorithm, this information on how many characters to skip is stored in a table known as a prefix table.

# A prefix table provides two crucial pieces of information:
    # How many characters can we skip from the text?
    # How many characters can we skip from the pattern?

# So, let's learn how to fill this table.

#.................How to Fill a Prefix Table?.................
# Let's understand the general rules for filling the prefix table in the Knuth-Morris-Pratt (KMP) algorithm.

# We fill the prefix table with integers that later help us skip the unnecessary comparisons.

# The integer value associated with each character of a pattern is referred to as a ____fail function____.

# Next, we'll explore these rules in detail.

#.....................Rules For Prefix Tables.................
# Let's suppose we have the following pattern: "ABABACA". Then, we can follow the rules given below to create its prefix table:

# 1. The fail function value for the first character of the pattern is always 0. This indicates the starting point of the pattern.

# Pattern:       A B A B A C
# Pattern:       A B A B A C
# Fail function: 0

# 2. If any other character in the pattern doesn't match the first character, its fail function is assigned the value 0.

# This indicates there is no repetition of characters. Consequently, we cannot skip any comparison.

# Pattern:       A B A B A C A
# Pattern:         A B A B A C A
# Fail function: 0 0

# 3. If a character matches the first character, its fail function is set to 1.

# This suggests the beginning of a potential repeating pattern. Thus, we can skip one character.

# Pattern:       A B A B A C A
# Pattern:           A B A B A C A
# Fail function: 0 0 1

# 4. Each match increases the value of the fail function by 1.

# Also, instead of matching the character with the first character, we move the reference character one position to the right.

# Pattern:       A B A B A C A
# Pattern:           A B A B A C A
# Fail function: 0 0 1 2

# Similarly,

# Pattern:       A B A B A C A
# Pattern:           A B A B A C A
# Fail function: 0 0 1 2 3

# 5. In the event of a mismatch, the fail function resets to 0.

# Pattern:       A B A B A C A
# Pattern:           A B A B A C A
# Fail function: 0 0 1 2 3 0

# However, the mismatched character is then again compared to the first character of the pattern to check if it starts a new matching prefix.

# Pattern:       A B A B A C A
# Pattern:                 A B A B A C A
# Fail function: 0 0 1 2 3 0

# If the mismatched character matches the first character, the fail function for that character is set to 1, indicating the start of a new potential pattern.

# 6. The process continues until the pattern ends.

# We repeat all the previous processes until we reach the end of the pattern.

# Pattern:       A B A B A C A
# Pattern:                   A B A B A C A
# Fail function: 0 0 1 2 3 0 1

# This is how the prefix table is filled. Let's look at it with the help of an example.

#................Example: Prefix Table...........
# Suppose we have the following pattern:

        # A B A B A C A

# To fill the prefix table, we initialize the fail function as F and set F[0] = 0.

# Since the second character, "B" doesn't match the first character, "A", we set F[1] = 0 as well.

#   P| A B A B A C A
#   F| 0 0

# NOTE: The fail function gives the number of characters you can skip using the prefix table.

# For F[2], we compare the characters at index 0 and index 2. Since they are the same ("A" and "A"), so F[2] = 1.

#      0 1 2 3 4 5 6
#   P| A B A B A C A
#   F| 0 0 1

# This implies that we can skip one comparison for the future.

# Prefix Table: _ A B A _ _ _ _ _ _ _
# Pattern:        A B A B A C A
# Fail Function:      A B A B A C A

# Since the match occurs for P[0] and P[2], we increase our next comparison with one more character.

# For this case, we will now compare P[0:1] with P[2:3] (we increased our comparison by one character).

# For F[3], since the previous pattern "AB" (length 2) is being repeated, so F[3] = 2.

#      0 1 2 3 4 5 6
#   P| A B A B A C A
#   F| 0 0 1 2

# This implies that we can skip two comparisons for the future.

# Prefix Table: _ A B A B _ _ _ _ _ _
# Pattern:        A B A B A C A
# Fail Function:      A B A B A C A

# For F[4], since the initial pattern of "ABA" (length = 3) appears again, so F[4] = 3.

#      0 1 2 3 4 5 6
#   P| A B A B A C A
#   F| 0 0 1 2 3

# This implies that we can skip three comparisons for the future.

# Prefix Table: _ A B A B A _ _ _ _ _
# Pattern:        A B A B A C A
# Fail Function:      A B A B A C A

# For F[5], since the character "C" does not match with the previous pattern nor the first character, we set F[5] = 0.

#      0 1 2 3 4 5 6
#   P| A B A B A C A
#   F| 0 0 1 2 3 0

# This implies that we can skip no comparisons in the future.

# Prefix Table: _ A B A B A C _ _ _ _
# Pattern:        A B A B A C A
# Fail Function:              A B A B A C A

# For F[6], since the character "A" matches the first character "A", so F[6] = 1.

#      0 1 2 3 4 5 6
#   P| A B A B A C A
#   F| 0 0 1 2 3 0 1

# This implies that we can skip one comparison in the future.

# Prefix Table: _ A B A B A C A _ _ _
# Pattern:        A B A B A C A
# Fail Function:              A B A B A C A

# Thus, we have filled our prefix table.

# NOTE: The numbers that we fill up in the prefix table are referred to as longest prefix suffix (LPS) values.

# Next, we will write a working program to fill a prefix table.

#....................Source Code: Prefix Table................

def compute_lps_array(pattern):
    # start with F[0] = 0
    lps = [0]
    # temporary value
    c = 0
    # start from 1 because we already have F[0] = 0
    for i in range(1, len(pattern)):
        # in case of a pattern match
        if pattern[c] == pattern[i]:
            # increase substring length by 1
            c = c + 1 
        # else if pattern matches the first character
        elif pattern[i] == pattern[0]:
            c = 1
        # if the pattern doesn't match the subsequence or the first character
        else:
            # reset substring length to 0
            c = 0
        # Fail function F[i] = c
        lps.append(c)
        
    return lps

# example usage 
pattern = "ABABACA"
lps_result = compute_lps_array(pattern)
print(f"The LPS array for pattern '{pattern}' is: {lps_result}")


#....................Working of the KMP Algorithm.............
# Let's see how a prefix table helps in string-matching algorithms.
# Consider the following pattern: "ABABAC".
# The prefix table will be:

#   A B A B A C
#   0 0 1 2 3 0

# Now, let's compare the previous pattern "ABABAC" with the text "ABABABAC".

#   A B A B A B A C
#   A B A B A C
#   0 0 1 2 3 0

# When comparing the two, we can see that the first five characters match.
# However, "B" and "C" do not match.

# Normally, you would shift the pattern one position to the right and start comparing again.

# However, using the prefix table, we can skip all redundant comparisons.
# Next, we'll look at how to skip these unnecessary comparisons.

# In our comparison, the text and the pattern only matched until the first five characters.

# If we look at the last match, we can see that the corresponding value of the fail function is 3.

#   A B A B |A| B A C
#   A B A B |A| C
#   0 0 1 2 |3| 0

# This 3 implies that we can skip the pattern comparison for the first three characters.

# NOTE: Since we referred to text[4] to get 3, we align the pattern such that the third character of the pattern aligns with text[4].

#......Skipping Characters......
# If we align pattern[2] with text[4] in the above comparison, we get the following:

# Index 0 1 2 3 4 5 6 7
#       A B A B A B A C
#           A B A B A C
# Index     0 1 2 3 4 5

# On further matching, we can see that this substring matches the pattern.

#       A B A B A B A C
#           A B A B A C
# LPS       0 0 1 2 3 0

# This is how step-by-step matching works in KMP.

#..............Thought Process: KMP Algorithm.................
# Now, let's see how we can implement the KMP algorithm in Python:

# 1. Get the text and the pattern.
        # def kmp(text, pattern):

# Here, we have defined the kmp() function which takes in two arguments:
#     * text - the original string
#     * pattern - the pattern to be searched

# 2. Create the prefix table (compute the longest prefix suffix array).
        # lps = compute_lps_array(pattern)

# 3. Iterate over the text.
        # while i < len(text):

# 4. Check for a match.
# At each position, we check if the character in pattern matches with the corresponding character in text.
# If there is a match, we increment the pointers for both text and pattern.

        # if pattern[j] == text[i]:
        #     i += 1
        #     j += 1

# 5. Check for a complete match.
# After each match, we check if the pattern is matched completely and store them in a list called occurrences. We also update the value of j using the lps list.

        # # check for a complete match
        # if j == len(pattern):
        #     occurrences.append((i - j))
        #     # Reset j based on the lps array
        #     j = lps[j - 1]

# We shift j in case of a match because the text can have more than one occurrence of the pattern.

# 6. In case of a mismatch, shift to the next potential match.
        ## If there is a mismatch, adjust j based on the lps array
        # if j != 0:
        #     j = lps[j - 1]
        # else:
        ## If j is already 0, move to the next character in the text
        #     i += 1


#.................Source Code: KMP Algorithm..................
def compute_lps_array(pattern):
    # start with F[0] = 0
    lps = [0]
    # temporary value
    c = 0
    # start from 1 because we already have F[0] = 0
    for i in range(1, len(pattern)):
        # in case of a pattern match
        if pattern[c] == pattern[i]:
            # increase substring length by 1
            c = c + 1 
        # else if pattern matches the first character
        elif pattern[i] == pattern[0]:
            c = 1
        # if the pattern doesn't match the subsequence or the first character
        else:
            # reset substring length to 0
            c = 0
            
        lps.append(c)
    return lps


def kmp(text, pattern):
    # compute the lps array for the given pattern
    lps = compute_lps_array(pattern)
    
    # initialize a list to store occurrences of the pattern in the text
    occurrences = []
    i = 0
    j = 0  # Using 'j' to track the position in the pattern
    
    # iterate over the text
    while i < len(text):
        # check for a match
        if text[i] == pattern[j]:
            i += 1
            j += 1
            # check for a complete match
            if j == len(pattern):
                occurrences.append((i - j))
                # Reset j based on the lps array
                j = lps[j - 1]
        else:
            # If there is a mismatch, adjust j based on the lps array
            if j != 0:
                j = lps[j - 1]
            else:
                # If j is already 0, move to the next character in the text
                i += 1

    # Return the list of occurrences of the pattern in the text
    return occurrences

# example usage
text = "ABABA"
pattern = "ABA"
occurrences = kmp(text, pattern)
if occurrences:
    print(f"The pattern found at indices: {occurrences}.")
else:
    print("The pattern is not present in the text.")