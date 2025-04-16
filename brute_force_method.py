# ....................Introduction........................
# The brute force method is the most straightforward method for string-matching. It involves comparing the given pattern with every substring in the text until a match is found.

# Next, we will visualize the workings of the brute force method using images.

# ..............Working of Brute Force Method..................
# Suppose we have the following text:

#         [CODEWITHCODER]

# And we have to search the following pattern:

#         [CODE]

# To find the required pattern, we align the pattern with the same length at the beginning of the text.

#         Text
#         [CODEWITHCODER]

#         Pattern
#         [CODE]

# At this point, we align the pattern "CODE" with the first four characters of our original text. We then compare the first characters of the text and the given pattern.

# As "C" and "C" match, we now check for the second character.
# Here, the first four characters of the pattern match with the original text. In other words, we found a match.

# However, the text can have more than one occurrence of the pattern. Thus, we continue our search.

# We then move and check the pattern with the next four characters of the string.
#           Text
#         [CODEWITHCODER]

#         Pattern
#          [CODE]

# As the character "O" doesn't match the first character of the pattern ("C"), we shift one step forward in the text.
# We then move on to the next set of characters.

# #         Text
# #         [CODEWITHCODER]

# #         Pattern
# #           [CODE]

# Here, "D" and "C" don't match. So, we move on to the next character.

#         #         Text
# #         [CODEWITHCODER]

# #         Pattern
# #             [CODE]
# Here, "E" and "C" don't match. So, we move on to the next character.

# #         Text
# #         [CODEWITHCODER]

# #         Pattern
# #              [CODE]
# Here, "W" and "C" don't match. So, we move on to the next character.

# #         Text
# #         [CODEWITHCODER]

# #         Pattern
# #              [CODE]
# Here, "I" and "C" don't match. So, we move on to the next character.

# #         Text
# #         [CODEWITHCODER]

# #         Pattern
# #               [CODE]
# Here, "T" and "C" don't match. So, we move on to the next character.

# #         Text
# #         [CODEWITHCODER]

# #         Pattern
# #                [CODE]
# Here, "H" and "C" don't match. So, we move on to the next character.

# #         Text
# #         [CODEWITHCODER]

# #         Pattern
# #                 [CODE]
# Here, the pattern matches the substring of our text. However, we continue our search.

# Here, "O" and "C" don't match. So, we continue moving on to the remaining characters until we finally reach the end of the text.

# #         Text
# #         [CODEWITHCODER]

# #         Pattern
# #                  [CODE]
# In this way, the pattern "CODE" is matched twice within our original string.

#.....................Thought Process to Implement Brute Force Method
# Now, let's see how we can implement the brute force method.
# 1. Get the text and the pattern.

        # def brute_force(text, pattern):

# The function takes two arguments:
#     * text - the original string
#     * pattern - the pattern to be searched

# 2. Iterate over the text and pattern.
# Inside the function, we use two nested loops to compare characters from the text and the pattern.
        # for i in range(len(text)):
        #     for j in range(len(pattern)):

# These loops allow us to consider all possible starting positions of the pattern in the text.

# 3. Check for a complete match.
# At each position, we compare characters in the text with characters in the pattern to see if they match. If we find a mismatch at any point, we break out of the inner loop.

#         # inside the inner loop
#         match = text[i+j] == pattern[j]
#         # mismatch found, break the loop
#         if not match:
#             break  

# If we've successfully matched all characters in the pattern, we record the starting position of the match and store them in a list called occurrences.

        # if j == len(pattern)-1:
        #     occurrences.append(i)

# The direct comparison technique for pattern searching is straightforward but inefficient for locating matches within text.


#................Source Code: Brute Force Method................
def brute_force(text, pattern):
    # initialize a list to store positions of pattern occurrences
    occurrences = []  

    for i in range(len(text) - len(pattern) + 1):

        # check if the pattern matches starting from position i
        for j in range(len(pattern)):
            
            match = text[i+j] == pattern[j]
            # mismatch found, break the loop
            if not match:
                break  
            # whole pattern is matched, record the position
            if j == len(pattern) - 1:
                occurrences.append(i)  
            
        

    return occurrences  


input_text = "CODEWITHCODER"
input_pattern = "CODE"
occurrences = brute_force(input_text, input_pattern)
if occurrences:
    print(f"The pattern found at indices: {occurrences}.")
else:
    print("The pattern is not present in the text.")