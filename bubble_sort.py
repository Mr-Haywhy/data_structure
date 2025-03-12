# Bubble sort implementation in Python

list_1 = [1,19,20,5,2,7]
size = len(list_1)

for i in range(size):
    for j in range(size-1):
        if list_1[j] > list_1[j + 1]:
            list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]

# print(list_1)


# bubble sort function
def bubble_sort(list_item):
    # Get the length of the list
    size = len(list_item)

    # Outer loop to access each list element
    # Outer loop controls the number of passes
    for each_list_element in range(size):
        
        # Variable to track swapping
        swapped = False


        # Inner loop to compare list elements
        for compare_list_element in range(size - 1 - each_list_element):

            # Swap element if necessary
            if list_item[compare_list_element] > list_item[compare_list_element + 1]:
                list_item[compare_list_element], list_item[compare_list_element + 1] = list_item[compare_list_element + 1], list_item[compare_list_element]

                print(list_item)
            # # To use this bubble sort to sort a list in descending order 
            # if list_item[compare_list_element] < list_item[compare_list_element + 1]:
            #     list_item[compare_list_element + 1], list_item[compare_list_element] = list_item[compare_list_element], list_item[compare_list_element + 1]

            # Change the swapped variable to True if swapping occurs
                swapped = True
                
        # If swapping doesn't occur, the list is sorted
        # Terminate the loop when sorted 
        if not swapped:
            break
    
    return(list_item)

# Our function is ready to sort your data.

data_set = [1,19,20,5,2,7]

sorted_list = bubble_sort(data_set)

print(f"Sorted data set {sorted_list}")