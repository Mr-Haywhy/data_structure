# Example: Calculating Disk Space
# Suppose we have a file system directory like this and we have to calculate the total memory occupied by this directory.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.22.png

# In order to calculate the space occupied by the MyDocuments folder, we first have to calculate the space occupied by all the subfolders.

# In order to calculate the space occupied by each subfolder, we have to calculate the space occupied by the files first.

# This is similar to visiting all the child nodes in a tree before visiting the parent node. Thus, we can use postorder traversal for this.

# ...........Calculate the Total Disk Space...........
# Write a program to calculate the total disk space occupied by MyDocuments in the given figure.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.23.png

# The TreeNode class has been modified to contain the size of leaf nodes.
# Define a method, calculate__disk_space(), which takes in a node as its only argument.
# Inside the method, use the concept of postorder traversal to calculate the disk space occupied by the entire directory.
# The size of each file is:

# M1: 20 GB
# M2: 10 GB
# P1: 30 GB
# P2: 20 GB
# Work: 10 GB
# Example
# Expected Output = 90 GB
# Note: The size of the files has been mentioned in the code outline itself.

# Replace ___ with your code

class TreeNode:
    def __init__(self, data, size=0):
        self.data = data
        self.size = size
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, root=None):
        self.root = root

    def calculate_disk_space(self, node, total=[]):
        # write your code here

        for child in node.children:
            self.calculate_disk_space(child, total)

        total.append(node.size)

        return sum(total)


# create the tree nodes (directories and files)
my_documents = TreeNode("MyDocuments")
music = TreeNode("Music")
pictures = TreeNode("Pictures")
work = TreeNode("Work", 10)  # Work is a file, so it has a size
m1 = TreeNode("M1", 20)  # M1 is a file, so it has a size
m2 = TreeNode("M2", 10)  # M2 is a file, so it has a size
p1 = TreeNode("P1", 30)  # P1 is a file, so it has a size
p2 = TreeNode("P2", 20)  # P2 is a file, so it has a size

# build the tree structure
music.add_child(m1)
music.add_child(m2)
pictures.add_child(p1)
pictures.add_child(p2)
my_documents.add_child(music)
my_documents.add_child(pictures)
my_documents.add_child(work)

# create the tree
tree = Tree(my_documents)

# calculate the total disk space
total_size = tree.calculate_disk_space(my_documents)
print(f"{total_size} GB")