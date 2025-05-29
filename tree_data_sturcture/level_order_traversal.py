# ......Breadth-First Tree Traversal (Level Order Traversal).....
# Level order traversal, also known as breadth-first search, visits nodes in a level-by-level manner.

# For any general tree, we start from the root, visit all nodes at the current level, and then move to the next level.

# Let's clarify this with an example.
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.24.png

# .........Real-Life Analogy: Breadth-First Traversal........
# One of the best ways to understand breadth-first traversal is through an organizational hierarchy.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.26.png

# Now, if we apply breadth-first traversal to the tree, we can quickly determine the chain of command in the organization.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.27.png

# As per our traversal, we see that:
# *Level 0: CEO has the highest authority in the organization.
# *Level 1: CTO, CFO, and COO all have the same authority and answer directly to the CEO.
# *Level 2: The Managers all hold the same degree of authority.

# ..........Thought Process: Breadth-First Traversal...........
# Let's try to list the fundamental steps in implementing breadth-first traversal.

# If a node is at level n, all of its children will be at level n+1.

# So, the steps involved in the breadth-first approach are:

#     *Visit the root node.
#     *Visit all children of the root node.
#     *Repeat for all children nodes.

# A queue is the ideal data structure for this traversal.

# The process starts by visiting the root node and enqueuing its children at the back of the queue.

# As each node is visited, its children are enqueued to the back, and the node is dequeued from the front.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.28.png

# This way, all the children are visited before any of the grandchildren, as required.

# We can implement breadth-first traversal in the following steps.

# 1. Define the methods.

#         def breadth_first_traversal(self):
#             if not self.root:
#                 return
            
# We have to define our breadth_first_traversal() method and check if the tree is empty.

# 2. Create a queue.

# # we use a queue to keep track of nodes to visit
#         queue = deque()  

# Next, we create a queue by initializing a deque object from the Python collections module. This queue will help us keep track of the nodes that we need to visit.

#         queue.append(self.root)

# We add the root node to the queue as it is the first node that needs to be visited.

#         traversal = [] 

# We then create a list to store the nodes visited in level order.

# NOTE: We need a queue to implement breadth-first traversal. There is no queue library. So, we import the doubly-ended queue (deque) library from the collections module.

# 3. Define our loop.

# Now, let's make use of a loop that will continue until there are no more nodes in the queue.

# Inside this loop:

# 1. Dequeue the first node.

#         while queue:
#             # We use a queue: FIFO
#             current_node = queue.popleft()
#             # Append the data to the list
#             traversal.append(current_node.data) 

# We will first dequeue the first node in the queue using the popleft function and append its data to traversal. This node represents the next node at the current level that needs to be visited.

# 2. Iterate over the children node.

#         for child in current_node.children:
#             queue.append(child)

# We then iterate over the children of the current node (if any) and add them to the back of the queue.

# By doing this, we ensure that all nodes at the next level will be visited in the order they were added.

# The loop repeats the steps above until all nodes in the queue have been visited, ensuring that the entire tree has been traversed in a breadth-first manner.

# ........Source Code: Breadth-First Traversal..........
# Let's combine all of the blocks of code and realize the level order traversal of a tree.

from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, root=None):
        self.root = root
        
    def breadth_first_traversal(self):
        if not self.root:
            return []

        queue = deque()
        queue.append(self.root)
        
        traversal = [] 

        while queue:
            # we use a queue: FIFO
            current_node = queue.popleft()
            # append the data to the list
            traversal.append(current_node.data)  
    
            for child in current_node.children:
                queue.append(child)
    
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
print(f'Breadth First Traversal: {general_tree.breadth_first_traversal()}')

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.29.png

# Output

# Breadth First Traversal: ['A', 'B', 'C', 'D', 'E', 'F', 'G']