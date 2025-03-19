# BINARY SEARCH
# 
# Unlike linear search, binary search can only be implemented in a sorted list. If the elements in the list are unsorted, we need to sort the elements first.
# Binary search repeatedly compares the middle element with the target and uses the sorted nature of the list to eliminate half of the remaining elements
# 
# Thought Process: binary search
# 1. Set the first index as low and the last index as high
        # low = 0
        # high = len(lst) - 1
# 2. Find the middle element.
        # mid = (low + high) // 2
# 3. Check for three possibilities.
# 
    # Possibility 1: If the target value is equal to the middle element, we have found the element.
            # if target_value == lst[mid]:
            #     result_index = mid
# 
    # Possibility 2: If the target value is greater than the middle element, update the low index to mid + 1.
            # if target_value > lst[mid]:
            #     low = mid + 1
# 
    # Possibility 3: If the target value is less than the middle element, update the high index to mid - 1.
            # if target_value < lst[mid]:
            #     high = mid - 1
# 
# Basically, we are updating the low and high indexes such that they are closer to both the mid value and the target element.
# 
# 4. We update the mid element again and repeat step 3.
# We will repeat the process until low is greater than high. If low is greater than high, our target value is not in the list.
# 
        # ## if low is greater than high,
        # # the element is not found in the list 
        # while low <= high:

        #     # update middle point in each iteration
        #     mid = (low + high) // 2

        #     # condition for target value found
        #     if target_value == lst[mid]:
        #         return mid

        #     # update either low or high
        #     elif target_value < lst[mid]:
        #         high = mid - 1
        #     else:
        #         low = mid + 1
# 

# Binary search using the iterative process.
# function to perform binary search
def binary_search(lst, target):
    
    # set low and high index
    low = 0
    high = len(lst) - 1
    
    # if low is greater than high,
    # the element is not found in the list 
    while low <= high:
        
        # find middle element
        mid = (low + high) // 2
        
        # if target value is equal to middle element
        # return the element
        if target == lst[mid]:
            return mid
        
        # if target value is less than the middle element
        # update high to mid - 1 
        elif target < lst[mid]:
            high = mid - 1
        
        # if target value is less than the middle element
        # update low to mid + 1 
        else:
            low = mid + 1
    
    return None
