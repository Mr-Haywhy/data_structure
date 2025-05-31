# ...............Example: Expression Trees..............
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.4.3.png

# We can use a special type of binary tree called an Expression Tree to evaluate mathematical expressions.

# The expression tree in the figure is for the simple expression of 1+2.

# Expression trees are used in compilers and calculators to represent expressions in a structured manner.

# Here, the leaf nodes are associated with variables or constants, and the internal nodes are associated with one of the operators +, −, ×, and /.
    
# ............Thought Process: Creating Expression Trees..........
# We can clarify this with an example. Let's take the mathematical expression [{(3+1) *3} / {(9-5) + 2}] - [{3 * (7-4)} + 6] .

# Let's break down the concept of creating the tree.

# 1. Divide the subtrees.
# The outermost operation - divides our equation into two parts. These parts are the elements of our two subtrees.

# Here [{(3+1) *3} / {(9-5) + 2}] becomes our left subtree and [{3 *(7-4) }+ 6] becomes our right subtree.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.4.4.png

# 2. Handle each subtree.
# We treat each subtree as an individual tree and repeat the same process as earlier.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.4.5.png

# In our left subtree, division / is the outermost operation which becomes the left child of root.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.4.6.png

# In our right subtree, addition + is the outermost operation so it becomes the right child of the root.

# 3. Repeat.
# Since we have identified the outermost operation for each subtree, the subtrees can be divided into subtrees of their own. We continue this process until we reach the numbers which become our leaf nodes.

# So our final representation of the tree should look like this.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.4.7.png

# Now if we were to apply inorder traversal to the expression tree above we would get the infix notation of the given expression.

# Let's take it one step at a time and first create our Expression Tree.

# .................Expression Tree: Creating Our Tree..............
# We can break down the steps involved in creating a tree into three parts.

# Create the Nodes
# We can start implementing our tree by first creating our nodes.

#         # create the nodes
#         root_node = BinaryTreeNode("-")
#         node1 = BinaryTreeNode("/")
#         node2 = BinaryTreeNode("+")
#         node3 = BinaryTreeNode("*")
#         node4 = BinaryTreeNode("+")
#         node5 = BinaryTreeNode("*")
#         node6 = BinaryTreeNode("6")
#         node7 = BinaryTreeNode("+")
#         node8 = BinaryTreeNode("3")
#         node9 = BinaryTreeNode("-")
#         node10 = BinaryTreeNode("2")
#         node11 = BinaryTreeNode("3")
#         node12 = BinaryTreeNode("-")
#         node13 = BinaryTreeNode("3")
#         node14 = BinaryTreeNode("1")
#         node15 = BinaryTreeNode("9")
#         node16 = BinaryTreeNode("5")
#         node17 = BinaryTreeNode("7")
#         node18 = BinaryTreeNode("4")

# Assign Hierarchy
# After creating our node, let's assign the appropriate hierarchy to the nodes and link them.

#         # link the nodes
#         root_node.add_left_child(node1)
#         root_node.add_right_child(node2)

#         node1.add_left_child(node3)
#         node1.add_right_child(node4)

#         node2.add_left_child(node5)
#         node2.add_right_child(node6)

#         node3.add_left_child(node7)
#         node3.add_right_child(node8)

#         node4.add_left_child(node9)
#         node4.add_right_child(node10)

#         node5.add_left_child(node11)
#         node5.add_right_child(node12)

#         node7.add_left_child(node13)
#         node7.add_right_child(node14)

#         node9.add_left_child(node15)
#         node9.add_right_child(node16)

#         node12.add_left_child(node17)
#         node12.add_right_child(node18)

# Create the Tree:
#         # create binary tree
#         tree = BinaryTree(root_node)


# .............Inorder Output for Expression Trees............
# Before we define any logic to operate on our tree, let's just check the output of inorder traversal to verify the nodes are visited in the correct order.

# We can directly integrate our existing method of inorder traversal to this code to achieve this result.

        # def inorder_traversal(self, node, visited_nodes=[]):
        #     if node is not None:
        #         # first recur for left child
        #         self.inorder_traversal(node.left, visited_nodes)
        #         # then print the data of node
        #         visited_nodes.append(node.data)
        #         # now recur for right child
        #         self.inorder_traversal(node.right, visited_nodes)
        #     return visited_nodes

# Output
    # ['3', '+', '1', '*', '3', '/', '9', '-', '5', '+', '2', '-', '3', '*', '7', '-', '4', '+', '6']

# Our expression was [{(3+1) *3} / {(9-5) + 2}] - [{3 * (7-4)} + 6] and the output of our code is the elements in the same order excluding the parenthesis.

# The absence of parentheses in the output is expected, as the tree's structure inherently captures the precedence and grouping denoted by the parentheses in the original expression.

# When evaluating the expression using the tree, each subtree is processed first, reflecting the inherent grouping of the original expression.

# Thus, the tree provides a clear roadmap for the order of operations, making the parentheses redundant in the output.

# ................Expression Tree: Evaluating the Expression..............
# Now that we know we are on the right track, let's create another method to evaluate the expression.

# We can accomplish this in the following steps.

# 1. Define the method.

#         def evaluate(self, node):

# We begin by defining the method evaluate() which takes in a single argument node.

#         if not node:
#             return 0

# Now we have to check for the edge cases.

# If node doesn't exist , then we terminate the execution by returning 0.

#         if not node.left and not node.right:
#             return int(node.data)

# The leaf nodes of expression trees are always operands. So, we check if a node has its left or right child or not. If not, then we return the integer value contained by the leaf node.

# 2. Evaluate the subtree.

#         # Evaluate left subtree
#         left_val = self.evaluate(node.left)
#         # Evaluate right subtree
#         right_val = self.evaluate(node.right)

# In inorder fashion, we evaluate the left and right subtrees next beginning with the left subtree.

# 3. Check the operator.
# Now, we check the operator present in our node and perform the correct operation.

#         # Check which operator to apply and return the result
#         if node.data == '+':
#             return left_val + right_val
#         elif node.data == '-':
#             return left_val - right_val
#         elif node.data == '*':
#             return left_val * right_val
#         elif node.data == '/':
#             return left_val / right_val


# ................Source Code: Expression Tree..............
# Let's add this method to our existing codes and see the result.
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
    
    # def evaluate(self, node):
    #     if not node:
    #         return 0

    #     # if left and right children are None, then it's a leaf node
    #     # we assume it's an operand and return its integer value
    #     if not node.left and not node.right:
    #         return int(node.data)

    #     # evaluate left subtree
    #     left_val = self.evaluate(node.left)
    #     # evaluate right subtree
    #     right_val = self.evaluate(node.right)

    #     # check which operator to apply and return the result
    #     if node.data == '+':
    #         return left_val + right_val
    #     elif node.data == '-':
    #         return left_val - right_val
    #     elif node.data == '*':
    #         return left_val * right_val
    #     elif node.data == '/':
    #         return left_val / right_val
        

# ................Expression Tree: Optimizing the Code...............
# Upon carefully observing the logic behind each of the methods, we have basically applied inorder traversal in both cases.

# This is not how a good piece of code should be so let's define a method inorder_and _evaluate() to take care of both processes.

# We change nothing to the logic behind each of them but just combine them.

    def inorder_and_evaluate(self, node):
        if not node:
            return "", 0

        # if left and right children are None, then it's a leaf node
        # we assume it's an operand and return its value
        if not node.left and not node.right:
            return str(node.data), int(node.data)

        # evaluate and traverse left subtree
        left_expr, left_val = self.inorder_and_evaluate(node.left)
        # Evaluate and traverse right subtree
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
root_node = BinaryTreeNode("-")
node1 = BinaryTreeNode("/")
node2 = BinaryTreeNode("+")
node3 = BinaryTreeNode("*")
node4 = BinaryTreeNode("+")
node5 = BinaryTreeNode("*")
node6 = BinaryTreeNode("6")
node7 = BinaryTreeNode("+")
node8 = BinaryTreeNode("3")
node9 = BinaryTreeNode("-")
node10 = BinaryTreeNode("2")
node11 = BinaryTreeNode("3")
node12 = BinaryTreeNode("-")
node13 = BinaryTreeNode("3")
node14 = BinaryTreeNode("1")
node15 = BinaryTreeNode("9")
node16 = BinaryTreeNode("5")
node17 = BinaryTreeNode("7")
node18 = BinaryTreeNode("4")

# linking nodes
root_node.add_left_child(node1)
root_node.add_right_child(node2)

node1.add_left_child(node3)
node1.add_right_child(node4)

node2.add_left_child(node5)
node2.add_right_child(node6)

node3.add_left_child(node7)
node3.add_right_child(node8)

node4.add_left_child(node9)
node4.add_right_child(node10)

node5.add_left_child(node11)
node5.add_right_child(node12)

node7.add_left_child(node13)
node7.add_right_child(node14)

node9.add_left_child(node15)
node9.add_right_child(node16)

node12.add_left_child(node17)
node12.add_right_child(node18)

# creating binary tree
tree = BinaryTree(root_node)

print(tree.inorder_traversal(tree.root))
print(tree.evaluate(tree.root))

# Output
    # ['3', '+', '1', '*', '3', '/', '9', '-', '5', '+', '2', '-', '3', '*', '7', '-', '4', '+', '6']
    # = (-13.0)

#..................Why Optimize a Traversal Code?................
# Traversals are fundamental operations for working with trees, and they often serve as the basis for more complex operations. Performing any operations on a tree requires traversals of some sort.

# While it's possible to write separate methods for traversal and for the specific operation you're interested in, this can lead to redundant code, especially when the logic for the two tasks is similar.

# In scenarios like the ones we've discussed, it's more efficient to integrate the traversal logic directly into the operation you're performing. This reduces the lines of code and can make the overall algorithm more streamlined and efficient.

# By combining traversal and operation into a single method, you can optimize both the code structure and the computational performance.