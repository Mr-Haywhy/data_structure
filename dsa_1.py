#
# Sum of Natural Numbers

def calculate_sum(n):
    total = 0

    for i in range(n+1):
        total += i
    
    return total

result = calculate_sum(100)

print(result)

#
# Rewriting the code up here in an optimized way
#

def calculate_sum_opt(j):
    return j * (j + 1) // 2

opt_result = calculate_sum_opt(100)

print(opt_result)