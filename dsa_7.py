# Thought Process to Implement Quick Sort
# Now, let's see how we can implement quick sort. We'll create a function named quick_sort() that takes a list lst as its parameter.

# 1. Check for base condition and determine the pivot.
    # We return the list if it contains one or zero elements. Else, we use the final element as the pivot.
            # length = len(lst)

            # # base condition     
            # if length <= 1:
            #     return lst
            # else:
            #     # pop() returns the last element of the list
            #     pivot = lst.pop()
    
    # Note that we've removed the pivot from the list using the pop() method because we need to insert it in a different position.

# 2. Place the elements into the greater and lesser sublists.
            # # two sublists to hold elements
            # # greater and smaller than pivot        
            # right = []
            # left = []

            # # iterate through list elements    
            # for element in lst:
                
            #     # check if element is greater than pivot
            #     if element > pivot:

            #         # add element to right list
            #         right.append(element)
                    
            #     else:

            #         # add element to left list
            #         left.append(element)

# 3. Call the function recursively to merge the two sublists.
            # return quick_sort(left) + [pivot] + quick_sort(right)
# Here, the return statement recursively calls quick_sort(left) and quick_sort(elements greater).
# As a result, the list gets broken down into smaller and smaller pieces until the list contains a single element.
    # Then, the return statement appends 3 lists in the following order:
        # the list with the smaller values
        # the [pivot] list consisting of only the pivot element
        # the list with the greater values

# Thus, the lists get sorted and merged with each recursion, until a fully sorted list is returned by the function

#.........................Quick Sort...........................#
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst.pop()

    right = []
    left = []

    for element in lst:
        if element > pivot:         # Assending order
        # if element < pivot:       # descending order
            right.append(element)
        else:
            left.append(element)

    return quick_sort(left) + [pivot] + quick_sort(right)

list_1 = [7, 2, 1, 6, 8, 5, 3, 4]

sorted_list = quick_sort(list_1)

print(sorted_list)