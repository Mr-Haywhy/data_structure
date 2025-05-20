#..................Postorder Traversal...................
# Postorder traversal explores the tree in a left-right-root manner.
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.14.png
# Here, we fully explore each child subtree before visiting the root node.

# ..............Real-Life Analogy: Postorder Traversal.........
# Imagine writing a research paper.

# Let's represent its structure using a tree for better planning
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.16.png

# As there are a lot of parts involved, we need to plan our workflow very carefully.

# This can be done using postorder traversal.
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.17.png

# We start with writing our introduction.
# We then collect our data and analyze it. Now, we can define our methodology.
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.18.png

# After that, we have to list our findings and deliver our discussion. Doing this will enable us to present our results.
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.19.png

# In the end, we should prepare a summary of our work and mention the works we plan to do in the future. From this information, we can now present our concluding statements.

# Once we have done all this, we can finally combine them to file our research paper.

# NOTE: Postorder traversal should be used in a general tree data structure where the parent node's computation or operation is dependent on the results of its children.

#...........Thought Process: Postorder Traversal
# We will again use recursion to implement our traversal method.

        # def post_order_traversal(self, node):

# Now, let's define the cases for recursion.

# Base Case
        # if not node:
        #     return
# For our postorder tree traversal, the base case is the same as preorder traversal. If the node is null (or doesn't exist), return without doing anything.

# Recursive Case
# Even in our recursive case, the operations performed are the same; only their order is different.

# So our recursion takes place in the following order:

# 1. Recur on the children first.

        # for child in node.children:  
        #     self.post_order_traversal(child)

# We start at the root and immediately call the recursion on its left child. This recursive function keeps on running until we finally encounter a left child, which happens to be a leaf node.

# 2. Print the node.

        # # then visit the node itself
        # print(node.data)

# After all the child subtrees have been traversed, we finally print the current node.

#.............Source Code: Postorder Traversal................
# Now that we have understood how the code works, let's combine the blocks of code and view our results.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, root=None):
        self.root = root
        
    def postorder_traversal(self, node, traversal=[]):
        if not node:
           return traversal
    
        for child in node.children:
           # recursively traverse child nodes
           self.postorder_traversal(child, traversal)
    
       # append nodes after visiting all
       # the child nodes of a parent
        traversal.append(node.data)
        print(traversal)
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
print(f'Postorder Traversal: {general_tree.postorder_traversal(general_tree.root)}')

# Let us use the above code to find the postorder traversal of the following tree.
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.20.png

# Output: Postorder Traversal: ['G', 'E', 'F', 'B', 'C', 'D', 'A']