def count_occurrence(lst, n):
    if len(lst) <= 1:
        return lst
    
    count = 0

    # loop through the element of the list
    for element in lst:
        if element == n:
            # increment count if a match is found
            count += 1

    return count

count_occurrence()