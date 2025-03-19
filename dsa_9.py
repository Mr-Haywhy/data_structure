# Search algorithms are fundamental techniques in computer science that involve looking for a specific item, value, or piece of information within a dataset.
# The concept of computer search parallels tasks we perform daily, such as finding a book in a library, locating a contact in a phone directory, or even searching for a specific word in a document.
# Here, we will cover two types of search algorithms:
    # Linear Search
    # Binary Search

# LINEAR SEARCH
# The linear search algorithm is used to find an element within a list.
# In this algorithm, we sequentially check each element of the list until the desired element is found.

# Thought Process to Implement Linear Search
# 
# 1. Use a loop to traverse (access elements one-by-one) along with its corresponding index.
        # for index, element in enumerate(lst):
                # pass
# 
# 2. Compare each element with the target value.
    # Within the loop, we will compare list elements to the target value. If a match is found, we use the corresponding index of that value.
        # for index, element in enumerate(lst):
                # if element == target:
                #     result = index
# 
# 3. If the element is not found in the list, set the result to None.
        # for index, element in enumerate(lst):
                # if element == target:
                #       result = index
        # result = None
# 


# FUNCTION TO PERFORM LINEAR SEARCH

def linear_search(lst, target):
    # travese through each element
    for index, element in enumerate(lst):
        # compare each element with a target value
        if element == target:
            return index
    # return None if the target isn't found in lst
    return None

linear_search()