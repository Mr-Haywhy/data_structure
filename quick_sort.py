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