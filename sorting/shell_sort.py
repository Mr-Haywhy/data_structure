'''
~ Introduction
Shell sort is a sorting algorithm specifically designed to handle large datasets by improving the efficiency of insertion sort.

~ Working of Shell Sort
Suppose we need to sort the following list:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.3.1.png

1.1. Create sublists by selecting elements at a fixed interval.

In Shell sort, the interval or gap refers to the distance between elements that are compared and potentially swapped.

Since the length of our list is 8, let our starting interval be 8/2 = 4. This means that a sublist starting from the 0th index will have elements at the 4th, 8th, 12th …indices.

Since we only have eight elements in our list, our first sublist will contain elements from the 0th and 4th indices.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.3.2.png

The sublists are sorted with insertion sort, and their elements are reinserted into the original list in the sorted order.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.3.3.png

1.2. Repeat the process for all remaining elements.
After sorting sublists from the 0th element, we proceed to sort new sublists of four-element intervals starting from the 1st element, i.e., 1st and 5th.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.3.4.png

Now, we repeat the same process for the 2nd and 6th elements.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.3.5.png

Finally, we take a sublist of the 3rd and 7th elements.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.3.6.png

The first loop with interval 4 is complete, and the list is more organized than before.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.3.7.png

In shell sort, the gap is reduced in each iteration to progressively bring elements nearer to their final positions, enhancing efficiency.

So now, we'll reduce the interval by half in the next iteration.

2.1. Reduce the gap.
Let our new interval be half of the previous one, i.e., 2.

2.2. Compare and sort based on the interval.
We have the following semi-sorted list:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.3.8.png

Now, we'll create a sublist of elements at an interval of 2 starting from the 0th index.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.3.9.png

Now, let's sort this sublist using insertion sort. Then, we insert the elements of this sorted sublist back into the original list in the corresponding order.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.3.10.png

2.3. Repeat for the rest of the elements.
Now, we'll create a sublist of elements at an interval of 2 starting from the 1st index.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.3.11.png

Now, let's sort this sublist using insertion sort and insert the elements in the list in sorted order.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.3.12.png

The loop with interval 2 is complete.

Finally, we will reduce the interval to 1 and repeat the same process to get the final sorted list.

Now Let's sort our list using insertion sort at an interval 1.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.3.13.png

This list is now fully sorted.

After interval-based sorting, our list now had the smaller elements far closer to the start than at the end.

Only 1, 5, and 8 were out of place and need to be shifted by only one place each.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.3.14.png

So when we performed insertion sort with an interval of 1 (i.e., the entire list), it required far less shifting than it would have previously needed.

~ Intervals in Shell Sort
In the above example, we reduced the interval in half. However, we can also use other sequences to reduce the interval.

Some optimal sequences that can be used in the Shell sort algorithm are:
    * Shell's original sequence: N/2 , N/4 , …, 1
    * Knuth's increments: 1, 4, 13, …, (3k – 1) / 2
    * Sedgewick's increments: 1, 8, 23, 77, 281, 1073, 4193, 16577...4j+1+ 3·2j+ 1
    * Hibbard's increments: 1, 3, 7, 15, 31, 63, 127, 255, 511…
    * Papernov & Stasevich increments: 1, 3, 5, 9, 17, 33, 65,...
    * Pratt Sequence: 1, 2, 3, 4, 6, 9, 8, 12, 18, 27, 16, 24, 36, 54, 81....

NOTE: The performance of Shell sort depends on the type of sequence used for a given input list.
'''

'''
Thought Process: Shell Sort
1. Define the initial interval.

        interval = n//2

2. Perform insertion sort for a given interval.

        insertion_sort(lst, interval)

3. Reduce the interval after completing the insertion sort for the current interval.

        interval //= 2

NOTE: We're using Shell's sequence.

4. Repeat as long as the interval is greater than 0.

        while interval > 0:
        

Recap: Insertion Sort
This is what insertion sort looks like.

        def insertion_sort(lst):
            for i in range(1, len(lst)):
                key = lst[i]   
                j = i - 1  
                while j >= 0 and key < lst[j]:
                    lst[j + 1] = lst[j]
                    j = j - 1
                lst[j + 1] = key

Insertion sort can be viewed as Shell sort with interval 1.

For interval, we can modify this as:

        def insertion_sort(lst, interval):
            for i in range(interval, len(lst)):
                key = lst[i]            
                j = i - interval          
                while j >= 0 and key < lst[j]:
                    lst[j + interval] = lst[j]
                    j = j - interval    
                lst[j + interval] = key

Next, we will see a complete example of shell sort.
'''

# Source Code: Shell Sort
def insertion_sort(lst, interval):
    for i in range(interval, len(lst)):
        key = lst[i]            
        j = i - interval          
        while j >= 0 and key < lst[j]:
            lst[j + interval] = lst[j]
            j = j - interval    
        lst[j + interval] = key

def shell_sort(n):
    # rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        insertion_sort(lst, interval)
        interval //= 2

lst = [9, 8, 3, 7, 5, 6, 4, 1]
size = len(lst)

# function call
shell_sort(size)
print(f"Sorted List: {lst}")


'''
Complexity Analysis of Shell Sort
Shell sort is an unstable sorting algorithm because it does not examine the elements lying between the intervals.

In the worst case, its time complexity becomes O(n∗(log(n))^2).

Here's a summary of the various complexities of Shell sort:

    Best Case Time Complexity	    O(n log⁡n)
    Worst Case Time Complexity	    O(n^2) 
    Average Case Time Complexity    O(n^1.5) to O(n logn)
    Space Complexity	            O(1)
'''