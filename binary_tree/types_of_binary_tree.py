# ............Types of Binary Tree.............
# Binary trees are classified into different types. In the following lessons, we will be discussing the following types of binary trees:

#         Full binary tree
#         Complete binary tree
#         Perfect binary tree
#         Degenerate tree

# ...........Full Binary Tree...........
# A full binary tree or a proper binary tree is a special type of binary tree in which every parent node has either two or no children.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.5.1.png

# .......Maximum and Minimum Full Binary Tree For A Given Height..........
# Any node in a full binary tree can have two or no child nodes.

# So, there are two heights where the maximum and minimum number of nodes are equal:

#     *Height 0: A singleton tree is the only case for a full binary tree of height 0.
#     *Height 1: For a full binary tree with height one there must be a root node and its two children.

# .........Minimum Case
# To create a full binary tree with height greater than one with the minimum number of nodes possible, we add two children to one of the siblings and no child to the other.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.5.2.png

# ..........Maximum Case
# To create a full binary tree with the maximum number of nodes for height greater than one, we add two children to both siblings.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.5.3.png


# ..............Properties of Full Binary Tree............
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.5.4.png

# If we compare the minimum and maximum cases for a given height side by side, we can get the range of values that the number of nodes lies in.

# In this case, we have the two cases for height three, where we can see:

#     *Number of internal(node) nodes ranges from 3 to 7.
#     *Number of external(leaf node) nodes ranges from 4 to 8.
#     *Total number of nodes ranges from 7 to 15.

# In general, we can state the following properties for a full binary tree.

# Let,
#     h = Height of the tree
#     I = Number of Internal Nodes
#     E = Number of External/Leaf Nodes
#     N = Total Number of Nodes 

# A full binary tree with the above specifications has the following properties.

# 1. Range of N (Total Number of Nodes)

#     2h+1 ≤ N ≤ 2^(h+1) - 1

# *Minimum value of N = 2h + 1
# *Maximum value of N = 2^(h+1) -1

# 2. Value of N (Total Number of Nodes) for Given I (Number of Internal Nodes) and E (Number of External/Leaf Nodes)

#     *N = 2I + 1
#     *N = 2E - 1

# 3. Range of E (Number of External/Leaf Nodes)

#     h+1 ≤ E ≤ 2^h

# *Minimum value of E = h+1
# *Maximum value of E = 2^h
 
# 4. Value of E (Number of External/Leaf Nodes) for Given I (Number of Internal Nodes) and N (Total Number of Nodes)

#     *E = I + 1
#     *E = (N+1)/2

# 5. Range of I (Number of Internal Nodes)

#     h ≤ I ≤ 2^h -1

# *Minimum value of I = h
# *Maximum value of N = 2^h+1 +1

# 6. Value of I (Number of Internal Nodes) for Given E (Number of External/Leaf Nodes) and N (Total Number of Nodes)

#         *I = (N-1)/2
#         *I = E - 1


#...........Check if a Given Tree is a Full Binary Tree.........
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.5.5.png

# Write a program to check if a given tree is a full binary tree or not.

# Define a method, is_full_binary_tree() which takes a single argument node which will be our root node.
# Inside the method, check for the following cases using recursive approaches:
#     *If the tree is empty, return True.
#     *If the tree is a singleton tree (only one node), return True.
#     *If a node has both left and right children, recursively check for the left and right subtrees.
#     *If the node has only one child, return False.


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_left_child(self, node):
        self.left = node

    def add_right_child(self, node):
        self.right = node

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def is_full_binary_tree(self, node=None):
        # write your code here
        if not node:
            return True
            
        if self.left and self.right:
            return self.is_full_binary_tree(self.left) and self.is_full_binary_tree(self.right)


# take user input
input_str = "1 2 3 4 5 6 7" #input() 
inputs = input_str.split()

root, node1, node2, node3, node4, node5, node6 = [BinaryTreeNode(val.strip()) for val in inputs]

root.add_left_child(node1)
root.add_right_child(node2)
node1.add_left_child(node3)
node1.add_right_child(node4)
node2.add_left_child(node5)
node2.add_right_child(node6)

# call the function
tree = BinaryTree(root)
print(tree.is_full_binary_tree())




# ...................Complete Binary Tree...................
# A complete binary tree is a binary tree in which all the levels, except possibly the last, are completely filled, and all nodes are as far left as possible.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.5.6.png

# ...................Perfect Binary Tree......................
# To be a perfect binary tree, every internal node has exactly two child nodes and all the leaf nodes are at the same level.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.5.7.png

# ..............Relationship Between Full, Complete, and Perfect Binary Tree..............
# From the definitions, we can infer some relationships:

# 1. A full binary tree is not necessarily a complete binary tree.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.5.8.png

# This is a full binary tree, but it's not a complete binary tree because the last level is not filled from left to right.

# 2. A complete binary tree is not necessarily a full binary tree.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.5.9.png

# This is a complete binary tree, but it's not a full binary tree because there's a node with only one child.

# 3. A perfect binary tree is a full and complete binary tree.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.5.10.png

# This is a tree where all internal nodes have two children and all leaves are at the same level.

# ....................Degenerate Tree.....................
# In degenerate trees, the parent nodes have at most one child node.

# This effectively transforms the tree into a linked list.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.5.11.png

# Degenerate trees represent the worst-case scenario where search and insertion operations take linear time.

# So, a degenerate tree is not something you generally aim for — it's a situation you try to avoid.

# ....................Application of Binary Trees..................
# Binary Trees are arguably the most popular variant of tree data structures and for good reasons.

# We discussed a very powerful application of binary trees with expression trees during inorder traversal which are heavily used in compiler design.

# On top of that, here are some standard cases in computer programming where binary trees are heavily used.

# 1. Binary Decision Trees

# We use these particular binary trees when we want to represent a variety of possible outcomes that can come from responding to a series of yes-or-no questions.

# We represent a question with an internal node and separate the two outcomes ("Yes" and "No") into two separate child nodes.

# Depending on whether the response to the question is "Yes" or "No," we move from the root to the left or right child of the current node.

# We trace a path in the tree from the root to a leaf by following an edge from a parent to a child with each choice we make.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.5.12.png

# Decision trees like the one above are a mainstay when it comes to classification and regression problems associated with Machine Learning Algorithms.

# This tree in particular is used by an AI code to classify a given animal as either a Hawk, a Penguin, a Dolphin or a Bear.

# 2. Spatial Partitioning

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.5.13.png

# There's a whole section of algorithms in computer graphics called spatial partitioning which uses binary trees to divide a space into smaller regions.

# These algorithms perform their own operations on the tree to manipulate the space to fit their use.