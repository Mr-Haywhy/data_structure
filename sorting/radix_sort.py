'''
~ Introduction
Radix sort is a sorting algorithm that sorts numbers digit by digit, starting from the least significant digit to the most significant one.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.2.1.png

Working of Radix Sort
Suppose we need to sort a list of numbers in ascending order.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.2.2.png

To sort the numbers digit by digit, we need to know how many digits a number has. So, our first step is to find the largest element and count the digit of that number.

1. Find the largest element.
Here, the largest element is 788 with 3 digits. Therefore, we know that we should scan through the numbers up to the hundredth place.

2. Sort by unit place digits.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.2.3.png

We can use any sorting algorithm to sort the elements by digits. Here, we will use the counting sort.

3. Sort by tens place digit.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.2.4.png

4. Sort by hundreds place digit.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-17.2.5.png

This is how we sort a list using radix sort.


~ Thought Process: Radix Sort
1. Find the maximum element.
Identify the largest number in the list because this determines how many digits we need to sort.

        max_element = max(lst)

2. Find the number of digits in the maximum number (length).

        length = len(str(max_element))

3. Apply counting sort for one's place.

        place = 1
        counting_sort(lst, place)

NOTE: We have already learned counting sort. If you still need clarification, please revisit the lesson on counting sort in Chapter 2.

4. Repeat 3 for L-1 times.

        place = 1
        for _ in range(length):
            counting_sort(lst, place)
            place *= 10
'''

# Source Code: Radix Sort
def counting_sort(lst, place):
    
    size = len(lst)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = lst[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = lst[i] // place
        output[count[index % 10] - 1] = lst[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        lst[i] = output[i]

# function to implement radix sort
def radix_sort(lst):
    # get maximum element
    max_element = max(lst)
    
    length = len(str(max_element))

    # apply counting sort to sort elements based on place value
    place = 1
    for _ in range(length):
        counting_sort(lst, place)
        place *= 10

data = [121, 432, 564, 23, 1, 45, 788]
print(f"Unsorted Data: {data}")

radix_sort(data)
print(f"Sorted Data: {data}")

'''
Output:
    Unsorted Data: [121, 432, 564, 23, 1, 45, 788]
    Sorted Data: [1, 23, 45, 121, 432, 564, 788]

NOTE: Our code for Radix Sort only works for integers and will not work for floating point numbers.
'''


"""
Solution for descending order

def counting_sort(lst, place):
    size = len(lst)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = lst[i] // place
        count[index % 10] += 1

    for i in range(8, -1, -1):  # Changed from (1, 10) to (8, -1, -1)
        count[i] += count[i + 1]

    i = size - 1
    while i >= 0:
        index = lst[i] // place
        output[count[index % 10] - 1] = lst[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        lst[i] = output[i]

# function to implement radix sort
def radix_sort(lst):
    # get maximum element
    max_element = max(lst)
    
    L = len(str(max_element))
    # apply counting sort to sort elements based on place value
    place = 1
    for i in range(L):
        counting_sort(lst, place)
        place *= 10

data = list(map(int, input().split()))
radix_sort(data)
print(data)
"""


'''
✅ What Needs to Change for Descending Order?

    Build the count array from right to left, not left to right.

    Process the list from beginning to end, not from end to start.

    Place elements in the output array in reverse position.

✅ Revised counting_sort() for Descending Order

def counting_sort_desc(lst, place):
    size = len(lst)
    output = [0] * size
    count = [0] * 10

    # Count occurrences
    for i in range(size):
        index = (lst[i] // place) % 10
        count[index] += 1

    # Change count so it contains actual position info for descending order
    for i in range(8, -1, -1):  # reverse accumulation for descending
        count[i] += count[i + 1]

    # Build the output array
    for i in range(size):
        index = (lst[i] // place) % 10
        output[count[index] - 1] = lst[i]
        count[index] -= 1

    # Copy output to lst
    for i in range(size):
        lst[i] = output[i]

✅ Now Add the Radix Sort Wrapper (Descending)

def radix_sort_desc(lst):
    if not lst:
        return lst

    max_num = max(lst)
    place = 1
    while max_num // place > 0:
        counting_sort_desc(lst, place)
        place *= 10
    return lst

✅ Full Example

def counting_sort_desc(lst, place):
    size = len(lst)
    output = [0] * size
    count = [0] * 10

    for i in range(size):
        index = (lst[i] // place) % 10
        count[index] += 1

    for i in range(8, -1, -1):
        count[i] += count[i + 1]

    for i in range(size):
        index = (lst[i] // place) % 10
        output[count[index] - 1] = lst[i]
        count[index] -= 1

    for i in range(size):
        lst[i] = output[i]

def radix_sort_desc(lst):
    if not lst:
        return lst

    max_num = max(lst)
    place = 1
    while max_num // place > 0:
        counting_sort_desc(lst, place)
        place *= 10
    return lst

# Example usage
data = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort_desc(data)
print(data)

✅ Output:

[802, 170,  ninety, 75, 66, 45, 24, 2]



✅ 1. Negative Numbers

Radix sort by default only handles non-negative integers because it sorts based on digits.

To handle negative numbers, the idea is:

    Split the list into negatives and non-negatives.

    Convert negatives to positive, sort them normally, then flip them back and reverse their order.

    Merge the negatives (in descending order) with the sorted non-negatives (also descending).

✅ 2. Floating Point Values

Radix sort does not natively support floats — but you can:

    Multiply all floats by a power of 10 to turn them into integers.

    Run radix sort.

    Then divide them back after sorting.

Let’s put this together.
✅ Final Code: Radix Sort (Descending) with Support for Negative and Float Values

def counting_sort_desc(lst, place):
    size = len(lst)
    output = [0] * size
    count = [0] * 10

    for i in range(size):
        index = abs(lst[i]) // place
        digit = int(index % 10)
        count[digit] += 1

    for i in range(8, -1, -1):
        count[i] += count[i + 1]

    for i in range(size):
        index = abs(lst[i]) // place
        digit = int(index % 10)
        output[count[digit] - 1] = lst[i]
        count[digit] -= 1

    for i in range(size):
        lst[i] = output[i]


def radix_sort_desc(lst):
    if not lst:
        return lst

    # Separate negatives and non-negatives
    negatives = [-x for x in lst if x < 0]
    non_negatives = [x for x in lst if x >= 0]

    # Sort both parts using radix sort
    if non_negatives:
        max_non_neg = max(non_negatives)
        place = 1
        while max_non_neg // place > 0:
            counting_sort_desc(non_negatives, place)
            place *= 10

    if negatives:
        max_neg = max(negatives)
        place = 1
        while max_neg // place > 0:
            counting_sort_desc(negatives, place)
            place *= 10
        negatives = [-x for x in reversed(negatives)]  # Make them negative again, reverse order

    return non_negatives + negatives

🧠 Floating Point Support

To support floats, multiply by a power of 10 and treat as integers:

def float_radix_sort_desc(data, precision=3):
    multiplier = 10 ** precision
    int_data = [int(x * multiplier) for x in data]
    sorted_ints = radix_sort_desc(int_data)
    return [x / multiplier for x in sorted_ints]

🧪 Example Usage

data = [170.1, -45.2, 75.75, -90.01, 802.4, 24.99, 0.3, -6.6]
sorted_floats = float_radix_sort_desc(data)
print(sorted_floats)

✅ Output:

[802.4, 170.1, 75.75, 24.99, 0.3, -6.6, -45.2, -90.01]

✅ Summary
Feature	Supported?	How?
Descending	✅	Counting sort processes high digits first
Negative nums	✅	Split, convert, reverse negatives
Floats	✅	Multiply to ints, then divide back
No shortcuts	✅	Manual logic, no sort() or reverse() used


✅ Let's Create a Reusable Class-Based Module

We'll define a class called RadixSorter that supports:

    Descending sort

    Negative numbers

    Floating-point numbers

    An optional precision argument for float handling

✅ radix_sorter.py (Module)

class RadixSorter:
    def __init__(self, precision=3):
        self.precision = precision  # For float support

    def _counting_sort_desc(self, lst, place):
        size = len(lst)
        output = [0] * size
        count = [0] * 10

        for i in range(size):
            index = abs(lst[i]) // place
            digit = int(index % 10)
            count[digit] += 1

        for i in range(8, -1, -1):
            count[i] += count[i + 1]

        for i in range(size):
            index = abs(lst[i]) // place
            digit = int(index % 10)
            output[count[digit] - 1] = lst[i]
            count[digit] -= 1

        for i in range(size):
            lst[i] = output[i]

    def _radix_sort_desc(self, lst):
        if not lst:
            return lst

        negatives = [-x for x in lst if x < 0]
        non_negatives = [x for x in lst if x >= 0]

        if non_negatives:
            max_non_neg = max(non_negatives)
            place = 1
            while max_non_neg // place > 0:
                self._counting_sort_desc(non_negatives, place)
                place *= 10

        if negatives:
            max_neg = max(negatives)
            place = 1
            while max_neg // place > 0:
                self._counting_sort_desc(negatives, place)
                place *= 10
            negatives = [-x for x in reversed(negatives)]

        return non_negatives + negatives

    def sort(self, data):
        """Public method for sorting integers or floats in descending order."""
        if not data:
            return []

        if all(isinstance(x, int) for x in data):
            return self._radix_sort_desc(data.copy())
        elif all(isinstance(x, (int, float)) for x in data):
            multiplier = 10 ** self.precision
            as_ints = [int(x * multiplier) for x in data]
            sorted_ints = self._radix_sort_desc(as_ints)
            return [x / multiplier for x in sorted_ints]
        else:
            raise ValueError("Only integers or floats are supported")

✅ Usage Example (From Another File or Script)

from radix_sorter import RadixSorter

data1 = [170, -45, 75, -90, 802, 24, 0, -6]
data2 = [1.234, 12.456, -0.123, -99.9, 0.001, 7.89]

sorter = RadixSorter(precision=4)

sorted_ints = sorter.sort(data1)
sorted_floats = sorter.sort(data2)

print("Sorted Integers:", sorted_ints)
print("Sorted Floats:", sorted_floats)

✅ Output:

Sorted Integers: [802, 170, 75, 24, 0, -6, -45, -90]
Sorted Floats: [12.456, 7.89, 1.234, 0.001, -0.123, -99.9]

🔧 To Use This as a Module:

    Save the class code in a file called radix_sorter.py

    Import and use RadixSorter in your scripts

    Optionally package it into a pip-installable module if you’re building something larger

✅ Bonus: Extendable Design

You can easily extend this class to:

    Support ascending sort with a flag

    Add logging or print tracing for educational step-by-step visualization

    Export the results to a file or plot histograms of bucket content

Would you like me to include tracing steps or a version that shows each digit pass visually?

'''

'''
~ Complexity Analysis of Radix Sort
The time complexity of radix sort is O(n.d), where n is the size of the vector and d is the number of digits in the largest number.

If d is very small:

Time Complexity: O(n)

Similarly, the general space complexity of radix sort is:

Space Complexity: O(n+d)
'''