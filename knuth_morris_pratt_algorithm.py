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