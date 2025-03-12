# SELECTION SORT
# Working of selection sort
# Suppose we have the following unsorted list.
# UL[18, 10, 8, 14, 1]
# To sort this list, we follow these steps:
# 1. Find the smallest element and swap it with the first element in the list. 
#  At this point, the correct element is placed at the first position. However, the portion of the list from the second position to the last remains unsorted
# 2. Find the smallest element in the unsorted portion of the list and swap it with the second element.
# 3. Continue this process until all the elements are sorted.


# THOUGHT PROCESS TO IMPLEMENT SELECTION SORT
# First, let's see how we can find the smallest element and swap it with the element in the first position.
# 1. Find the index of the smallest element in the list.
        # min_index = 0
        # # iterate from second element to last
        # for j in range(1, len(lst)):
        #     # get the index of the smallest element
        #     if lst[j] < lst[min_index]:
        #         min_index = j

# 2. Swap the smallest element with the first element.
        # lst[min_index], lst[0] = lst[0], lst[min_index]

# 3. Repeat step 2 for each element in the list
        # for i in range(len(lst)):
        #     min_index = i

        # for j in range(i + 1, len(lst)):
        #     if lst[j] < lst[min_index]:
        #         min_index = j


# lst = [18, 10, 8, 14, 1]

# min_index = 0

# #  outer loop to ensure that each element in the list is considered, not just the first element
# for i in range(len(lst)):
#     min_index = i
#     # iterate from second element to last
#     for j in range(i + 1, len(lst)):
        
#         # get the index of the smallest element
#         if lst[j] < lst[min_index]:
#             min_index = j
#             # swap the smallest element with the first element
#     lst[min_index], lst[i] = lst[i], lst[min_index]


# print(j)  # 4

# # 1st iteration
# # in the first iteration of the outer loop, we identify the smallest element in the entire list
# # 2nd iteration
# # After the first iteration the unsorted position of the list will be from the second to the last position. In the second iteration, we identify the smallest element in th unsorted position of the list(second smallest element). Then, this element is swapped with the second element.
# # This process continues until the end of the list is reached.

def selection_sort(lst):
   
    for i in range(len(lst)):
        
        # assume the first unsorted element is the minimum
        min_index = i
    
        # iterate over unsorted elements
        for j in range(i + 1, len(lst)):

            # find index of the smallest element
            # in the unsorted part of the list
            if lst[j] < lst[min_index]:
                min_index = j
    
        # swap the smallest element with the first element
        # of the unsorted part 
        lst[min_index], lst[i] = lst[i], lst[min_index]
        print(lst)
    return lst

   

data = [18, 10, 8, 14, 1]
print(f'Unsorted List: {data}')

sorted_list = selection_sort(data)
print(f'Sorted List: {sorted_list}')


