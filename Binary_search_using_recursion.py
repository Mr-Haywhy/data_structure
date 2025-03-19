# Binary Search Using Recursion
def binary_search_rec(lst, target, low, high):

    if high >= low:
        mid = (high + low) // 2

        if lst[mid] == target:
            return mid

        elif lst[mid] > target:
            return binary_search_rec(lst, target, low, mid - 1)

        else:
            return binary_search_rec(lst, target, mid + 1, high)

    else:
        return None