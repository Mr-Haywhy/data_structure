# Insertion sort works by repeatedly
    # 1. taking an element from the unsorted portion of the list
    # 2. and inserting it into its correct position within the already-sorted portion
# Suppose we need to sort this list: [74132]
# To sort this list in ascending order, we follow these steps:
# 1. Divide the list into sorted and unsorted sublists.
    
    # key = lst[i]

# 2. Set the first unsorted element as the key element.
# 3. We'll compare the key with the sorted sublist (moving from right to left) and insert it into its correct position. i.e 'compare the key element with the element to its left. if the key is smaller, swap'
    
    # Let i be the index of the key
    # key = lst[i]
    # j = i -1

    # compare the key element with elements to its left one by one
    # end the loop if the key element is larger or equal 
    # while key <= lst[j] and j >= 0:

        # shift the element to its right
        # lst[j + 1] = lst[j]

        # decrease j to go to the next element to its left
        # j = j - 1

    # Insert the key elemrnt at the correct position
    # lst[j + 1] = key

# 4. Repeat step 3 for all the elements of the unsorted part.
#   NOTE: if the key is larger or equal to the element to its left, we stop the comparison because the element is already in the correct position.

def insertion_sort(lst):
    # Iterate from index 1 to the last index.
    for i in range(1, len(lst)):
        # key element
        key = lst[i]
        j = i - 1

        # compare the key element with elements to its left one by one.
        # end the loop if the key element is larger or equal to the element to its left.
        # this while loop sort the data set in ascending order
        # while j >= 0 and key <= lst[j]:
            # to sort the data in a descending order adjust the while loop to be:
        while j >= 0 and key >= lst[j]:
            # shift the element to its right
            lst[j + 1] = lst[j]

            # decrease j to go to the next element to its left
            j = j - 1

        # insert the key element at the correct position
        lst[j + 1] = key
        print(f"Sort Process: {lst}")
    return lst

data =  [7, 4, 1, 3, 2]

print(f"Unsorted List: {data}")
sorted_list = insertion_sort(data)
print(f"Sorted List: {sorted_list}")