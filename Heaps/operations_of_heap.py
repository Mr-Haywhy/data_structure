"""
~ Introduction
In this lesson, we will learn to perform these operations:

Insert into a heap.
Extract min node (root) from a heap.
Peek in a heap.
Let's start by learning how to insert a node into a min heap.

~ Insert into a Min Heap
Suppose we have a min heap with this structure:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.3.1.png

Let's say we need to insert a node with value 5 into the heap.

Our heap will look like this after insertion.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.3.2.png

Let's learn how this works.

~ Thought Process: Insert into Heap
To insert into a heap, we follow the steps below.

1. Insert at the end of the heap.
Let's start by adding the new node at the end of the heap.

    self.heap.append(value)

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.3.3.png

For the heap to remain a heap, all the nodes must satisfy the heap property.
In our case, the tree must satisfy the *min heap property*.

2. Compare with parent and swap if the value is smaller.
This newly inserted node violates the heap property, so we should restore the heap property.
To satisfy the min heap property, the value of the node at a given index should be greater than or equal to the value of their parent index (self.parent[index]).

    if self.heap[index] < self.heap[self.parent(index)]:
        self.swap(index, parent_index)

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.3.4.png

3. Repeat step 2 until the heap property is satisfied.
To complete the insertion process, we must ensure that the final tree satisfies the heap property.
We continue swapping until the parent is smaller than the inserted value.

    if self.heap[index] < self.heap[self.parent(index)]

This is because all existing nodes had already satisfied the heap property before the insertion.
So, once the inserted node also satisfies the heap property, we can be certain that all nodes satisfy the heap property.
Or we continue swapping until the item reaches the root of the heap.

    if self.has_parent(index) 

If our item reaches the root, there are no nodes above it to create any issues. Thus, we can terminate our loop.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.3.5.png

We have now inserted all the nodes. And since they all satisfy the heap property, the process ends.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.3.6.png


"""

# Source Code: Insert Into Heap
def insert(self, value):
    self.heap.append(value)
    index = len(self.heap) - 1

    while self.has_parent(index) and self.heap[index] < self.heap[self.parent(index)]:
        parent_index = self.parent(index)
        self.swap(index, parent_index)
        index = parent_index

"""
Output:
    [12, 15, 25, 16]
    [5, 12, 25, 16, 15]
"""

"""
~ Time Complexity for Insertion
The height of a binary heap with n elements is log(n).
So, in the worst case, you might need to perform log(n) comparisons and swaps. Therefore,

Time Complexity: O(logn)
"""

"""
~ Extract Min Node From Heap
Suppose we have to extract the min node (root node) from this heap:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.3.8.png

After extracting 5, the heap will have the following structure:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.3.9.png

Let's see how the extraction is done.

~ Thought Process: Extract Min
Suppose we have the following heap.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.3.10.png

To extract the min node from a heap, we follow the given steps.

1. Replace the root node with the last element and remove the last node from the heap.

    self.heap[0] = self.heap[-1] 
    self.heap.pop() 

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.3.11.png

2. Find the index of the smaller child.

    smaller_child_index = self.left_child(index)
    if self.has_right_child(index): 
        if self.heap[self.right_child(index)] < self.heap[self.left_child(index)]:
            smaller_child_index = self.right_child(index)

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.3.12.png

3. If the current node is smaller than the smaller child, we're done.

    if self.heap[index] <= self.heap[smaller_child_index]:
        return

4. If the current node is greater than the smaller child, swap them.

    self.swap(index, smaller_child_index)

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.3.13.png

NOTE: If both children violate the heap property, swap with the smaller child.

5. Repeat until the heap property is satisfied or a leaf node is reached.

    while True:
        # break if leaf node is reached
        if not self.has_left_child(index):
            break
        # Step 2 and 3 logic
        # break if heap property is satisfied 
        self.heap[index] <= self.heap[smaller_child_index]:
        break
        
NOTE:  A heap is a complete binary tree. Thus, if a node does not have a left child, it cannot have a right child.

The new root node is 12, and its children are 15 and 25.

Since 12 is smaller than both of its children (15 and 25), the heap property is satisfied, and the process ends.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.3.14.png

~ For Heap With One Node
If a heap has only one node, we can simply empty our array and avoid all deletion computations.

    if(self.size() == 1):
        min = self.heap[0]
        self.heap = []
        return min

We only use the long computation process if there are more than two nodes.
"""

# Source Code: Extract Min From Heap

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

    # insert into heap
    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1

        while self.has_parent(index) and self.heap[index] < self.heap[self.parent(index)]:
            parent_index = self.parent(index)
            self.swap(index, parent_index)
            index = parent_index

    # delete from heap
    def extract_min(self):
        min = self.heap[0]

        # empty the list if the heap has one element
        if self.size() == 1:
            self.heap = []
            return min

        # replace the root node with the last node
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        index = 0
        while True:
            # break if leaf node is reached
            if not self.has_left_child(index):
                break

            # find the smaller child index
            smaller_child_index = self.left_child(index)
            if self.has_right_child(index):
                if self.heap[self.right_child(index)] < self.heap[self.left_child(index)]:
                    smaller_child_index = self.right_child(index)

            # compare the node with its smaller child and swap if needed
            if self.heap[index] <= self.heap[smaller_child_index]:
                break

            self.swap(index, smaller_child_index)
            index = smaller_child_index
        return min
            
# Example usage:
heap = MinHeap()
values = [12, 15, 25, 16, 5]
for value in values:
    heap.insert(value)
print(heap) 
print(f'Root: {heap.extract_min()}')
print(heap)


"""
Output:
    [5, 12, 25, 16, 15]
    Root: 5
    [12, 15, 25, 16]

NOTE: If the heap is empty, the code will throw Index error.
"""

"""
~ Time Complexity for Extracting Min
The height of a binary heap with n elements is log(n).
So, in the worst case, you might need to perform log(n) comparisons and swaps. Hence,

Time Complexity: O(logn)
"""


"""
~ Peek in Min Heap
In heap, returning the value of the root node is called peeking.
In a min heap, peek() returns the smallest value.

~ Thought Process
Since the first element is always the smallest element in a min heap, here's how to access it.

    # peek
    def peek(self):
        return self.heap[0]

Output:
    Root: 1
    [1, 2, 5, 3, 4, 6, 7]


~ Time Complexity for Peek
Since we can perform peeking in a single statement, its complexity will be constant.

Time Complexity: O(1)
"""


# Combining Up To Now
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

    # insert into heap
    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1

        while self.has_parent(index) and self.heap[index] < self.heap[self.parent(index)]:
            parent_index = self.parent(index)
            self.swap(index, parent_index)
            index = parent_index

    # delete from heap
    def extract_min(self):
        min = self.heap[0]

        # empty the list if the heap has one element
        if self.size() == 1:
            self.heap = []
            return min

        # replace the root node with the last node
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        index = 0
        while True:
            # break if leaf node is reached
            if not self.has_left_child(index):
                break

            # find the smaller child index
            smaller_child_index = self.left_child(index)
            if self.has_right_child(index):
                if self.heap[self.right_child(index)] < self.heap[self.left_child(index)]:
                    smaller_child_index = self.right_child(index)

            # compare the node with its smaller child and swap if needed
            if self.heap[index] <= self.heap[smaller_child_index]:
                break

            self.swap(index, smaller_child_index)
            index = smaller_child_index
        return min
    
    # peek
    def peek(self):
        return self.heap[0]
            
heap = MinHeap()
# inserts
heap.insert(10)
heap.insert(40)
heap.insert(20)
heap.insert(30)
print(heap)

# peek
print(f'Root: {heap.peek()}')

# extract min
print(f'Root: {heap.extract_min()}')
print(heap)