#.................Introduction to Trees...................
# A tree is a non-linear data structure that represents relationships and connections among various elements, facilitating easy navigation and search.

# The primary purpose of a tree is efficient data organization.

            #         1
            #         /\
            #        /  \------Edge
            #       /    \
            #      2      3----Node
            #     /\
            #    /  \
            #   /    \
            #  4      5

# Here,
    # *the circles are nodes
    # *the lines are edges

# In a tree, nodes are the individual elements, and edges connect these nodes.

#.........Real life Analogy: E-commerce Platform............

                        # Products
                            # |
            # |                                 |
    # Electronics                           Clothing
   # |             |                    |              |
# Mobiles       Laptops               Men's          Women's
                                    #   |              |
                                    # Shirts         Dresses

# Here, we have used a tree structure to organize products hierarchically for an e-commerce platform.

# Nodes represent product categories and subcategories, while edges show how they are connected or related to the platform.

# This streamlines navigation and improves data management.

#....................Why Trees?........................
# Let's take a practical example to understand why trees are used.
# In a file system, a directory can have multiple sub-directories. Each of these sub-directories can further contain additional directories and files.
# Suppose our My Documents directory contains three sub-directories:
    # Music
    # Pictures
    # Work
# Inside the Music directory, we have two files.
    # M1
    # M2
# Inside the Pictures directory, we have two files.
    # P1
    # P2
# And our Work directory is empty.

#.............Using List to Store Data..............
# Let's try to store this information using a list.
    # [Music| M1| M2| Pictures| P1| P2| Work]

# This list provides the names of all directories and files.
# However, it doesn't give information on how they are structured within My Documents.

#.............Using Tree to Store Data................
# Let's use a tree to represent this data.
                    # MyDocuments
                        # |
        # |               |                     |
      # Music         Pictures                 Work
    # |      |        |       |
    # M1     M2       P1      P2

# This tree clearly shows the contents of My Documents.

# On top of that, it also indicates which files/directories belong to which parent directory.


#...........Relationships in a Tree...............
# The tree data structure is inspired by family trees, which use terms like parent, child, siblings, ancestors, and descendants to describe relationships.

# So, relationships in trees are hierarchical, with elements above, below, or at the same level as others.
# The relationships in a tree are:

# 1. Parent
# The connected node directly above the current node in the hierarchy is known as its parent node.

# 2. Child
# The connected nodes directly below a particular node are its child nodes.

# 3. Siblings
# Sibling nodes in a tree share the same parent node. They are at the same level in the hierarchy.

#.................Anatomy of a Tree....................
# Now, let's look at the structure of a tree.

                            # Root
                            # /|\
                           # / | \
                          # /  |  \
                         # /   |   \
                    # Leaf    Leaf  Node
                                    # /|\
                                   # / | \
                                  # /  |  \
                                 # /   |   \
                              # Leaf  Leaf  Leaf

# Here,
#     *The top-most node with no parent is called the root node.
#     *Nodes with no children are called leaf nodes.

# A tree can have only one root node.

# NOTE: In DSA, it's also common to refer to the leaf nodes as external nodes and all the other nodes as internal nodes.

# Now that we know the terminology, we can study the properties of a node.

#....................Depth of a Node...................
# The depth of a node in a tree refers to the path length from the root node to that particular node.
# Depth is measured using the number of edges required to reach a particular node from the root node.
# The depth of the root node is zero since it does not have any ancestors.


            #         A d=0
            #         /\
            #        /  \
            #       /    \
            #      B d=1  C d=1
            #     /\      /
            #    /  \    /
            #   /    \  /
            #  D      E F d=2
           # d=2     d=2 \
            #             \
            #              \
            #               G d=3

# In our tree example:
    # Node A is at depth 0 because it is the root node.
    # Nodes B and C are at depth 1 because they are one edge away from the root.
    # Nodes D, E, and F are at depth 2 because they are two edges below the root.
    # Node G is at depth 3 because it is three edges below the root.

#...............Height of a Node................
# The height of a node in a tree refers to the length of the longest path from that node to a descendant leaf node.
# Height is measured using the number of edges encountered when moving from the node to the deepest child node.
# The height of a leaf node is zero since it has no children.
            
            #         A h=3
            #         /\
            #        /  \
            #       /    \
            #      B h=1  C h=2
            #     /\      /
            #    /  \    /
            #   /    \  /
            #  D      E F h=1
           # h=0     h=0 \
            #             \
            #              \
            #               G h=0

# In our tree example:

    # *Node A is at height 3 because the longest path from A to a leaf node is three edges.
    # *Node C is at height 2 because the longest path from C to a leaf node is two edges.
    # *Nodes B and F are at height 1 since the longest path from them to a leaf node is one edge.
    # *Nodes D, E, and G are at height 0 because they are leaf nodes.

#.................Height of a Tree....................
# Now that we are familiar with calculating the height and depth of any node of a tree, understanding the height of the entire tree should be relatively easy.

# Let's look at the information we have gathered so far in a combined image.

            #         A h=3 d=0
            #         /\
            #        /  \
            #       /    \
            #  d=1 B h=1  C h=2, d=1
            #     /\      /
            #    /  \    /
            #   /    \  /
            #  D      E F h=1, d=2
           # h=0     h=0 \
           # d=2     d=2  \
            #              \
            #               G h=0, d=3

# The height of the entire tree is simply the height of the root node or the depth of the deepest node.

# In this case, the height and depth of our tree is 3.

#................Degree of a Node...............
# The degree of a node is the number of children that the node has.
# It's an integer value that gives some insight into the structure of the tree

            #         A deg=2
            #         /\
            #        /  \
            #       /    \
            #deg=3 B      C degree=1
            #     /|\       /
            #    / | \     /
            #   /  |  \   /
            #  D   |   F  G degree=1
           #deg=0  |   deg=0 \
            #      E          \
            #   deg=0          \
                            # H degree=0

# In our tree:

    # Node A has a degree of 2 since it has two children (B and C).
    # Node B also has a degree of 3 since it has three children (D, E, and F).
    # Node C has a degree of 1 since it has one child (G).
    # Node G has a degree of 1 since it has one child (H).
    # Node D, Node E, Node F, and Node H have a degree of 0 since they do not have any children (leaf nodes).

#.............Degree of a Tree
# The degree of a tree is the maximum degree of any node in the tree.

            #         A deg=2
            #         /\
            #        /  \
            #       /    \
            #deg=3 B      C degree=1
            #     /|\       /
            #    / | \     /
            #   /  |  \   /
            #  D   |   F  G degree=1
           #deg=0  |   deg=0 \
            #      E          \
            #   deg=0          \
                            # H degree=0

# In our example, the degree of the tree is 3 since it is the highest value of degree for any node (B).


#.................Level of a Tree
# In a tree data structure, the nodes are arranged at different levels.
    # The root node is at Level 0.
    # The nodes directly connected to the root are called Level 1 nodes.
    # Each Level 1 node can have its own set of child nodes, which become Level 2 nodes.

# As we go down the tree, each set of child nodes from a particular level increases the level number until we reach the deepest nodes at the lowest level.

            #         A         Level=0
            #         /\
            #        /  \
            #       /    \
            #      B      C     Level=1
            #     /\      /
            #    /  \    /
            #   /    \  /
            #  D      E F       Level=2
            #            \
            #             \
            #              \
            #               G   Level=3

# NOTE: The maximum number of levels in a tree depends upon the height of the tree.


#.................Subtrees.................
# A subtree is a portion of a tree that is derived from a specific node. This node is known as the subtree root.

# The subtree retains the hierarchical relationships and structure of the original tree.

# Suppose we have a tree like this:


            #         A         
            #         /\
            #        /  \
            #       /    \
            #      B      C     
            #     /\      /
            #    /  \    /
            #   /    \  /
            #  D      E F       
            #            \
            #             \
            #              \
            #               G   


# In our example tree, we can obtain the following sets of subtrees:

# 1. Subtree rooted at node B: B, D, and E.
            #      B           
            #     /\      
            #    /  \    
            #   /    \  
            #  D      E

# 2. Subtree rooted at node C: C, F, and G.
            #      C     
            #     /
            #    /
            #   /
            #  F       
            #  \
            #   \
            #    \
            #     G

# 3. Subtree rooted at node F: F and G.

            #  F       
            #  \
            #   \
            #    \
            #     G

#.....................Forest..................
# In data structures, a forest is a set of non-interacting trees.

# We can create a forest by removing certain nodes from a tree. Let's consider an example.

                            #  A
                            # /|\
                           # / | \
                          # /  |  \
                         # /   |   \
                        # B    C    D

# When we remove the root node (A), each of its child nodes (B, C, and D) becomes a separate tree.

# So, our forest will look like this:

            #   B               D
            #           C

# Each of B, C, and D forms its own separate tree, which together makes up a forest.

# By changing the node we remove, we can create different sets of forests from the same tree.

# Let's observe this by removing node C from our original tree.

                            #  A            C
                            # / \
                           # /   \
                          # /     \
                         # /       \
                        # B         D

# We now have two trees - one rooted at A with children B and D, and the other being node C itself.

#...............Linked Structure of Trees.....................
# Until now, we have treated trees as drawings with circles (nodes) and lines (edges) connecting them. These drawings help us understand the concept, but computers don't see them this way.

# In computers, they're built using specific data formats like lists, creating a special structure that sets them apart from other data structures.

# This is known as the linked structure of trees.
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.3.1.png

# Here, each node is allocated a block of memory which stores the following information:

#     *The data element.
#     *Reference to the parent node.
#     *A single container of references to its children as one node can have multiple children.
# The container can be set up using other concrete data types like lists.

# If you don't understand everything on this page, that's fine. Everything will make sense during the actual implementation.

#..................Thought Process: Implementation of Trees
# There are three steps involved in implementing a tree.

# 1. Create a class to handle nodes.
# A node contains:
#     *The value of the node.
#     *Information of children derived from that node.

# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.children = []

# Here, we've created a TreeNode class to manage single node-related operations.
# Within the initializer method, we store its data and maintain a list of its child node references.

# 2. Add a method to add children to a node.
# Now that we can create a node let's define a method to add children to it.

# def add_child(self, child):
#     self.children.append(child)
# The add_child method adds a child to a Node in a tree.

# 3. Create a class to handle nodes in a tree.

# class Tree:
#     def __init__(self, root = None):
#         self.root = root

# Here, we have created a class Tree that will store information of all the nodes in a tree.

# .............Combining the Classes
# Merging the code from the two classes, we get a skeletal program to create and manage a tree data structure.

            # class TreeNode:
            #     def __init__(self, data):
            #         self.data = data
            #         self.children = []

            #     def add_child(self, child):
            #         self.children.append(child)

            # class Tree:
            #     def __init__(self, root = None):
            #         self.root = root

# We will use this code as a template and add every method we define hereafter within this skeletal code.

# ................Creating Trees..................
# Now that we have the basics ready, we can create a tree.
# Let's take the following tree as an example.:
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.3.2.png

# As you already know by now, a tree data structure comprises two main components:
#     *Data node
#     *Relationship between the nodes

# Thus, we break down the creation process into two halves:
# 1. Adding Nodes
# 2. Defining Relationships

# ............Creating Trees: Add Nodes
# Now, let's use the code from the previous page to create the following tree.
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.3.3.png

# First, let's create our root node:

            # root = TreeNode("Book")

# Now, let's create the child nodes of the root node.

            # child1 = TreeNode(1)
            # child2 = TreeNode(2)
            # child3 = TreeNode(3)

# Now, let's create all the leaf nodes.

            # child1_1 = TreeNode(1.1)
            # child1_2 = TreeNode(1.2)
            # child1_3 = TreeNode(1.3)
            # child1_4 = TreeNode(1.4)
            # child2_1 = TreeNode(2.1)
            # child3_1 = TreeNode(3.1)
            # child3_2 = TreeNode(3.2)
            # child3_3 = TreeNode(3.3)

# We have now successfully created all the nodes of the tree.

# However, these nodes are currently nothing more than individual instances of the TreeNode class with no relationships.

# Thus, we will define these relationships next.

#.............Creating Trees: Define Relationships...........
# We'll now define hierarchies starting with the root.

# Our root node has three children.
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.3.4.png

# Let's add this relationship using the add_child() method.
            # root.add_child(child1)
            # root.add_child(child2)
            # root.add_child(child3)

#..........Defining Relationships of Leaf Nodes........
    # i. Children of child1
# add four children to the child1 node

            # child1.add_child(child1_1)
            # child1.add_child(child1_2)
            # child1.add_child(child1_3)
            # child1.add_child(child1_4)

    # ii. Children of child2
# add a child of child2 node
            # child2.add_child(child2_1)

    # iii. Children of child3
# add three children to the child3 node
            # child3.add_child(child3_1)
            # child3.add_child(child3_2)
            # child3.add_child(child3_3)

#...............Creating the Tree.............
# Now that we have created all the nodes and defined the hierarchy, we can finally create our tree.

            # general_tree = Tree(root)

# Next, we will put all these codes together to create a fully functional tree.

#.............Source Code: Implementation of Trees............
# Now, let's combine everything we've done so far into a full-fledged executable program.

# a class to create and add nodes
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        print(f'Node {self.data} was created')

    def add_child(self, child):
        self.children.append(child)
        print(f'Node {child.data} was added as child to Node {self.data}')

# a class to create tree and perform tree operations
class Tree:
    def __init__(self, root=None):
        self.root = root
        print("A tree was created")

# create the root node
root = TreeNode("Book")

# create children of root
child1 = TreeNode(1)
child2 = TreeNode(2)
child3 = TreeNode(3)

# create leaf nodes
child1_1 = TreeNode(1.1)
child1_2 = TreeNode(1.2)
child1_3 = TreeNode(1.3)
child1_4 = TreeNode(1.4)
child2_1 = TreeNode(2.1)
child3_1 = TreeNode(3.1)
child3_2 = TreeNode(3.2)
child3_3 = TreeNode(3.3)

# describe relationships between the nodes
# and add children to the root node
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

# create the tree
general_tree = Tree(root)

# OUTPUT =[
    # Node Book was created
    # Node 1 was created
    # Node 2 was created
    # Node 3 was created
    # Node 1.1 was created
    # Node 1.2 was created
    # Node 1.3 was created
    # Node 1.4 was created
    # Node 2.1 was created
    # Node 3.1 was created
    # Node 3.2 was created
    # Node 3.3 was created
    # Node 1 was added as child to Node Book
    # Node 2 was added as child to Node Book
    # Node 3 was added as child to Node Book
    # Node 1.1 was added as child to Node 1
    # Node 1.2 was added as child to Node 1
    # Node 1.3 was added as child to Node 1
    # Node 1.4 was added as child to Node 1
    # Node 2.1 was added as child to Node 2
    # Node 3.1 was added as child to Node 3
    # Node 3.2 was added as child to Node 3
    # Node 3.3 was added as child to Node 3
    # A tree was created
# ]

# From this output, it's clear that our tree was created and the child nodes were added confirming that our code is correct but incomplete.

# To complete our code, we will need to incorporate methods for traversal like we did in previous data structures.

# Since non-linear data structures offer multiple traversal paths, let's first focus on performing basic operations on our tree.

# But before that, let's make sure you're comfortable with everything we've covered so far.