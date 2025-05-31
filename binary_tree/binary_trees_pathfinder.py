# Coding a pathfinder! Here's how it works:

# This code lets you explore every nook and cranny of a binary tree. Imagine it as a guide on a treasure hunt, tracing every root-to-leaf path and proudly displaying each finding.

# It starts by defining nodes and a tree, then prints all routes from the mighty root to each little leaf. Handy for anyone venturing into tree structures!

# Each node is an adventurer with the power to branch out, left or right. Paths are printed whenever these adventurers meet their final destination - a leaf!

# Input your journey's stops and watch it unveil every path taken in a beautiful order.

# Ever thought of coding as arranging a treasure map? Why not try creating a larger tree next time, and see what new paths unfold?

# Write a program to print all the paths from the root node to the leaf nodes of a given binary tree.
#     *Define a method, print_paths(), which takes two      arguments: current_node and path (where path is a list of nodes visited during traversal).
#     *Start from the root and traverse your way down to every leaf node.
#     *While traversing, keep storing the nodes in a list.
#     *Print the list when you reach a leaf node.
#     *Return the list once you have traversed every node.

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

    def print_all_paths(self):
        self.print_paths(self.root, [])

    def print_paths(self, current_node, path):
        if current_node is None:
            return

        # append the current node to the path
        path.append(current_node.data)

        # if it's a leaf node, print the path
        if current_node.left is None and current_node.right is None:
            print(path)
        else:
            # otherwise, continue with the left and right children
            self.print_paths(current_node.left, path.copy())
            self.print_paths(current_node.right, path.copy())

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
tree.print_all_paths()