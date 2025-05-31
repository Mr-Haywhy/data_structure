# ................Inorder Traversal...............
# Whilst preorder, postorder, and level order traversal work just fine with binary trees, there's a separate method of traversal unique to binary trees and its variant called inorder traversal.

# Inorder traversal follows a left-root-right approach.

# The trajectory of inorder traversal is like this:
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.4.2.png

# The trajectory followed during inorder traversal here is:
    # H -> D -> I -> B -> E -> A -> F -> C -> J -> G -> K.

# ............Thought Process: Inorder Traversal.............
# Let's break down our implementation into three separate steps.

# Defining the Method:

        # def inorder_traversal(self, node, visited_nodes=[])

# The function is initialized to take two arguments:

#   *node: is the current node
#   *visited_nodes: a list of nodes visited during traversal

# We initially set visited_nodes to be empty.

# Recursive Case:
# We enter recursion only if we encounter a node.

        # if node is not None:

# In order to implement inorder traversal, we will have to append our data to the list between two recursive cases.

# 1. Recur on the left child.

        # first recur for left child
        # self.inorder_traversal(node.left, visited_nodes)

# First we recursively call inorder_traversal() on the left child of the current node and print the data of the node.

# 2. Append node to the visited nodes.

        # then print the data of node
        # visited_nodes.append(node.data)

# We then append the node data to visited_node.

# 3. Recur on the right child.

        # now recur for right child
        # self.inorder_traversal(node.right, visited_nodes)

# We then define a recursive call on the right child of the current node.

# Base Case:
# For our base case, we return visited_nodes immediately if we encounter no node.

        # return visited_nodes

# After visiting the nodes and its subtrees, we return visited_nodes which now includes the inorder traversal of the tree.

# .............Source Code: Inorder Traversal.............
# So, if we combine this method in our existing tree, we get

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

    def inorder_traversal(self, node, visited_nodes=[]):
        if node is not None:
            # first recur for left child
            self.inorder_traversal(node.left, visited_nodes)
            # then print the data of node
            visited_nodes.append(node.data)
            # now recur for right child
            self.inorder_traversal(node.right, visited_nodes)
        return visited_nodes


# creating nodes
root_node = BinaryTreeNode("root")
left_node = BinaryTreeNode("left")
right_node = BinaryTreeNode("right")

# linking nodes
root_node.add_left_child(left_node)
root_node.add_right_child(right_node)

# creating binary tree
tree = BinaryTree(root_node)

# in-order traversal
visited_nodes = tree.inorder_traversal(tree.root)

# printing result
print(visited_nodes) 

# Output:
    # ['left', 'root', 'right']


#...............Complexity Analysis of Binary Tree Operations.............
# Before we move on to further examples, we need to understand the best and worst case performances of a binary tree. The time complexity for the binary tree operations we have studied until now are:

# Operation	Time Complexity
# Traversal	    O(n)
# Insertion	    O(1)