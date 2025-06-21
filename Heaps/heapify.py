"""
~ Heapify
Heapify is the process of rearranging nodes in a tree to ensure that every node satisfies the heap property.

Consider the following input list:

        19, 15, 20, 16, 11, 10, 24, 25, 6, 21

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.4.1.png

After heapifying, the array satisfies the heap property. And will look as follows:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.4.2.png

~ Working of Heapify
Let's see how heapify works:

Heapify works by ensuring every node satisfies the heap property. That is, the value of a node is smaller than its child nodes.

To heapify, we will compare each node with its child nodes.

Heapify typically starts from the bottom of the heap because it is more efficient in terms of the number of comparisons and swaps required to satisfy the heap property.

~ Working of Heapify
To heapify an array, we will start by assuming all the leaf nodes satisfy the heap property. This is because none of the leaf nodes have a child to compare.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.4.3.png

Now we will actually start from the last internal node (11 in this case). We have chosen 11 because it is the first node with a child (we are traversing backward).
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.4.4.png

We will compare it with its child (21). As 11< 21, it satisfies the heap property.

Now, we will move to the next internal node (16) and compare it with its children (6 and 25).
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.4.5.png

Since 16 > 6, it doesn't satisfy heap property. So, we will swap 6 and 16.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.4.6.png

Now, we will repeat this process for node 20.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.4.7.png

Since 20 > 10, swap 20 with 10.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.4.8.png

Now, we will continue it for 15.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.4.9.png

Both the children of 15 have less value than 15. Since we want the smallest element on top, we will swap 15 with the smaller child (6).
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.4.10.png

NOTE: After swapping a node with a smaller child, the newly swapped node may violate the heap property. So, after every swap, we must check if the new child satisfies the heap property.

Now we will check for 19.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.4.11.png

As 19 > 6, we will swap 19 and 6 (smaller child).
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.4.12.png

As you can see 19 again violates the heap property, so we will swap 19 with 11.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.4.13.png

Since all nodes satisfy the heap property, this marks the end of the heapify process.

~ Thought Process
Heapify ensures that each node satisfies the heap property.

To achieve this, we compare the value of each node to their children and see if the node violates the heap property.

Let's create a function named heapify_down(), and for a node at index index we will follow the following steps:

NOTE: We are naming the function heapify_down() because we are comparing the value of each node with its child nodes (down) and not with the parent (up).

1. Return if the node is a leaf node.

    if not self.has_left_child(index):
        return

A heap is a complete binary tree. Thus, if a node does not have a left child, it cannot have a right child.

So, a node without a left child is a leaf node.
We assume all leaf nodes satisfy the heap property.

2. Find the index of the smaller child.
We will assume the left child is the smaller child since all non-leaf nodes will have a left child.

If a node has a right child and if the right child is smaller than the left child, it will be our smaller child.

    smaller_child_index = self.left_child(index)
    if self.has_right_child(index) and self.heap[self.right_child(index)] < self.heap[smaller_child_index]:
        smaller_child_index = self.right_child(index)

3. If the current node is smaller than the smaller child, we're done.

    if self.heap[index] <= self.heap[smaller_child_index]:
        return
        
4. If the current node is greater than the smaller child, swap them.

    self.swap(index, smaller_child_index)

5. Repeat for the child.
After swapping a node with a smaller child, it is possible that the newly swapped node violates the heap property. So, after every swap, we must check if the new child satisfies the heap property.

    self.heapify_down(smaller_child_index)

This marks completion of heapify for a single node at index index. To completely heapify an array we must perform heapify down for each element in the array.

    def heapify(self, array):
        self.heap = array
        for i in range(len(self.heap) - 1, -1, -1):
            self.heapify_down(i)

"""

# Source Code: Heapify

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

heap = MinHeap()
list1 = [19, 15, 20, 16, 11, 10, 24, 25, 6, 21]
heap.heapify(list1)
print(heap)

# Output:
    # [6, 11, 10, 15, 19, 20, 24, 25, 16, 21]


"""
~ Heapify-Up
In the last case, we compared with the child node and heapified down.

Alternatively, we can also compare to the parent and heapify up.
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
            self.heapify_up(i)

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

heap = MinHeap()
list1 = [19, 15, 20, 16, 11, 10, 24, 25, 6, 21]
heap.heapify(list1)
print(heap)


# Output:
    # [6, 11, 10, 15, 19, 20, 24, 25, 16, 21]

# This is the same as the heapify down operation we performed earlier.