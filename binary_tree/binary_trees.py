# ............What are Binary Trees?............
# A binary tree is a tree that has, at most, two children.

# A simple binary tree is visualized as:
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.1.1.png

# The properties of binary tree are:

# *Every node has, at most, two children.
# *Each child node is classified as either a left node or a right node.
# *The left child always precedes the right child in the order of the nodes.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.1.2.png

# ...........Why Binary Trees?...............
# Suppose, you're contemplating a new job opportunity and find it challenging to make a decision. Given the significance of this choice, you want to consider all factors thoroughly.

# This is where a solid understanding of data structures can simplify your life. Trees can help you visualize and evaluate various outcomes across multiple scenarios.

# To organize your thoughts, you can represent each question or decision point as a node in a tree using a straightforward yes-no format.

# In this setup:
#     Yes: becomes the right child of the node.
#     No: answer becomes the left child.
# This structure results in a decision tree that can guide your thought process.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.1.3.png

# Now that we know the nature and use of binary trees, we will next discuss the various properties that set it apart from general trees.

# ...........Properties of a Binary Tree...........
# Binary Trees will naturally inherit fundamental characteristics like the anatomy and relationships of a general tree.

# The primary difference comes in the form of the degree of the nodes because, in a binary tree, we are limited to a maximum of degree two for each node.

# Because of this constraint, there are some interesting relationships between the number of nodes with respect to the height of the tree and the level.

# .............Maximum Number of Nodes at a Level...........
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.2.1.png

# There's an interesting relationship between the height and the number of nodes in a binary tree:

# Level 0 has at most one node.
# Level 1 has at most two nodes.
# Level 2 has at most four nodes, and so on.
# So, in general, level d has at most 2^d nodes.

# Thus, the maximum number of nodes on the levels of a binary tree grows exponentially as we go down the tree.

# ...........Maximum Number of Nodes in a Tree of a Particular Height............
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.2.2.png

# In general, a tree with height h has, at most, 
# 2^(h+1)−1 nodes.

# If we look at the figure above,

# A binary tree of height 0 has only 1 (2^(0+1)-1) node (the root node).
# A binary tree of height 1 has, at most, 3 (2^(1+1) -1) nodes.
# A binary tree of height 2 has a maximum of 7 (2^(2+1)-1) nodes and so on.

# ............Implementation of Binary Trees...............
# As binary trees are a variation of general trees, we can modify our code from general trees to match the characteristics of binary trees.

# Let's start by creating our nodes.

# .............Create Nodes.............
# A binary tree node will have three core information:
#     *The data value
#     *The location of the left child
#     *The location of the right child

# And unlike general trees, here we must define the child being added as a left or a right child.


# ...........Thought Process: Creating Nodes...........
# We can divide the entire process of creating nodes in a tree into the following steps.

# 1. Create a class to handle nodes.

#         class BinaryTreeNode:
#             def __init__(self, data):
#                 self.data = data
#                 self.left = None
#                 self.right = None
# Here we have defined a BinaryTreeNode class to handle all the creation of nodes needed in our tree.

# Inside the dunder method, we have added the following fields:

#     *self.data: The data value.
#     *self.left: The location of the left child.
#     *self.right: The location of the right child.

# 2. Create methods to add children to a node.

#             def add_left_child(self, node):
#                 self.left = node

#             def add_right_child(self, node):
#                 self.right = node
# As we need to explicitly define if a child is right or left child, we have created two methods:

#     *add_left_child(): attaches a left child to a node.
#     *add_right_child(): attaches a right child to a node.

# .............Create Tree...............
# Creating a binary tree is exactly the same as creating general trees once all the nodes have been created.

#         class BinaryTree:
#             def __init__(self, root=None):
#                 self.root = root

# Here, we have create a BinaryTree class to handle all operations in our binary tree.

# By creating an instance of the class, we can initialize a BinaryTree object with a selected node as the root.

# ............Combining the Classes.............
# So our combined code for Binary Tree looks like this
     
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

#     def add_left_child(self, node):
#         self.left = node

#     def add_right_child(self, node):
#         self.right = node

# class BinaryTree:
#     def __init__(self, root=None):
#         self.root = root

# binary_tree = BinaryTree()

# As we haven't created any nodes nor defined any hierarchy, there's nothing to process here yet.

# So, we will be creating a sample tree using this skeletal code next.

# ..............Creating a Binary Tree............
# Let's take a sample tree like this.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.3.1.png

# We can create this binary tree in three steps.

# 1. Creating Nodes
# We create our nodes by creating an instance of BinaryTreeNode as:

# # creating nodes
# root_node = BinaryTreeNode("root")
# left_node = BinaryTreeNode("left")
# right_node = BinaryTreeNode("right")

# 2. Adding Children
# Now we assign proper hierarchy to the tree as:

# # linking nodes
# root_node.add_left_child(left_node)
# root_node.add_right_child(right_node)

# 3. Creating the Tree
# Finally, we can create our binary tree by creating an instance of BinaryTree.

# # creating binary tree
# tree = BinaryTree(root_node)

# .............Source Code: Binary Trees.............
# If we combine all of the individual blocks of code together, we should get a fully-fledged program to implement a binary tree.

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        print(f'Node {data} was created')

    def add_left_child(self, node):
        self.left = node
        print(f'Node {node.data} was added as a left child of {self.data}')

    def add_right_child(self, node):
        self.right = node
        print(f'Node {node.data} was added as a right child of {self.data}')
    
class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        print('A tree was created')

# creating nodes
root_node = BinaryTreeNode("root")
left_node = BinaryTreeNode("left")
right_node = BinaryTreeNode("right")

# linking nodes
root_node.add_left_child(left_node)
root_node.add_right_child(right_node)

# creating binary tree
tree = BinaryTree(root_node)

# ........Output.........
#     Node root was created
#     Node left was created
#     Node right was created
#     Node left was added as a left child of root
#     Node right was added as a right child of root
#     A tree was created

# However, like with the implementation of general trees, this code is incomplete without methods of traversals.