def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2

    left_part = merge_sort(lst[: mid])
    right_part = merge_sort(lst[mid :])

    return merge(left_part, right_part)

def merge(left, right):
    output = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])

    return output

data_list = [2, 15, 20, 10, 1, 4, 6, 40]

sorted_list = merge_sort(data_list)

print(sorted_list)