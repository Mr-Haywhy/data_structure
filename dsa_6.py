# MERGE SORT
# Merge sort breaks a list into multiple sublists, and each sublist is then sorted individually.
# Then, the sorted sublists are combined to form the sorted list.

# number = [1,2,1,6,9,1,2,0,5,4,2,5,6,9]
# mid = len(number) // 2
# print(number[mid : ])

# FIND THE MID-POINT OF THE LIST
# 1. Find the midpoint of the list.
# 2. Divide the list's smaller halves recursively until individual elements are retrieved.

        # merge_sort(lst):
        #     mid = len(lst) // 2

        # end recursion if list is divided into individual elements
        # i.e. when list length is 1
            # if len(lst) <= 1:
            #     return lst

        # get the left half portion of list and recursively divide it again
            # left_partition = merge_sort(lst[: mid])
        # get the right half portion of the list and recursively divide it again
            # right_partition = merge_sort(lst[mid: ])


######## MERGE_SORT VISUALIZER ########
# def merge_sort(lst):

#     if len(lst) <= 1:
#         return lst
    
#     print(f"lst: {lst}")

#     # get the mid_point of the list
#     mid = len(lst) // 2

#     print(f'mid: {lst[mid]}')

#     # get the left half portion of list and recusively divide it again
#     left = merge_sort(lst[: mid])
#     print(f'Left partition: {left}')

#     # get the left half portion of list and recusively divide it again
#     right = merge_sort(lst[mid: ])
#     print(f'Right partition: {right}')

#     return '---'

# data_list = [5,4,8,7,3,2]
# merge_sort(data_list)

# Suppose we have two sorted lists: our goal is to get this sorted list by merging them.
# The merge() function should also work for list with more than one element.
# 1. Compare the elements of left and right and add the smaller element to the output list.
    # # empty list to store the merged result
    # output = []

    # # index for the left sublist
    # i = 0

    # # index for the right sublist
    # j = 0

    # # if element of left list is smaller
    # # add that element to the output list
    # if left[i] < right[j]:
    #     output.append(left[i])

    # # else, add the element of right list
    # else:
    #     output.append(right[j])

# 2. Repeat Step 1 for all elements in both lists until we reach the end of one of the lists.
# This allows us to extract the smallest elements one by one.
    # output = [ ]

    # i = 0
    # j = 0

    # # loop through both the lists
    # while i < len(left) and j < len(right):

    #     if left[i] < right[j]:
    #         output.append(left[i])
    #         i += 1;    # increment i
    #     else:
    #         output.append(right[j])
    #         j += 1;    # increment j

#  the loop terminate once one of the lists exceeds its bounds.
# 3. Outside the loop, append the remaining elements and return the output list.
    # def merge(left, right):
    #     output = [ ]

    #     i = 0
    #     j = 0

    #     while i < len(left) and j < len(right): 

    #         if left[i] < right[j]:
    #             output.append(left[i])
    #             i += 1
    #         else:
    #             output.append(right[j]) 
    #             j += 1

    #     # copy the remaining elements to output
    #     output.extend(left[i:])
    #     output.extend(right[j:])

    #     return output

#########________Merge Function_________#############
def merge(left, right):
    output = [ ]

    i = 0
    j = 0

    while i < len(left) and j < len(right): 

        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j]) 
            j += 1

    # copy the remaining elements to output
    output.extend(left[i:])
    output.extend(right[j:])

    return output

merge_result = merge([4, 5], [2, 3, 7, 9])
print(merge_result)

#_________________Merge_Sort()_______________#
# function to perform merge sort
def merge_sort(lst):
    
    # base condition:recursion ends if the length of the list is 1 or less
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2

    # get the left half of the list and further divide it u
    left_partition = merge_sort(lst[: mid])
    right_partition = merge_sort(lst[mid: ])

    # start merging
    return merge(left_partition, right_partition)

def merge(left, right):
    output = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    # append the remaining element
    output.extend(left[i:])
    output.extend(right[j:])

    return output

data_list = [6, 8, 1, 4, 5, 3, 7]
print(f"Unsorted: {data_list}")

result = merge_sort(data_list)

print(f"Sorted: {result}")