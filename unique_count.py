# Create a program to find the number of unique elements in a list.
# Assumption: The input list will only contain non-negative integers


def count_unique_elements(lst):
    if len(lst) <= 1:
        return lst
    
    max_element = max(lst)
    counting_list = [0] * (max_element + 1)

    for num in lst:
        counting_list[num] += 1

    unique_count = 0

    for value in counting_list:
        if value >= 1:
            unique_count += 1

    return unique_count

list = [2, 2, 3, 4, 6, 3, 7, 8]
sorted_list = count_unique_elements(list)
print(sorted_list)