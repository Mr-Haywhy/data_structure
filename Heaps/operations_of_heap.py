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

