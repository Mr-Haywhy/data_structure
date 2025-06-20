"""
~ Introduction
As we know, a binary tree contains two essential pieces of information:
    *data contained by the nodes
    *relationship between the nodes

Consider the following tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.1.1.png

Drawing a tree is time-consuming and space-inefficient. So, we will represent the tree as an array or list.

In an array,
    *The data stored in the array represents the data contained in the nodes.
    *The position of the data represents the relationship between the nodes.

~ Array Representation
Consider the same tree again, but this time, let's number the nodes.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.1.2.png

The array representation would be:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.1.3.png

NOTE: To understand this concept easily, we will start the array with 1.

For any node at index i in the array:
    *The left child is located at index 2i.
    *The right child is located at index 2i + 1.
    *The parent is located at index floor(i/2).

~ Working: Array Representation
Since A is the root node, we will insert it at the first position (index 1 in this case).
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.1.4.png

B is the left child node of A :
        B: 2 * 1 = 2

C is the right child node of A:
        C: 2 * 1 + 1 = 3

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.1.5.png

D and E are the child nodes of B.

Since B is at index 2:
        D: 2 * 2 = 4
        E: 2 * 2 + 1 = 5

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.1.6.png

Similarly, F and G are the child nodes of C.
        F: 2 * 3 = 6
        G: 2 * 3 + 1 = 7

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.1.7.png


~ Implementation of Array Representation
Our representation so far assumes that the first node is at index 1. However, in implementation, the index starts from 0, so our relationship should be slightly modified as follows:

For any node at index i in the array:
    *The left child is located at index 2i + 1.
    *The right child is located at index 2i + 2.
    *The parent is located at index ((i - 1) // 2).

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.1.8.png


~ Thought Process: Array Representation
Let's see how array representation is done.

1. Find the parent index.
For any node at index i in the array, the parent is located at index ((i - 1) // 2).

    # calculate the index of a node's parent
    def parent(self, index):
        return (index - 1) // 2

2. Find the child index.
For any node at index i in the array:
* The left child is located at index 2i + 1.
* The right child is located at index 2i + 2.

    # calculate the index of a node's left child
    def left_child(self, index):
        return 2 * index + 1

    # calculate the index of a node's right child
    def right_child(self, index):
        return 2 * index + 2

3. Check if the parent exists.
Given that our array starts at 0, we can say that the parent exists if the parent index is greater than or equal to 0.

    # check if a node at a given index has a parent
    def has_parent(self, index):
        return self.parent(index) >= 0

4. Check if a child exists.
Assuming our binary tree is represented as an array, a child node is present only if the index of the child is within the bounds of the array's length.

    # check if a node at a given index has a left child
    def has_left_child(self, index):
        return self.left_child(index) < len(self.array)

    # check if a node at a given index has a right child
    def has_right_child(self, index):
        return self.right_child(index) < len(self.array)

Next, we will look at the source code.
"""

# Source Code:
class BinaryTree:
    def __init__(self):
        self.array = []

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
        return self.left_child(index) < len(self.array)

    # check if a node at a given index has a right child
    def has_right_child(self, index):
        return self.right_child(index) < len(self.array)

    # add a new element to the binary tree 
    # for demonstration purposes
    def insert(self, value):
        self.array.append(value)

    # print the tree contents (for demonstration)
    def print_tree(self):
        print(self.array)


bt = BinaryTree()

# insert elements into the binary tree
for i in range(10):
        bt.insert(i)

# display binary tree
bt.print_tree()
print()

# check some relationships
index = 3
if bt.has_parent(index):
    print(f"Parent of node at index {index}: {bt.array[bt.parent(index)]}")
    
if bt.has_left_child(index):
    print(f"Left child of node at index {index}: {bt.array[bt.left_child(index)]}")
    
if bt.has_right_child(index):
        print(f"Right child of node at index {index}: {bt.array[bt.right_child(index)]}")


"""
Output:
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    Parent of node at index 3: 1
    Left child of node at index 3: 7
    Right child of node at index 3: 8

Here, we added the insert() method to add elements to the array for demonstration purposes only.
"""