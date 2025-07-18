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