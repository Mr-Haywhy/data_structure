# ...........Introduction to Binary Tree Traversal........
# You will be happy to know that the methods of traversals we discussed in general trees work with binary trees as well.

# As we have gone through them in detail in the previous chapter, we won't be discussing them here.

# We will only be discussing a variation of traversal specific to a binary tree called inorder traversal.

# But before we move on to inorder traversal, try and add the implementation of preorder and postorder traversals in our existing skeletal structure of binary tree.



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
       
        
    def preorder_traversal(self, node, traversal=[]):
        # write your code here
        if not node:
            return traversal

        traversal.append(node.data)
        if node.left: 
            self.preorder_traversal(node.left, traversal)
        if node.right: 
            self.preorder_traversal(node.right, traversal)

        return traversal
        
    def postorder_traversal(self, node, traversal=[]):
         # write your code here
        if not node:
            return traversal

        if node.left:
            self.postorder_traversal(node.left, traversal)
        if node.right:
            self.postorder_traversal(node.right, traversal)
        
        traversal.append(node.data)
        return traversal
         

# create child nodes
A = BinaryTreeNode("A")
B = BinaryTreeNode("B")
C = BinaryTreeNode("C")
D = BinaryTreeNode("D")
E = BinaryTreeNode("E")
F = BinaryTreeNode("F")

# define relationships
A.add_left_child(B)
A.add_right_child(C)
B.add_left_child(D)
B.add_right_child(E)
C.add_left_child(F)

# call the function
tree = BinaryTree(A)

print(f'Preorder Traversal: {tree.preorder_traversal(tree.root)}')
print(f'Postorder Traversal: {tree.postorder_traversal(tree.root)}')

# Output:
    # Preorder Traversal: ['A', 'B', 'D', 'E', 'C', 'F']
    # Postorder Traversal: ['D', 'E', 'B', 'F', 'C', 'A']