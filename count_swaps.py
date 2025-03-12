
def count_swaps(lst):
    
    # set number of swaps to 0
    swaps = 0
    
    for i in range(len(lst)):
        min_index = i

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        # swap only if lst[i] and lst[min_index] are not equal     
        if lst[i] != lst[min_index]:
            lst[min_index], lst[i] = lst[i], lst[min_index]

            # increment the swaps variable
            swaps += 1
            
    return swaps

# take integer inputs and convert it to a list
data = list(map(int, input().split()))

result = count_swaps(data)

print(result)