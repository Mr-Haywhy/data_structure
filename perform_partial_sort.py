def perform_partial_sort(lst, n):

    # iterate only till the n-th element
    for step in range(1, n):
        key = lst[step]
        j = step - 1

        # compare the key element with the elements to its left one by one
        # end the loop if the key element is larger or equal
        while j >= 0 and key <= lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1

        lst[j + 1] = key
        print(lst)

    return lst[:n]

list = [7, 4, 1, 3, 2]
n = 3
sorted_partial_list = perform_partial_sort(list, n)

print(sorted_partial_list)