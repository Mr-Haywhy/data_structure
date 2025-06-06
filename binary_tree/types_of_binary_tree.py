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
input_str = input()
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