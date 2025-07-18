def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst.pop()

    right = []
    left = []

    for element in lst:
        if element > pivot:
            right.append(element)
        else:
            left.append(element)
    return quick_sort(left) + [pivot] + quick_sort(right)

data = [18, 10, 8, 14, 1]
Sorted_list = quick_sort(data)

print(Sorted_list)



def quick_sort_desc(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst.pop()

    right = []
    left = []
    

    for element in lst:
        if element > pivot:
            left.append(element)  # Larger values to the left
        else:
            right.append(element)  # Smaller values to the right

    return quick_sort_desc(left) + [pivot] + quick_sort_desc(right)

data = [18, 10, 8, 14, 1]
sorted_list = quick_sort_desc(data)

print(sorted_list)