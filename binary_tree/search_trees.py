"""
.....................Introduction to Search Trees...........................
Search trees are a special class of trees that define certain rules which streamlines searching and navigation.

Search trees are tree data structures used for locating specific keys from within a set. They organize the keys in a manner that allows for efficient navigation.

The operations that can be performed in a search tree are:

Search: Finds a key within the tree.
Insertion: Adds a key to the tree.
Deletion: Removes a key from the tree.
To perform these operations, the nodes in the tree must be in a certain order. Let's discuss this.

..................Ordered Trees.....................
An ordered tree is a tree in which the children of each node have a specific order and that order is important.

A tree is ordered if, for each set of children, there is a specific child designated as the first, another as the second, and so on.

This means that every child holds a specific position in the order - first child, second child, and so forth.

Next, we will see an example.

.................Real-Life Analogy: Unordered Trees............
After a hectic week at work, you decide to treat yourself for the weekend.

You go to the supermarket and return home with a bag containing a bag of chips and a bottle of coke, and a box of cookies.

Let's use a tree to represent the contents of the bag.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.1.png

This is an accurate representation of the content of the bag using a tree. But is it the only way?

You could interchange the position of the items in the tree around and it will retain its essence all the same.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.2.png

These types of trees are unordered trees.

Now consider a family tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.3.png


We could easily swap the order of contents in the bag. But here, if you swap the order of children, you would lose some information.

Here, the order of the children is representing the birth order of the children and you cannot just swap it.

This type of tree is known as ordered trees.

NOTE: Binary Trees and all its variants are ordered trees.

In unordered trees, there's no right or wrong order to represent the nodes.However, in the ordered tree, there is a certain order of precedence.

NOTE: A common mistake that beginners make is assuming that ordered trees order the data in a specific order. However, in practice, the nodes are ordered, not their values.
"""

"""
.......................Binary Search Tree (BST)....................
Binary search trees are binary trees that have the following properties:

*The left child's data should always be less than the parent's data.
*The right child's data should always be greater than the parent's data
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.4.png

In the figure above:
*Every leaf node to the right of a node is greater than the node.
*Every leaf node to its left is smaller than the node.

....................Why BST?....................
Binary Search Trees (BST) are used to implement a sorted map or a sorted list.

Sorted Map
A sorted map is a data structure that contains key-value pairs, and the keys are kept in sorted order.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.5.png

Here, the dates are the keys and events are the value.
Since the dates(keys) are arranged in ascending order, this is a sorted map.

Sorted List
Sorted List just contains the value in sorted order.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.6.png

.......................BST Search Operation................
Search operations are performed in BSTs by viewing it as a decision tree i.e. every time we arrive at a node starting from the root, we ask a simple yes/no question;

"Is the value we are searching for greater than the value of the current node ?"

Which leaves us with two possible options:
*Yes: Continue your search in the right subtree.
*No: Continue your search in the left subtree.

The third option, the value we are searching for being equal to the value of the current node completes the search operation.

....................Working of BST Search..................
Let's look at an example and try to find 4 in this BST:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.7.png
We start at our root node which has the value 8.

Step I: Check is 4>8 ?
As our answer is No, we continue our search in the left subtree and move to the left node which is 3.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.8.png

Setp II: Check is 4>3 ?

The answer is yes, so we move towards the right subtree and arrive at the right node of 3 which is 6.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.9.png

Step III: Check is 4 > 6 ?
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.10.png

As the answer is no , we move towards the left subtree and arrive at 4 which is our desired element.


..................Thought Process: BST Search Operation.............
We can implement the search operation in python in the following steps.

1. Defining the function.

        def search(self, value, current_node= None):
        
We start by defining our search() method which takes in two parameters:

~ value, which is the value we want to search for in the binary search tree.
~ current_node, which represents the node we're currently examining.

We start by setting current_node to the root of the tree if it's not provided.

2. Edge Case.

            if current_node is None:
                return None
                
For our edge case, we check if the current_node is None, which would happen if we've reached a leaf node without finding the value.

In that case, we simply return None to indicate that the value is not present in the tree.

3. Base Case.

            if value == current_node.data:
                return current_node

For our base case, we check if the value we're looking for is equal to the data stored in the current_node.

If they are equal, we've found the value we're searching for, and we return the current_node.

4. Recursive Case.

There are two possible recursive cases depending on the value of current_node.

Case I: Current Node > Search Value

            elif value < current_node.data:
                return self.search(value, current_node.left) if current_node.left else None

If the value we're looking for is less than the data in the current_node, that means the value we're searching for might be in the left subtree.

We recursively call the search function on the left child of the current_node, if it exists.

If the left child is None, meaning there's no left subtree, we return None since the value isn't present in that direction.

Case II: Current Node < Search Value

            else:
                return self.search(value, current_node.right) if current_node.right 

If the value is greater than the data in the current_node, we need to search in the right subtree.

We recursively call the search function on the right child of the current_node, if it exists.

If the right child is None, we return None as the value isn't present in that part of the tree.
"""

#.........Source Code: BST Search Operation..........
"""
*****************************************************************************************
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def search(self, value, current_node=None):

        if current_node is None:
            return None

        if value == current_node.data:
            return current_node
        elif value < current_node.data:
            return self.search(value, current_node.left) if current_node.left else None
        else:
            return self.search(value, current_node.right) if current_node.right else None
        

*****************************************************************************************
"""

"""
...........................BST Insertion Operations........................
An element is inserted into a BST as the earliest possible leaf node.

Insertion in BST can be solved by answering two sets of questions.

Question I: Is our element greater than the node we are currently at?

Yes: Move towards the right subtree.
No: Move towards the left subtree.
Question II: Can we add a child to the existing node in that direction?

Yes: Add the element there.
No: Keep searching for the node where the answer is yes.

...........................Working of BST Insertion..........................
Let's understand this with an example.
Consider the following tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.12.png

Case I: Adding a Child Node Is Possible
Let's try to add 6 in this tree.

Step I:
Question I: Check is 6 > 7 ?
As the answer is no, we have to move towards the left.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.13.png

Question II: Can a leaf node be added as a left child of 7 ?
Each node of binary trees can have utmost two child nodes and 7 currently only has one child node which is a right node.

So, the answer is yes.

Hence, we add 6 right there.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.14.png

Case II: Child Node Can't Be Added
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.15.png

Now let's try adding 8 to the tree next.

Step I
Question I: Is 8 > 7?
As the answer is yes we have to move towards the right .

Question II: Can We Add a Child in This Direction?
Unfortunately, 7 already has 10 as its right node .

So, we can't add 8 here.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.16.png

So we continue with the search process and traverse to 10.

Step II
Question I: Is 8 > 10 ?
The answer is no. So, we have to move towards the left.

Question II: Can We Add a Child Node Here ?
Once again 10 already has a left node 9.

So, we can't add 8 here as well.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.17.png

We then arrive at 9.

Step III:
Question I: Is 8 > 9 ?
The answer is no and now we must again move left.

Question II: Can we add a child in this direction ?
This time, the answer is yes so we can add 8 as a left child of 9 and complete our insertion process.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.18.png


.....................Thought Process: BST Insertion Operations....................
We can implement insertion in BST in the following steps.

1. Defining the function.

        def insert(self, value, current_node=None):

First, let's define our method insert(), which takes in two parameters:

* value, which is the value we want to insert for in the binary search tree
* current_node, which represents the node we're currently examining.

2. Solving our problem case.
Based on the value to be inserted we can have two cases.

Case I: Current Node > Value
If the value we want to insert is less than the data in the current_node, we need to insert it into the left subtree.

        if value < current_node.data:
            if current_node.left is None:
                current_node.left = BinarySearchTreeNode(value)
            else:
                self.insert(value, current_node.left)

If the left child of the current_node is None, we can directly create a new node with the given value and set it as the left child.

If the left child already exists, we recursively call the insert function on the left child to continue traversing the tree until we find an appropriate spot for insertion.

Case II: Current Node < Value

If the value is greater than the data in the current_node, we need to insert it into the right subtree.

elif value > current_node.data:
    if current_node.right is None:
        current_node.right = BinarySearchTreeNode(value)
    else:
        self.insert(value, current_node.right)
If the right child of the current_node is None, we create a new node with the given value and set it as the right child.

If the right child already exists, we recursively call the insert function on the right child.

.....................Insert into Empty BST...................
First, we need to make sure the tree is not empty.

If the root itself is None, indicating an empty tree, we directly create a new node with the given value and set it as the root of the tree.

If the tree is not empty, we proceed to insert into the tree starting from the root.

        if self.root is None:
            self.root = BinarySearchTreeNode(value)
            return

"""

#........Source Code: BST Insertion Operation.............
"""
************************************************************************************
def insert(self, value, current_node=None):
    if self.root is None:
        self.root = BinarySearchTreeNode(value)
        return

    if current_node is None:
        current_node = self.root

    if value < current_node.data:
        if current_node.left is None:
            current_node.left = BinarySearchTreeNode(value)
        else:
            self.insert(value, current_node.left)
    elif value > current_node.data:
        if current_node.right is None:
            current_node.right = BinarySearchTreeNode(value)
        else:
            self.insert(value, current_node.right)

def inorder_traversal(self, node, visited_nodes=None):
        if visited_nodes is None:
            visited_nodes = []

        if node:
            self.inorder_traversal(node.left, visited_nodes)
            visited_nodes.append(node.data)
            self.inorder_traversal(node.right, visited_nodes)

        return visited_nodes

bst = BinarySearchTree()

values_to_insert = [1,2,3,4,5]

for value in values_to_insert:
    bst.insert(value)

print(f'Inorder Traversal after Insertion {bst.inorder_traversal(bst.root)}')

************************************************************************************
"""


"""
Output

Inorder Traversal after Insertion [1, 2, 3, 4, 5]
Here, initially we start each insertion from root. This is signified by the code:
        if current_node is None:
            current_node = self.root
"""



"""
...........................BST Deletion Operation..............
Depending upon the position of node to be deleted, BST deletion has three cases:
* Deleting leaf node
* Deleting node with one child
* Deleting node with two children

................BST Deletion : Deleting Leaf Node..............
If the node to be deleted is a leaf node, then simply delete the node.

For example, consider the following tree:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.19.png

Here 4 is to be deleted so we simply delete the node.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.20.png

........................BST Deletion: Deleting Node With One Child
If the node has one child then,
* Replace that node with its child node.
* Remove the child node from its original position.

Consider the following tree:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.21.png

Here 6 is to be deleted.

Step I: Copy the value of its child.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.22.png

So,we first replace 6 with a copy of its inorder successor (7).

Step II: Remove the child node from its original position.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.23.png

And then we delete the original instance of 7.
"""


"""
.......................BST Deletion: Deleting Node With Two Children.................
If the node has two children then,
* Replace the node with the inorder successor.
* Remove the inorder successor from its original position.

Consider the following tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.24.png

Here 3 is to be deleted.

Step I: Replace the node with its inorder successor.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.25.png

Step II: Delete the inorder successor
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.26.png

Now, we delete 4 from its original position.

......................Thought Process: BST Deletion Operation...................
We can implement deletion in BST in the following steps.

1. Defining the function.

        def delete(self, root, value):

We start implementing deletion by defining our delete() method which takes two parameters;
    *value
    *root

2. Recursive Case.
Next, we compare the value to the data in the root.
Based on the result we can have two cases:

Case I: Root Node > Value

        # if the value to be deleted is smaller than the root's value, 
        #then it lies in the left subtree
        if value < root.data:
            root.left = self.delete(root.left, value)

If the value is smaller, it means the node to be deleted is in the left subtree.

We recursively call the delete function on the left child of the root to continue searching for the node to delete in that subtree.

Case II: Root Node < Value

        # if the value to be deleted is larger than the root's value, 
        #then it lies in the right subtree
        elif value > root.data:
            root.right = self.delete(root.right, value)

If the value is greater than the data in the root, we recursively call the delete function on the right child of the root to continue searching in the right subtree.

3. Deleting the node.
We have found our node to be deleted if the value is the same as the value of the root for a particular subtree.

Here we have to address two cases:

Case I: Node with no or only one child

        # node with only one child or no child
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp

If the node has no children, we simply remove it.

And, if the node has one child,we simply connect its parent directly to its child.

Case II: Node with two children

        # Node with two children
        temp = root.right
        while temp.left:
            temp = temp.left
        # copy the inorder successor's content to this node
        root.data = temp.data  
        # delete the inorder successor
        root.right = self.delete(root.right, temp.data)  

If the node has two children,we find the node's inorder successor (the smallest node in the right subtree).

We then copy the inorder successor's data to the node and recursively delete the inorder successor.

4. Base Case.

        # base case: If the root is None, return None
        if not root:
            return root

For our base case, we simply return the root if our tree is empty.
This also serves as error handling as root refers to the subtree root when called during recursion.

        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
            
So, if we reach the leaf nodes and still fail to find our value to be deleted,then both root.left and root.right used during the recursive case will return None. Hence, the entire base case will return None.
"""

#.....................Source Code: BST Deletion Operation..................
"""Now that we have coded every logic necessary, let's combine each block of code into a single method."""

"""
**************************************************************************************
def delete(self, root, value):
    if not root:
        return root

    if value < root.data:
        root.left = self.delete(root.left, value)
    elif value > root.data:
        root.right = self.delete(root.right, value)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp

        temp = root.right
        while temp.left:
            temp = temp.left
        root.data = temp.data
        root.right = self.delete(root.right, temp.data)

    return root

**************************************************************************************
"""


"""
............Find the Lowest Common Ancestor (LCA) of two nodes in a BST........
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.28.png

The LCA of two nodes is the deepest node that has both the nodes as its descendant.

Write a program to find the LCA of two given nodes in a BST.

* Define a method find_LCA() which takes three arguments: current_node, p and q.
* p and q are the nodes whose LCA we must find.
* Inside the method,compare p and q with the value of the current_node and define three cases:
    * If both p and q are greater than current node's data, then LCA lies in the right subtree
    * If both p and q are smaller than current node's data, then LCA lies in the left subtree.
    * If one of p or q is smaller and the other is greater than current node's data, then current_node is the LCA.
* Return the LCA once you have checked every ancestor of the given nodes.


 def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case: If the current node is None or equals to p or q, return it.

        if root is None or root == p or root == q:
            return root

        # Recursively search in the left and right subtrees

        left_lca = lowestCommonAncestor(root.left, p, q)
        right_lca = lowestCommonAncestor(root.right, p, q)

        # If both left and right subtrees return non-None values,
        # it means p and q are in different subtrees, so the current root is the LCA.

        if left_lca and right_lca:
            return root

        # If only one subtree returns a non-None value, that value is the LCA (or contains the LCA).

        elif left_lca:
            return left_lca
        else:
            return right_lca
"""

"""
...........................Combining Up To Now: Binary Search Tree.....................
To implement our Binary Search Tree, the class structure and the lines of code for inorder traversal will be the same.

We will just name the classes BinaryTreeNode and BinaryTree to BinarySearchTreeNode and BinarySearchTree respectively to denote we are dealing with BST.

Now let's combine all the individual methods for search, insertion, and deletion to get a fully functioning BST.
"""

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value, current_node=None):
        if self.root is None:
            self.root = BinarySearchTreeNode(value)
            return
    
        if current_node is None:
            current_node = self.root

        if value < current_node.data:
            if current_node.left is None:
                current_node.left = BinarySearchTreeNode(value)
            else:
                self.insert(value, current_node.left)
        elif value > current_node.data:
            if current_node.right is None:
                current_node.right = BinarySearchTreeNode(value)
            else:
                self.insert(value, current_node.right)
        else:
            current_node.right = BinarySearchTreeNode(value)

    def search(self, value, current_node=None):
        if current_node is None:
            current_node = self.root

        if current_node is None:
            return None

        if value == current_node.data:
            return current_node
        elif value < current_node.data:
            return self.search(value, current_node.left) if current_node.left else None
        else:
            return self.search(value, current_node.right) if current_node.right else None

    def delete(self, root, key):
        if not root:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = root.right
            while temp.left:
                temp = temp.left
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root

    def inorder_traversal(self, node, visited_nodes=None):
        if visited_nodes is None:
            visited_nodes = []

        if node:
            self.inorder_traversal(node.left, visited_nodes)
            visited_nodes.append(node.data)
            self.inorder_traversal(node.right, visited_nodes)

        return visited_nodes
    

    def find_LCA(self, current_node, p, q):
            # write your code here
        if current_node is None or current_node == p or current_node == q:
            return current_node

        left_lca = self.find_LCA(current_node.left, p, q)
        right_lca = self.find_LCA(current_node.right, p, q)

        if left_lca and right_lca:
            return current_node

        elif left_lca:
            return left_lca
            
        else:
            return right_lca


bst = BinarySearchTree()

values_to_insert = [1,2,3,4,5]

for value in values_to_insert:
    bst.insert(value)

print(f'Inorder Traversal after Insertion {bst.inorder_traversal(bst.root)}')

values_to_search = [2,3,6]

for value in values_to_search:
    node = bst.search(value)
    print(f'Search for {value}: {"Found" if node else "Not Found"}')

values_to_delete = [2]

for value in values_to_delete:
    bst.root = bst.delete(bst.root, value)

print(f'Inorder Traversal after Deletion {bst.inorder_traversal(bst.root)}')

"""
Output:
    Inorder Traversal after Insertion [1, 2, 3, 4, 5]
    True
    True
    None
    Inorder Traversal after Deletion [1, 3, 4, 5]
"""

for value in values_to_insert:
    bst.insert(value)

# find the LCA of two nodes
value1 = 2
value2 = 4

node1 = bst.search(value1)
node2 = bst.search(value2)

if node1 and node2:  # ensure both nodes are found in the tree
    lca = bst.find_LCA(bst.root,node1, node2)
    print(f'LCA of {value1} and {value2}: {lca.data if lca else "None"}')



"""
....................Performance of a Binary Search Tree..................
Let's revisit the example from BST search operation and experiment with some changes.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.7.29.png

Now take a moment to answer the question: Given the same elements, will our tree always look the same ?

Let's try creating this tree from scratch.

One of the order to create a tree like this is:

        8 -> 3 -> 10 -> 1 -> 6 -> 14 -> 4 ->7

Now let's take the same elements but change the order of elements as

        1 -> 3 -> 10 -> 6 -> 14 -> 4 -> 7

NOTE: As we can see from the figure, height of the tree has increased and as the time complexity of a search operation is O(h), the time to locate a leaf node now increases.

Changes will take place for both insertion and deletion of elements as well in the new tree even if they contain the same elements.

Depending upon the order of insertion it's a high possibility that our BST may turn into a degenerate tree.

Therefore, a BST is a powerful and versatile implementation for sorted maps or lists but definitely not the most efficient.

It would be much more efficient if we could implement them using a different class of data structures that retain their structure despite the sequence of insertion of elements during the creation.


.......................Complexity Analysis of BST Operations.................
For any operation (insertion, deletion, and search), we might need to traverse to the bottom of the tree. Thus, for a tree of height h,

Time Complexity: O(h)

This can be optimised by uniformly distributing the nodes on either side of the tree.

To see how the complexity of BST operations evolve with the skewness of the tree, refer to this blog.
"""