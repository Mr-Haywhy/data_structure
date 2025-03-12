#  SORTING ALGORITHM

# Sorting is the process of arranging elements in a particular order, most commonly either in ascending or descending order.

# Suppose you have a list of numbers, as shown below:

numbers = [12, -4, 56, 67, 10]

# You can quickly sort those elements using the list's sort() method.

numbers = [12, -4, 56, 67, 10]
numbers.sort()  

print(f"Sort using the sort() function: {numbers}")

# DIFFERENT SORTING ALGORITHIMS

# Each algorithm offers different levels of efficiency, depending on the dataset and its use case.
# Bubble Sort
# Selection Sort
# Insertion Sort
# Merge Sort
# Quick Sort
# Counting Sort

# The first three sorts in the above list are comparison-based sorting algorithms that work by comparing two elements and swapping them if necessary

# BUBBLE SORT
# Bubble sort works by repeatedly comparing two adjacent elements and swapping them if they are not in the correct order.

# To implement bubble sort in python:
# 1. Compare an element with its next element and swap them if necessary.

# if lst[j] > lst[j + 1]:
#     # swap elements       
#     lst[j], lst[j + 1] = lst[j + 1], lst[j]

# 2. Repeat Step 1 for each element in the list using a loop.
# Since we are comparing each element to its next element, we only need to run the loop up to the second-last element.

# This is because the last element will not have a next element for comparison.

# size = len(lst)

# for j in range(size - 1):
#     if lst[j] > lst[j + 1]:
#         lst[j], lst[j + 1] = lst[j + 1], lst[j]

# 3. Repeat Step 2 for each element in the list.
# Repeat the above steps for each position. With each iteration of the outer loop, one element will settle in its correct position, starting from the largest element.

lst = [12, -4, 70, 67, 10]

# Check the length of the list
size = len(lst)

# Pass the index of the item to be compared.
for i in range(size):  
    
    # Compare the pairing elements
    for j in range(size - 1): 

        # Compare an element with its next element and swap them if necessary
        if lst[j] > lst[j + 1]:   
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
        
    print(j)
print(f"Sorted using bubble sort wihout function: {lst}")

# In this snippet, _len(lst)_ determines the length of the list called lst. 
# Bubble Sort compares adjacent elements, so we loop through the list with two nested loops. 
# The outer loop _i_ determines the pass number, and the inner loop _j_ takes care of comparing pairs of elements.

# Each time it finds lst[j] greater than lst[j + 1], they swap positions in just one neat line with lst[j], lst[j + 1] = lst[j + 1], lst[j]. This helps to bring the larger elements to move towards the end.

# Once you've grasped this, try experimenting by adding print statements to see each step in action! Happy coding!

# Bubble Sort function


def bubble_sort(list_data):
    
    size = len(list_data)

    # Outer loop to access each list element
    # Outer loop controls the number of passes
    for i in range(size):
        
        # Inner loop to compare list elements
        for j in range(size - 1 - i):

            # Swap elements if necessary
            if list_data[j] > list_data[j + 1]:

                # Interchange this line for descending order sorting {[j+1] to [j]}
                list_data[j], list_data[j + 1] = list_data[j + 1], list_data[j]

    return(list_data)

data_set = [10, 15, 2, 1, 0, -1, 50, 0.5]
print(f"Unsorted List: {data_set}")

sorted_list = bubble_sort(data_set)

print(f"Sorted List using bubble sort function: {sorted_list}")


# Optimizing our inner loop so that the inner loop does not iterate to the second to the last item on the list after sorting the largest item.
# for i in range(size):
    # # Reduces comparison range by i in each pass
    # # Before: range(size - 1)
    # # After: range(size -1 - i)
    # for j in range(size -1 - i):



# When not to use bubble sort?
# * Avoid bubble sort for large datasets and performance-critical applications.
# * In such cases, sorting algorithms like merge sort or quick sort are more suitable.