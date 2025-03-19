# NOTE: Since counting sort uses the indexes of a list for sorting, it cannot be used for floating-point numbers.

# Thought Process to Implement Counting Sort
# # 1. Find the largest element and create the counting list.

        # max_element = max(lst)
        # # create a list and initialize all its elements to 0 
        # counting_list = [0] * (max_element + 1)

# 2. Count the occurrences of the elements in the unsorted list.

        # for num in lst:
        #     counting_list[num] += 1

# 3. Fill out the sorted list according to the value stored in the index of counting_list.

        # sorted_output = []

        # for index, value in enumerate(counting_list):
        #     sorted_output.extend([index] * value)

def counting_sort(lst):
    # if list is empty or has one element, return itself
    if len(lst) <= 1:
        return lst
    
    # find the largest element
    max_element = max(lst)
    # create a list and initialize all its elements to 0
    counting_list = [0] * (max_element + 1)
    # print(counting_list)

    # fill the counting list with frequency of each number
    for num in lst:
        counting_list[num] += 1
    # print(num)

    # # create the sorted output list
    sorted_output = []

    # # sorting ascending order
    for index, value in enumerate(counting_list):
        sorted_output.extend(value * [index])

    # sorting descending order
    # for index in range(len(counting_list) - 1, -1, -1):
    #     sorted_output.extend([index] * counting_list[index])
    
    # print(value)

    return sorted_output


list = [2, 2, 3, 4, 6, 3, 7, 8]
sorted_list = counting_sort(list)
print(sorted_list)