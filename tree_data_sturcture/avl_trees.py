'''
~ Introduction to AVL Trees
An AVL tree is a self-balancing BST where the difference between the heights of the left and right subtrees cannot be more than one for all nodes.

This unique balancing criteria is called the height-balance property.

AVL trees aim to define balance by introducing the concept of Balance Factor.

The balance factor of a node is the difference between the height of its left and right subtrees.

    Balance Factor (BF) = Height of Left Subtree - Height of Right Subtree

Since the height of the children can differ (at most) by one, the only possible values for the balance factor of any node in an AVL tree are 1,0, and -1.

NOTE: AVL trees are named after their inventors, Georgy Adelson-Velsky and Evgenii Landis, who introduced them in 1962.
AVL trees are a type of self-balancing binary search tree (BST) that maintain their balance through rotations during insertions and deletions.
AVL trees are used in applications where frequent insertions and deletions occur, as they provide O(log n) time complexity for search, insert, and delete operations.
AVL trees are particularly useful in scenarios where data is frequently modified, such as databases and memory management systems.

~ How to Calculate the Balance Factor?
Let's calculate the balance factor for each node of the following binary search tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.2.1.png

The height of each node becomes:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.2.2.png

Let's calculate the balance factor of each node.

    Balance Factor (BF) = Height of Left Subtree - Height of Right Subtree

NOTE: The balance factor of leaf nodes is zero. The height of a missing node is considered to be -1.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.2.3.png

Since all the nodes have values 0, 1, or -1, the tree above is an AVL tree.

~ Thought Process: Implementation of AVL Trees
We have implemented various tree structures thus far. AVL trees follow a similar approach.

AVL trees can be implemented by following the given steps:

1. Create a class to handle nodes.

        class AVLNode:
            def __init__(self, data):
                self.data = data
                self.left = None
                self.right = None
                self.height = 0 
                
AVL trees are an extension of BSTs.

So, the class to handle nodes will remain the same with one added attribute: height.

Here, we have initialized height to 0, which is the minimum height a non-empty tree can have.

2. Create a class to handle the tree.

        class AVLTree:
            def __init__(self):
                self.root = None

3. Create a helper to get the height of each node

        def get_height(self, node):
            if not node:
                # return -1 for None nodes
                return -1  
            return node.height

The logic is pretty simple here:
    * Return -1 if we fail to find any node.
    * Else, return the height attribute of the node.

4. Calculate the Balance Factor (BF) for each node.

        def get_balance(self, node):
            if not node:
                return 0
            return self.get_height(node.left) - self.get_height(node.right)
'''

# Combining the Classes
# Combining the classes leaves us with this skeletal format of our AVL tree.

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0 
        
class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return -1
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    

'''
Operations in an AVL Tree
Like BST, three key operations can be performed in an AVL tree.
    * Search: Find a particular key in the tree.
    * Insert: Insert a new key in the tree.
    * Delete: Delete a particular key from the tree.

Search in AVL Trees
Searching in an AVL tree is exactly the same as in BST, so we won't explain this operation here.

Instead, we'll only include the code for inorder traversal from BST to implement search in AVL trees. If you need clarification, please revisit Search in BST.

We can use any of the traversal techniques. Let us use inorder traversal for this course.
'''

def inorder_traversal(self, node, visited_nodes=None):
    if visited_nodes is None:
        visited_nodes = []
    if node:
        self.inorder_traversal(node.left, visited_nodes)
        visited_nodes.append((node.data, node.height))
        self.inorder_traversal(node.right, visited_nodes)
    return visited_nodes

'''    
Insertion and deletion in AVL trees also function the same way as in BST. However, in AVL, we have to maintain the balance in the tree.

~ Insertion in AVL Trees
The insertion operation in BST can be broken down into three steps:
    1. Insert the required node as a leaf node by following BST insertion.
    2. Calculate the balance factors of each node.
    3. If the tree is not a balanced AVL tree, apply the appropriate rotations.

~ Example: Insertion Into AVL Trees
Now, let's insert a node into a sample tree using the steps we just discussed and then derive a general algorithm for the process.

Suppose we have the following binary tree:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.2.4.png

Let's insert 7 in the given AVL tree:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.2.5.png

Calculate the Balance Factors
Now, we will calculate the balance factors of every node.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.2.6.png

After we insert 7 into the tree and update the balance factors, we find an imbalance at node 9, which has a balance factor of 2 (i.e. BF > 1).

~ Identify and Rectify the Imbalance
As we have already studied, there are four types of imbalances.
    * Left-Left imbalance (solved by right rotation)
    * Right-Right imbalance (solved by left rotation)
    * RL imbalance (solved by right-left rotation)
    * LR imbalance (solved by left-right rotation)

Thus, our tree after insertion has a case of left-left imbalance at node 9.

Thus, we balance the tree with right rotation.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.2.7.png

Now, let's implement rotations in Python so that we can use the code to implement AVL insertion.

~ Rotations in AVL
Rotation in AVL is the same as studied earlier. Consider the following right rotation:

        def rotate_right(self, y):
            x = y.left
            z = x.right

            # Perform rotation
            x.right = y
            y.left = z

            # Return new root
            return x

Since rotations in AVL are done to balance the tree, we update the height of each node during rotation. This will help us check whether the rotation has balanced the tree or not.

        def rotate_right(self, y):
            x = y.left
            z = x.right

            x.right = y
            y.left = z

            y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
            x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
            
            return x

NOTE: The order of calculation of height matters here as y is now a child of x. So, y's height should be calculated first.

Similarly, the left rotation becomes:

        def rotate_left(self, x):
            y = x.right
            z = y.left

            y.left = x
            x.right = z

            x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
            y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

            return y

NOTE: Similar to right rotation, the order of updating height is important here too.

With this out of the way, let's look into the insertion process.
'''

'''
~ Thought Process: Insertion in AVL Trees
We can insert new elements into our AVL tree by following these steps:

1. BST insert.
The first step is obviously BST insertion, which we can simply code like before.

        def insert(self, root, data):
            # standard BST insertion
            if not root:
                return AVLNode(data)
            elif data < root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)

2. Calculate the balance factor of each node.
The next step is to update the height of the root node, for which we will make use of the get_height() helper function.

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

After that, we will make use of the get_balance() helper to check the balance factor of each node.

        # use balance() to check for imbalance
        balance = self.get_balance(root)

3. Identify and rectify imbalance.
Now, all that's left to do is to identify the type of imbalance and apply the appropriate rotations for each of the cases.

        # RR imbalance 
        if balance > 1 and data < root.left.data:
            return self.rotate_right(root)

        # LL imbalance 
        if balance < -1 and data > root.right.data:
            return self.rotate_left(root)

        # LR rotation
        if balance > 1 and data > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # RL rotation
        if balance < -1 and data < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
'''

'''
# Source Code: Insertion in AVL Tree
Finally, let's combine all the blocks of code we've written so far. This will give us a complete implementation of an AVL tree.
'''

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

class AVLTree:
    def __init__(self):
        self.root = None
    
    def get_height(self, node):
        if not node:
            return -1
        return node.height
        
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        z = x.right

        x.right = y
        y.left = z

        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def rotate_left(self, x):
        y = x.right
        z = y.left

        y.left = x
        x.right = z

        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def insert(self, root, data):
        if not root:
            return AVLNode(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        balance = self.get_balance(root)

        if balance > 1 and data < root.left.data:
            return self.rotate_right(root)
        if balance < -1 and data > root.right.data:
            return self.rotate_left(root)
        if balance > 1 and data > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and data < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def inorder_traversal(self, node, visited_nodes=None):
        if visited_nodes is None:
            visited_nodes = []
        if node:
            self.inorder_traversal(node.left, visited_nodes)
            visited_nodes.append(node.data)
            self.inorder_traversal(node.right, visited_nodes)
        return visited_nodes

avl = AVLTree()
values_input = [14, 12, 15, 42, 31, 123, 26]
for value in values_input:
    avl.root = avl.insert(avl.root, value)

print(
    f'The inorder traversal after insertion is: {avl.inorder_traversal(avl.root)}')

'''
Output:
    The inorder traversal after insertion is: [12, 14, 15, 26, 31, 42, 123] 
'''

'''
~ Deletion in AVL Trees
Deletion in AVL trees is similar to deletion in BST, with the added step of maintaining balance after deletion.
We can delete a node from an AVL using the following steps:
    1. Delete a node just like in a BST.
    2. Update the Balance Factors.
    3. Perform the appropriate balancing operation.

We are already familiar with performing deletion in BST. Similarly, we already have a helper function to update the balance factor.

So, let's jump right into the balancing act.

Like with insertion, we can easily find the appropriate rotation to be used based on the balance factor of the imbalanced node.

Here again, we have two cases:

Case 1: Balance Factor > 1
    * Case 1.1: Balance factor of left child >= 0 : This is LL imbalance. Perform right rotation.
    * Case 1.2: Balance factor of left child < 0 : This is LR imbalance. Perform LR rotation.

Case 2: Balance Factor < -1
    * Case 2.1: Balance factor of right child <= 0 : This is RR imbalance. Perform left rotation.
    * Case 2.2: Balance factor of right child > 0 : This is RL imbalance. Perform RL rotation. 


~ Implementation of Deletion From AVL Trees
We can delete elements from our AVL tree by following these steps.

1. BST Delete

The first step is to perform the standard BST delete operation. Having discussed that in detail in the previous chapter, we will be skipping it here.

        def delete(self, root, data):
            if not root:
                return root

            if data < root.data:
                root.left = self.delete(root.left, data)
            elif data > root.data:
                root.right = self.delete(root.right, data)
            else:
                if not root.left or not root.right:
                    temp = root.left if root.left else root.right
                    if not temp:
                        root = None
                    else:
                        root = temp
                else:
                    temp = self.get_min_value_node(root.right)
                    root.data = temp.data
                    root.right = self.delete(root.right, temp.data)

            if root is None:
                return root

2. Calculate the balance factor of each node.
We then update the height and check for imbalances. Like in insertion, we make use of the get_height() helper.

        # update the height of the current node
        root.height = 1 + max(self.get_height(root.left),
                            self.get_height(root.right))

After that, we will make use of the get_balance() helper to check the balance factor and see if we have any imbalances.

        # get the balance factor to check if it became unbalanced
        balance = self.get_balance(root)

3. Apply Rotations

        # RR imbalance 
        if balance > 1 and data < root.left.data:
            return self.rotate_right(root)

        # LL imbalance 
        if balance < -1 and data > root.right.data:
            return self.rotate_left(root)

        # LR rotation
        if balance > 1 and data > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # RL rotation
        if balance < -1 and data < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root) 
'''

# Source Code: Deletion from AVL Trees

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

class AVLTree:
    def __init__(self):
        self.root = None
    
    def get_height(self, node):
        if not node:
            return -1
        return node.height
        
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        z = x.right

        x.right = y
        y.left = z

        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def rotate_left(self, x):
        y = x.right
        z = y.left

        y.left = x
        x.right = z

        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def insert(self, root, data):
        if not root:
            return AVLNode(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        balance = self.get_balance(root)

        if balance > 1 and data < root.left.data:
            return self.rotate_right(root)
        if balance < -1 and data > root.right.data:
            return self.rotate_left(root)
        if balance > 1 and data > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and data < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def delete(self, root, data):
        if not root:
            return root

        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if not root.left or not root.right:
                temp = root.left if root.left else root.right
                if not temp:
                    root = None
                else:
                    root = temp
            else:
                temp = self.get_min_value_node(root.right)
                root.data = temp.data
                root.right = self.delete(root.right, temp.data)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def inorder_traversal(self, node, visited_nodes=None):
        if visited_nodes is None:
            visited_nodes = []
        if node:
            self.inorder_traversal(node.left, visited_nodes)
            visited_nodes.append(node.data)
            self.inorder_traversal(node.right, visited_nodes)
        return visited_nodes

# Example usage
avl = AVLTree()
values_input = [4,2,8,10,6]
for value in values_input:
    avl.root = avl.insert(avl.root, value)

print('Inorder traversal of the AVL tree is:')
print(list(avl.inorder_traversal(avl.root)))

# Example of deleting a value
value_to_delete = 8
avl.root = avl.delete(avl.root, value_to_delete)

print('Inorder traversal after deletion:')
print(list(avl.inorder_traversal(avl.root)))

'''
Output:
    Inorder traversal of the AVL tree is:
    [2, 4, 6, 8, 10]
    Inorder traversal after deletion:
    [2, 4, 6, 10]
'''