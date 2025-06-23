"""
~ Introduction
Heap sort is an efficient sorting algorithm that utilizes the heap data structure to arrange elements in ascending or descending order. The algorithm involves two main operations:
    * Insertion into a heap
    * Deletion from the heap

Let's follow a detailed example with the given list: [15, 12, 25, 16, 5].

~ Thought Process
1. Insert into a heap.

    lst = [15, 12, 25, 16, 5]

    for i in array:
        heap.insert(i)

After insertion, the heap looks like this:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.5.1.png

2. Extract the minimum from the heap.

    for i in range(len(lst)):
        sorted_array.append(heap.extract_min()) 

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.5.2.png

In this way, a heap can be used to efficiently sort elements in ascending or descending order using the heap sort algorithm.

Next, we will explore the Python implementation of heap sort.



"""

class MinHeap:
    def __init__(self):
        self.heap = []

    # return the number of nodes in a heap
    def size(self):
         return len(self.heap)

    # check if the heap is empty
    def is_empty(self):
        return len(self.heap) == 0

    # string representation of a heap
    def __str__(self):
        return str(self.heap)

    # swap the heap values
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # calculate the index of a node's parent
    def parent(self, index):
        return (index - 1) // 2

    # calculate the index of a node's left child
    def left_child(self, index):
        return 2 * index + 1

    # calculate the index of a node's right_child
    def right_child(self, index):
        return 2 * index + 2

    # check if a node at a given index has a parent
    def has_parent(self, index):
        return self.parent(index) >= 0

    # check if a node at a given index has a left child
    def has_left_child(self, index):
        return self.left_child(index) < len(self.heap)

    # check if a node at a given index has a right child
    def has_right_child(self, index):
        return self.right_child(index) < len(self.heap)

    # heapify
    def heapify(self, array):
        self.heap = array
        for i in range(len(self.heap) - 1, -1, -1):
            self.heapify_down(i)

    # heapify down
    def heapify_down(self, index):
        # return if leaf node is reached
        if not self.has_left_child(index):
            return

        # find the smaller child index
        smaller_child_index = self.left_child(index)
        if self.has_right_child(index):
            if self.heap[self.right_child(index)] < self.heap[smaller_child_index]:
                smaller_child_index = self.right_child(index)

        # compare the node with its smaller child and swap if needed
        if self.heap[index] <= self.heap[smaller_child_index]:
            return
        self.swap(index, smaller_child_index)
        self.heapify_down(smaller_child_index)

    # heapify up
    def heapify_up(self, index):
        if self.has_parent(index):
            parent_index = self.parent(index)
            # compare the value to its parent and swap if necessary
            if self.heap[index] < self.heap[self.parent(index)]:
                self.swap(index, parent_index)
                self.heapify_up(parent_index)

    # insert into heap
    def insert(self, value):
        self.heap.append(value)
        # replace with heapify_up() logic
        self.heapify_up(self.size() - 1)

    # extract min from heap
    def extract_min(self):
        min = self.heap[0]

        # empty the list if the heap has one element
        if self.size() == 1:
            self.heap = []
            return min

        # replace the root node with the last node
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        # replace with heapify_down() logic
        self.heapify_down(0)
        return min

    # peek
    def peek(self):
        return self.heap[0]

# heap sort
def heap_sort(lst):
    # create empty array
    sorted_array = []
    # create heap
    heap = MinHeap()
    # insert heap
    for i in lst:
        heap.insert(i)
    # extract min
    for i in range(len(lst)):
        sorted_array.append(heap.extract_min())
    # return sorted array
    # Ascending Heap Sort
    return sorted_array

    # Descending Heap Sort
    # return sorted_array[:: -1]  


lst = [15, 12, 25, 16, 5]
print(heap_sort(lst))


"""
~ Complexity Analysis of Heap Sort
In heap sort, the minimum element (the root of the heap) is repeatedly removed, and the heap is adjusted (heapified) to maintain the heap property.

Each of the n deletions from the heap involves a call to the heapify() function, which works in O(logn) time for a binary heap.

Thus, the total time complexity for heap sort is O(n logn).
"""