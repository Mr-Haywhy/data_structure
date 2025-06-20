"""
~ Introduction
A heap is a special type of tree in which each node has a key that is either greater, less, or equal to the key of its parent.
This property is called the heap property.
There are two types of heap property:
    * Max heap property
    * Min heap property

~ Max Heap Property
In the max heap property,
    * The value of each node is greater than or equal to the values of its children.
    * The root node has the maximum value in the tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.2.1.png
    
The tree that satisfies the max heap property is called max heap.

~ Min Heap Property
In min heap property,
    * The value of each node is smaller than or equal to the values of its children.
    * The root node has the minimum value in the tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.2.2.png

The tree that satisfies the min heap property is called min heap.  

~ Binary Heaps
A binary heap is a complete binary tree with heap property. Hence, a binary heap has the following properties:
    * It is a complete binary tree.
    * It satisfies the heap property (either max-heap or min heap).

Binary heap is the most common type of heap.
In this chapter, we will learn about binary min heap.

NOTE: From here, whenever we mention heap, we are referring to the binary min heap.

~ Create a Heap
Let's start by creating a heap.
By heap, we mean a binary min heap.
We will implement this heap using binary representation of a tree.

~ Thought Process: Create Heap
Let's create a heap and add a few simple operations to it.

1. Define a class to implement the min heap.
We will use a list for the array representation of the heap.

    class MinHeap:
        def __init__(self):
            self.heap = []

2. Add helper methods: swap(), calculate_size(), etc.
These are simple methods that do not need much explanation.

    # return the number of nodes in a heap
    def size(self):
        return len(self.heap)

    # check if the heap is empty
    def is_empty(self):
        return len(self.heap) == 0

    # string representation of a heap
    def __str__(self):
        return str(self.heap)

    # swap the values at index i and j
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

3. Define heap relationships in array form.
We have covered this in the previous section.

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

4. Define heap operations.
Our heap will have the following operations:
    * Insert
    * Extract Min (Pop)
    * Peek

We will cover heap operations in the next lesson.
First, we will combine all these methods to create a working program of a min heap.

"""

# Source Code: Heap Creation

class MinHeap:
    def __init__(self):
        self.heap = []

    # return the number of nodes in the heap
    def size(self):
        return len(self.heap)

    # check if the heap is empty
    def is_empty(self):
        return len(self.heap) == 0

    # string representation of a heap
    def __str__(self):
        return str(self.heap)

    # swap the heap elements
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # calculate the index of a node's parent
    def parent(self, index):
        return (index - 1) // 2

    # calculate the index of a node's left child
    def left_child(self, index):
        return 2 * index + 1

    # calculate the index of a node's right child
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

min_heap = MinHeap()
print(min_heap) #[]

"""
If we run this program, the output will be empty since we haven't added any nodes to the heap.

In the next lesson, we will cover fundamental heap operations.
"""