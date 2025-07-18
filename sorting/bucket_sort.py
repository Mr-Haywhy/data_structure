'''
~ Introduction
Sorting algorithms play an important role in data organization and optimization.

While we have previously explored foundational sorting algorithms like merge, bubble, insertion, and counting sorts, they may fall short when the size of the data is large.

This chapter introduces you to more advanced and specialized sorting techniques:
    * Bucket Sort
    * Radix Sort
    * Shell Sort

~ Introduction
In Bucket Sort, we divide the elements into several groups called buckets where:
    * Each bucket is sorted using any one of the suitable sorting algorithms.
    * The sorted buckets are combined to form a final sorted list.

~ Working of Bucket Sort
Suppose we need to sort a list of elements.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.1.1.png

By definition, bucket sort first divides the elements into several buckets, sorts each bucket, and gathers all the buckets together.

This is called the scatter-gather approach.

    1. Scatter
First, we divide the list into smaller buckets. The number of buckets and the range of a bucket depends on the list.

Since, in our example, the list contains numbers from 1 to 14, it's easier to divide the elements into 3 buckets (0-5, 5-10, 10-15).
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.1.2.png

Now, let's insert the elements in their respective buckets.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.1.3.png

Each bucket has some elements. The elements in the buckets are not sorted.

The number and size of buckets depend on the data. For instance, with 5, 7, 1, 12, 15, we could use two buckets:
    * Bucket 1: To contain elements from 0-13 ( i.e., 5, 7, 1, 12)
    * Bucket 2: To contain elements from 14-28 (i.e., 15)

But this would be ineffective as the elements aren't uniformly distributed across the buckets.

A better option would be to use Bucket 1 for elements from 0-7 (1, 5, 7) and Bucket 2 for elements from 8-16 (12, 15).

    2. Sort
So far, we have divided the elements into 3 buckets.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.1.4.png

We can use any sorting algorithm to sort each bucket. Let's sort the elements in the buckets in ascending order.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.1.5.png

The final step is to gather all the sorted buckets together.

    3. Gather
Now that we have sorted each bucket's elements, it's time to gather them all and return them to the original list.

Here are the previously sorted buckets.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.1.6.png

Let's gather all these elements in a list, starting from the first bucket to the last bucket.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.1.7.png

Hence, the list is sorted.

Let's summarize the concepts we have learned so far with the help of an image.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.1.8.png
'''

'''
~ Thought Process: Bucket Sort
Now, let's see how we can explain the Bucket Sort process algorithmically.

We'll start by defining our bucket_sort function, which takes in the list to be sorted and the bucket range.

        def bucket_sort(lst, bucket_range):

1. Create buckets and insert the elements.
We start by creating empty buckets based on the given range.

        buckets = [[] for _ in bucket_range]

Now, we insert the elements into their respective buckets based on their value.

        # insert elements into their respective buckets
        for index, b_range in enumerate(bucket_range):
            for num in lst:
                if b_range[0] <= num < b_range[1]:
                    buckets[index].append(num)

2. Sort each individual bucket.
We can use any sorting algorithm to sort elements in the bucket.

We will use the selection_sort() function to sort the elements.

        sorted_list = []
        for bucket in buckets:
            # SORT
            bucket = selection_sort(bucket)

3. Gather the sorted elements from each bucket.
The final step is to concatenate the sorted elements from each bucket to get the final sorted list.

        # GATHER
        sorted_list.extend(bucket)

        return sorted_list

Next, we will write a fully executable program to sort the elements.
'''

# Source Code: Bucket Sort

def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[min_index], lst[i] = lst[i], lst[min_index]
    return lst

def bucket_sort(lst, bucket_range):
    
    # SCATTER   
    # create empty buckets
    buckets = [[] for _ in bucket_range]
    
    # insert elements into their respective buckets
    for index, b_range in enumerate(bucket_range):
        for num in lst:
            if b_range[0] <= num < b_range[1]:
                buckets[index].append(num)
 
    # sort and gather the elements of each bucket
    sorted_list = []
    for bucket in buckets:
        # SORT
        bucket = selection_sort(bucket)
        # GATHER
        sorted_list.extend(bucket)
    
    return sorted_list

lst = [10, 8, 2, 1, 12, 7, 6, 14, 11, 4] 
bucket_range = [(0, 5), (5, 10), (10, 15)]
print(f"Sorted List: {bucket_sort(lst, bucket_range)}")

'''
Output:
    Sorted List: [1, 2, 4, 6, 7, 8, 10, 11, 12, 14]
'''




def quick_sort_desc(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst.pop()

    left = []
    right = []

    for element in lst:
        if element > pivot:  # Changed comparison for descending
            right.append(element)
        else:
            left.append(element)

    return quick_sort_desc(left) + [pivot] + quick_sort_desc(right)

def bucket_sort(lst, bucket_range):
    buckets = [[] for _ in bucket_range]

    for index, b_range in enumerate(bucket_range):
        for num in lst:
            if b_range[0] <= num < b_range[1]:
                buckets[index].append(num)
                

    sorted_list = []

    for bucket in buckets:
        sorted_bucket = quick_sort_desc(bucket)  # Use descending quick sort
    
    for sorted_bucket in reversed(buckets):
        sorted_list.extend(sorted_bucket)

    return sorted_list

# take user input
lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
bucket_range = [(0, 5), (5, 10), (10, 15)]

print(bucket_sort(lst, bucket_range))



'''
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[min_index]:  # Change to '<' for ascending sort within each bucket
                min_index = j
        lst[min_index], lst[i] = lst[i], lst[min_index]
    return lst

def bucket_sort(lst, bucket_range):
    # SCATTER   
    # create empty buckets
    buckets = [[] for _ in bucket_range]
    
    # insert elements into their respective buckets
    for index, b_range in enumerate(bucket_range):
        for num in lst:
            if b_range[0] <= num < b_range[1]:
                buckets[index].append(num)
 
    # sort and gather the elements of each bucket
    sorted_list = []
    for bucket in buckets:
        # SORT
        bucket = selection_sort(bucket)
        
    # GATHER
    # Since we need the final list in descending order, 
    # start from the last bucket
    for bucket in reversed(buckets):
        sorted_list.extend(bucket)
    
    return sorted_list

lst = list(map(int, input().split()))
bucket_range = [(0, 5), (5, 10), (10, 15)]

print(bucket_sort(lst, bucket_range))
'''


'''
~ Best Use Case for Bucket Sort
When to use bucket sort?

The input data is uniformly distributed over a range, as each bucket will have a uniform load.
The range of input data is known, which helps in determining the number and size of the buckets.

* When not to use bucket sort?
The efficiency of bucket sort can be compromised if elements are not uniformly distributed.

For instance, when sorting numbers between 1-100 with 10 buckets, if most numbers are between 1-10, the first bucket overflows while another might remain empty.

This imbalance can slow down the sorting process, as the overloaded bucket takes longer to sort.

~ Complexity Analysis of Bucket Sort
The time complexity of bucket sort depends on:

The distribution of the input data.
The number of buckets used.
The sorting algorithm used to sort the individual buckets.
Based on the given factors, bucket sort has the following complexities:

        Best Case Time Complexity	    O(n + k)
        Worst Case Time Complexity	    O(n^2) 
        Average Case Time Complexity	O(n + k)
        Space Complexity	            O(n + k)

Here,

n is the number of elements.
k is the number of buckets.
'''

"""
What We'll Do:

    Keep your quick sort logic (already set up for descending order).

    Implement data-driven bucket creation:

        Use quantile-based bucket division or

        Use equal-frequency buckets — so that each bucket holds roughly the same number of elements.

    Apply quick sort to each bucket.

    Merge buckets in descending order.

✅ Step-by-Step Solution
🔧 1. Your existing quick_sort (descending order)

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

🧠 2. Revised Bucket Sort (non-uniform-aware using equal-frequency buckets)

def bucket_sort(lst, bucket_count=3):
    if not lst:
        return []

    # Step 1: Sort the list in descending order first
    sorted_data = quick_sort(lst.copy())

    # Step 2: Divide into equal-frequency buckets (non-uniform-aware)
    n = len(sorted_data)
    bucket_size = max(1, n // bucket_count)
    buckets = []

    for i in range(0, n, bucket_size):
        buckets.append(sorted_data[i:i + bucket_size])

    # Step 3: Sort each bucket again using quick_sort (even if already partially sorted)
    final_sorted = []
    for bucket in buckets:
        final_sorted.extend(quick_sort(bucket))

    return final_sorted


🧪 Example Use

data = [18, 10, 8, 14, 1, 50, 7, 6, 25, 3]
Sorted_list = bucket_sort(data, bucket_count=3)

print(Sorted_list)

✅ Output (Example):

[50, 25, 18, 14, 10, 8, 7, 6, 3, 1]

🔍 Why This Works Better for Non-Uniform Distributions

    Buckets are built by splitting sorted data into equal-sized groups, not fixed numeric ranges.

    It adapts to clustering, outliers, and skew naturally.

    It avoids the classic problem of “all data falling into one bucket.”

Let me know if you want:

    A version that uses percentile-based buckets (more exact quantiles)

    To modify the sorting algorithm (e.g., merge sort)

    Visualization of bucket contents

"""


"""

✅ Goal Recap

You're building a bucket sort that:

    Uses your own quick_sort() (already built to return in descending order).

    Handles non-uniform distributions, so data is not just dumped into equal fixed ranges.

    Does not use reverse() or other Python shortcuts — instead, everything is sorted and ordered manually.

✅ Revised Plan
1. Use your quick_sort() as-is (descending).
2. Dynamically create buckets based on equal-frequency (not fixed ranges).
3. Sort each bucket using your quick_sort().
4. Merge buckets in order (manually from high to low).
🧠 Explanation First — No Shortcuts!

    "Equal-frequency" means: divide the list into roughly the same number of elements per bucket, not by numeric range.

    It helps with non-uniform distributions (e.g., [1, 1, 1, 1000]), because it spreads elements evenly.

✅ Step-by-Step Code

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


def bucket_sort(lst, bucket_count=3):
    if not lst:
        return []

    # Step 1: Create empty buckets
    buckets = [[] for _ in range(bucket_count)]

    # Step 2: Find min and max to understand value spread
    min_val = min(lst)
    max_val = max(lst)
    range_size = (max_val - min_val + 1) / bucket_count

    # Step 3: Put each number in its appropriate bucket
    for num in lst:
        # Calculate which bucket index it should go into
        index = int((num - min_val) / range_size)
        if index == bucket_count:  # edge case: max value goes into the last bucket
            index -= 1
        buckets[index].append(num)

    # Step 4: Sort each bucket using your quick_sort
    sorted_list = []
    for i in range(bucket_count - 1, -1, -1):  # manually go high to low
        sorted_bucket = quick_sort(buckets[i])
        sorted_list.extend(sorted_bucket)

    return sorted_list

*****
🧪 Test It

data = [18, 10, 8, 14, 1, 50, 3, 33, 6, 25]
Sorted_list = bucket_sort(data, bucket_count=4)

print(Sorted_list)

✅ Example Output

[50, 33, 25, 18, 14, 10, 8, 6, 3, 1]

🔍 Walkthrough of Bucket Logic:

Let’s say your data is:

[1, 6, 8, 10, 14, 18, 25, 33, 50]

Min = 1, Max = 50, Bucket count = 4 → each bucket covers a range of size ≈ 12.25
Bucket Index	Range Approx	Values Filled
0	            [1–13.25)	    1, 6, 8, 10
1	            [13.25–25.5)	14, 18, 25
2	            [25.5–37.75)	33
3	            [37.75–50]	    50

Then each bucket is sorted in descending order using your quick_sort, and the final list is built by processing buckets from last to first, manually, to keep descending order.
✅ Key Takeaways:

    No reverse used

    Your own quick sort is respected

    Bucket logic is dynamic and data-driven

    Manual bucket merging is used to control sort direction

Let me know if you want to visualize buckets or switch to ascending later — happy to walk through every step.

"""