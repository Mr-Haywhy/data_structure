'''
~ Introduction
B-trees are an extended class of self-balancing trees like AVL and Red-Black Trees that maintain their balance of nodes. B-trees have two standout features:
    * B-trees are not binary trees. Thus, a node can have more than two children.
    * Each node stores values (called keys). A node in a B-tree can have more than one key.

Let's look at the following example:

tree_data_sturcture\Screenshot 2025-07-19 230031.png

As B-trees often have many children per node, they are commonly used in applications that process large volumes of data, such as databases and file systems.

Now, let's take a look at the structure of a B-tree.

~ Structure of a B-Tree
Let's look at an example of a B-tree:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.1.2.png

From the structure above, we can conclude that a B-tree has the following properties:
    * It can have multiple keys for a single node.
    * A single node can have more than two children.
    * All the leaf nodes must be at the same level.
    * Keys within nodes are always in sorted order.

The number of keys and the number of children are determined by the order of the B-tree, which we will discuss next.

~ Order of a B-Tree
The order of a tree is defined as the maximum number of children the tree can have.

Suppose the order of a B-tree is N. It means every node can have:
    * A maximum of N children.
    * A maximum of N - 1 keys.
    * A minimum of (N/2) - 1 keys (not counting the root node).

Let's take a B-tree of order N = 6. According to the properties of the B-tree, any node can have:
    * A maximum of (N - 1) = 6 - 1 = 5 keys.
    * A minimum of (N/2) - 1 = (6/2) - 1 = 2 keys.
    
Next, you'll take a couple of quizzes, and then learn about branching in B-trees and the key terms and concepts relevant to the topic.
'''