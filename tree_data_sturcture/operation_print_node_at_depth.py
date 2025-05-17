#....................Operation: Print Nodes at a Particular Depth..................
# Since the tree data structure is non-linear, there isn't really a straightforward way to print trees to show all nodes and relationships.
# One of the ways of printing a tree is to print it depthwise.

# Consider the following tree: https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.3.6.png

# Here's an explanation of how the logic works:

# We can have three cases here:
# 1. Base Case:
        # if not node:
        #     return []

# If the node is None, return an empty list as there are no more nodes to process.

# 2. Depth Equals Zero:
        # if depth == 0:
        #     return [node.data]

# If the given depth equals 0, we are at the root.
# So, the function returns a list containing the current node's data.

# 3. Recursive Case:
        # result = []
        # for child in node.children:
        #     result += self.get_nodes_at_depth(child, depth - 1)
        # return result

# If the given depth k is greater than 0, then we recursively call get_nodes_at_depth() for each child with depth−1 as the depth.

# The recursive call reduces the depth by 1 for each child, effectively moving down one level in the tree.

# The function collects the results from all the recursive calls into a single list and returns it.

#...............Source Code: Print Nodes at a Particular Depth...........
# Let's try to include a print statement for each of the outputs and observe the result.


# create a class to handle the creation of node and addition of child nodes
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# class to handle the creation of trees and operations performed in it
class Tree:
    def __init__(self, root=None):
        self.root = root
    
    def get_nodes_at_depth(self, node, depth):
        if not node:
            return []
        
        if depth == 0:
            return [node.data]
        
        if node and depth > 0:
            result = []
            for child in node.children:
                result += self.get_nodes_at_depth(child, depth - 1)
            return result

# creating our root node
root = TreeNode("Book")

# creating the children of root
child1 = TreeNode(1)
child2 = TreeNode(2)
child3 = TreeNode(3)

# creating our leaf nodes
child1_1 = TreeNode(1.1)
child1_2 = TreeNode(1.2)
child1_3 = TreeNode(1.3)
child1_4 = TreeNode(1.4)
child2_1 = TreeNode(2.1)
child3_1 = TreeNode(3.1)
child3_2 = TreeNode(3.2)
child3_3 = TreeNode(3.3)

# describing relationships between the nodes

# add children to the root node
root.add_child(child1)
root.add_child(child2)
root.add_child(child3)

# add children to child1
child1.add_child(child1_1)
child1.add_child(child1_2)
child1.add_child(child1_3)
child1.add_child(child1_4)

# add children to child2
child2.add_child(child2_1)

# add children to child3
child3.add_child(child3_1)
child3.add_child(child3_2)
child3.add_child(child3_3)

# creating our tree
tree = Tree(root)
for i in range(0,3):
    print(f"nodes at depth {i}: {tree.get_nodes_at_depth(root, i)}")


# The method we used prints the nodes of the tree level by level, allowing us to visualize the tree's structure.

# While it doesn't show the parent-child relationships directly, the level-by-level output gives us a good sense of the tree's hierarchy.

# So, to better represent trees, let's look at some tree traversal techniques.


# a class to create and add nodes
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# a class to create a tree and perform tree operations
class Tree:
    def __init__(self, root=None):
        self.root = root
    
    def get_nodes_at_depth(self, node, depth, level=0):
        if not node:
            return []
        
        if depth == level:
            print(f"Nodes at Level {level}: {node.data}")
            return [node.data]
        
        if node and depth > level:
            result = []
            for child in node.children:
                result += self.get_nodes_at_depth(child, depth, level + 1)
            return result

# create the root node
root = TreeNode("root")

# create leaf nodes
child1 = TreeNode(1)
child1_1 = TreeNode(2)
child1_1_1 = TreeNode(3)

# describe relationships between the nodes
root.add_child(child1)
child1.add_child(child1_1)
child1_1.add_child(child1_1_1)

# create the tree
general_tree = Tree(root)

# get nodes at each level
for i in range(0, 4):
    general_tree.get_nodes_at_depth(root, i)