#................Introduction to Traversal.................
# A traversal of a tree is a systematic way of accessing all the nodes of a tree.

# When combined with other properties of a tree, it can correctly represent both node data and node relationships.

# In this lesson, we will look at the following three different ways to traverse a tree:
    # Preorder Traversal
    # Postorder Traversal
    # Breadth First/ Level Order Traversal

#................Preorder Traversal....................
# Preorder traversal explores the tree in a root-left-right manner.
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.1.png

# Two things to remember in preorder traversal:
    # *Traversal takes from left to right.
    # *If the left child has descendants, you'll explore the left subtree fully before checking out the right one.
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.2.png

#................Real-Life Analogy: Preorder Traversal.............
# Creating a lesson plan followed in a course is a great way to understand the concept of preorder traversal.

# As there are a lot of topics to cover, we lay out the course structure using a tree diagram.
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.4.png

# If we approach this course randomly, we will be lost.

# However, by using preorder traversal for the given tree, we can get the perfect lesson plan to follow.
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.5.png

# We start at the root, which means we first learn Introduction to DSA.

# Then, we take a moment to understand the need for data structures under Why DSA and begin our journey by understanding the concept of Linear Data Structures.
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.6.png

# After familiarizing ourselves with the concept of linear data structures, we now examine special types of linear data structures, starting with Stack and moving on to Queue.

# After completing linear data structures, we move on to understanding the concepts of Nonlinear Data Structures.
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.7.png

# Now, we arrive at our first implementation of nonlinear data structures with Tree.

# NOTE: Preorder traversal should be used in a general tree data structure when the goal is to manipulate the current node before its children nodes.

#...................Thought Process: Preorder Traversal.............
# So, let's implement preorder traversal by creating the preorder_traversal() method inside the Tree class.

#         def preorder_traversal(self, node, traversal=[]):
      
# Our method will only take in two arguments:
  #*node, which is the current node we are at.
  #*traversal, which is a list to store the order of traversal.

# Now, let's define our cases for recursion.

# Base Case:
#         if not node:
#             return traversal
# For our tree traversal, the base case is straightforward. If the node is None (or doesn't exist), return without doing anything.

# Recursive Case
# There are two actions we perform during recursion:
# 1. Visit the current node.
#         # append the root node first
#         traversal.append(node.data)

# Start with the root node A. Then, append the value to traversal.

# 2. Recur on Its Children.

          ## then visit the children
#         for child in node.children:
#             self.preorder_traversal(child, traversal)

# For each child of the current node, call the same traversal function. This is where the recursive magic happens.

# When we call the function on the child node, it will repeat the process:
    #*Visit the child node.
    #*Call the function on its children, which will then call the function on their children, and so on.

#................Source Code: Preorder Traversal..............
# Now, let's combine everything we have done so far and fully implement the preorder traversal of the above general tree.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, root=None):
        self.root = root

    def preorder_traversal(self, node, traversal=[]):
       # if no nodes are left,
       # end the recursion
       if not node:
           return traversal
      
       # append node data
       traversal.append(node.data)

       for child in node.children:
           # recursively traverse child nodes
           self.preorder_traversal(child, traversal)
      
       return traversal

A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F')
G = TreeNode('G')

A.add_child(B)
A.add_child(C)
A.add_child(D)
B.add_child(E)
B.add_child(F)
E.add_child(G)

general_tree = Tree(A)
print(f"Preorder Traversal: {general_tree.preorder_traversal(general_tree.root)}")