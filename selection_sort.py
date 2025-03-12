def selection_sort(list_d):
    # assume the first to be the smallest in the list
    for i in range(len(list_d)):
        min_index = i
        # iterate over unsorted elements
        for j in range(i + 1, len(list_d)):
            # find index of the smallest element
            # in the unsorted part of the list
            if list_d[j] < list_d[min_index]:
                min_index = j
        # swap the smallest element with the first element
        # of the unsorted part 
        list_d[min_index], list_d[i] = list_d[i], list_d[min_index]

    return list_d

selection_sort()