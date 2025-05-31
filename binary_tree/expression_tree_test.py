#...............Create an Expression Tree...............
# Write a program to evaluate the given expression.

    # First create an expression tree.
    # Define the nodes and link them.
    # Complete inorder_and_evaluate()method to get the inorder expression of the tree and evaluate the expression.

# Expression: [(1+3) - 2] * [(4+5) - 11]

# Expected Output
# (((1 + 3) - 2) * ((4 + 5) - 11))
# -4

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

    def inorder_and_evaluate(self, node):
        if not node:
            return "", 0

        # if left and right children are None, then it's a leaf node
        # we assume it's an operand and return its value
        if not node.left and not node.right:
            return str(node.data), int(node.data)

        # evaluate and traverse left subtree
        left_expr, left_val = self.inorder_and_evaluate(node.left)
        # evaluate and traverse right subtree
        right_expr, right_val = self.inorder_and_evaluate(node.right)

        # combine the expressions
        combined_expr = f"({left_expr} {node.data} {right_expr})"
        
        # evaluate based on the operator
        if node.data == '+':
            return combined_expr, left_val + right_val
        elif node.data == '-':
            return combined_expr, left_val - right_val
        elif node.data == '*':
            return combined_expr, left_val * right_val
        elif node.data == '/':
            return combined_expr, left_val / right_val

# creating nodes
root_node = BinaryTreeNode("*")

# create other nodes
node1 = BinaryTreeNode("-")
node2 = BinaryTreeNode("-")
node3 = BinaryTreeNode("+")
node4 = BinaryTreeNode("2")
node5 = BinaryTreeNode("+")
node6 = BinaryTreeNode("11")
node7 = BinaryTreeNode("1")
node8 = BinaryTreeNode("3")
node9 = BinaryTreeNode("4")
node10 = BinaryTreeNode("5")


# linking nodes
root_node.add_left_child(node1)
root_node.add_right_child(node2)

node1.add_left_child(node3)
node1.add_right_child(node4)

node2.add_left_child(node5)
node2.add_right_child(node6)

node3.add_left_child(node7)
node3.add_right_child(node8)

node5.add_left_child(node9)
node5.add_right_child(node10)

# creating binary tree
tree = BinaryTree(root_node)
expression, result = tree.inorder_and_evaluate(tree.root)
print(expression)
print(result)