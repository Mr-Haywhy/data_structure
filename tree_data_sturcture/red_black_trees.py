'''
~ Introduction to Red Black Trees
Red-Black Trees are a category of self-balancing trees that utilize node colors to maintain balance.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.1.png

Visually, a Red-Black Tree looks like a Binary Search Tree (BST) with nodes colored either red or black.

These colors aren't arbitrary; they adhere to specific properties that ensure the tree's structure remains balanced.

Let's try analyzing each of these properties as well as their significance to imparting or restoring the balance of the tree.

~ Properties of Red Black Trees
Red-Black Trees (RBTs) are a type of self-balancing binary search tree with five key properties:

1. Leaf Property
Every leaf has invisible NIL node children, and is colored black. These NIL nodes signify the end of a path in the tree and help in maintaining balance.

2. Root Property
The root is always black.

A black root ensures that any path from the root to a leaf has at least one black node. By keeping the root black, it assists in maintaining the next crucial property related to red nodes.

3. Red Node Property
Red nodes can't have red children. This rule aids in avoiding long chains of consecutive red nodes, which could lead to an imbalance in the tree.

The absence of two consecutive red nodes results in consistent black height (number of black nodes from the root to a leaf).

4. Black Depth Property
Every path from root to NIL node has the same number of black nodes. This guarantees that no path is more than twice as long as any other, ensuring logarithmic height.

The above four properties must be satisfied at any given instance for a red-black tree to be balanced.

In case of insertion, however, one more property is added, which doesn't necessarily define balance but aids in the process.

5. New Insertions
New insertions are always red.
    * If inserting a red node doesn't violate any properties, no further action is required.
    * If it violates a property (like causing two consecutive red nodes), rotations and/or color changes can be executed to restore balance.

Let's see some examples of valid and invalid cases for red-black trees.

~ Example: Red Black Trees
A tree is a valid red-black tree if it satisfies all four properties we discussed previously. So, let's quickly go over some cases that constitute an invalid red-black tree.

Example I
Consider the following tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.2.png

This is invalid because the root is red. But the root of a red-black tree must always be black.

A valid version of this tree would have a black root.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.3.png

Example II
The following tree is not a valid red-black tree because there are consecutive red nodes.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.4.png

A valid version of this tree would have the red nodes colored black.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.5.png

Example III
This tree is not a valid red-black tree because there are 3 black nodes in Path 1 and only 2 black nodes in path 2.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.6.png

The black depth property states that any path from the root node to a leaf node must have the same number of black nodes.

A valid version of this tree would be something like this.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.7.png

With this introduction, let's move on to red-black tree operations.

~ Insertion in Red Black Trees
Like AVL trees, we can generalize inserting elements into a red-black tree into the following steps:
    1. Insert the element like you would in a BST.
    2. Mark the new insertion as red.
    3. Check if any of the properties of RBT are violated.
    4. Apply rotation and/or change color to restore the balance.

Let's first look at a basic case of insertion at the root.

~ Insert at Root
This is the most basic case, as Z is the first element to be inserted into the tree.

Since every new insertion has to be a red node, Z is initially red.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.8.png

Let's see if this new node violates the red-black tree property.

1. Leaf Property
Since Z has invisible black NIL leaves, the leaf property is satisfied.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.9.png

2. Root Property
This property specifies that the root node must be black. Since Z is a root node but red in color, it violates the root property.

To fix this, we simply change the color to black.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.10.png

3. Red Node Property and Black Depth Property
The red node property and black depth property are both satisfied.

Thus, the solution to this case is quite simple, as all we have to do is color Z black.

~ Cases of Insertion
If the insertion is into an existing red-black tree, we must consider the color of the uncle node.

An uncle in a tree is the sibling of your parent node. Depending on the status of the uncle node, we can have the following two cases:
    * The node has a red uncle.
    * The node has a black uncle.

~ Case 1: Node Has a Red Uncle
If the node has a red uncle, the grandparent must be black (red node property).
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.11.png

For this particular case, we don't need any rotation; we simply recolor Z's parents, grandparents and uncle.

Change the:
    * Color of the parent and the uncle node to black.
    * Color of the grandparent node to red.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.12.png

This satisfies the red black properties for the newly inserted node Z.

However, this might cause the grandparent node to violate a red-black property. Thus, we repeat this process for every grandparent node.

For example, if the tree above is a complete tree with node B as the root, then we cannot leave it red. So, we recolor it to black.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.13.png

This marks the end of balancing when the uncle is red.

Balancing becomes a little more complicated if the uncle is black.

Case 2: Node Has a Black Uncle
If the newly inserted node has a black uncle, we have four sub-cases:
    1. New node is the left child of the parent, and the parent is the left child of the grandparent.
    2. New node is the right child of the parent, and the parent is the right child of the grandparent.
    3. New node is the left child of the parent, and the parent is the right child of the grandparent.
    4. New node is the right child of the parent, and the parent is the left child of the grandparent.

The first two cases (left-left case and right-right case) share a common solution. Similarly, the next two cases (left-right case and right-left case) share a common solution.

~ Left-Left Case and Right-Right Case
Let's look at the two cases below:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.14.png

In both cases, the logic behind solving the problems is the same:
    * Rotate the grandparent of Z in the opposite direction.
    * Swap the colors of the original parent and grandparent of Z.

Let's clarify it further using the right-right case as an example.

~ Example: Right-Right Case
Consider the following right-right case:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.15.png

As Z is the right child of a right child with a black uncle, we rotate its grandparent B in the opposite direction i.e., left.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.16.png

After this, we simply swap the colors of both the original parent and grandparent.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.17.png

~ Left-Right Case and Right-Left Case
Let's look at following two cases:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.18.png

~ Example: Right-Left Case
Consider the following right-left case where the node Z has a black uncle.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.19.png

Here, Z is the left child. So, we simply rotate its parent A in the opposite direction, to the right.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.20.png

This rotation converts the Left-Right and Right-Left cases to Left-Left or Right-Right cases, respectively. We can then solve them using the methods we discussed previously.

With insertion completed, let's move on to deletion from a red-black tree.

~ Deletion From Red-Black Tree
Before deleting from a red-black tree, let's first examine deletion from a binary search tree.

There, we had three cases:
    * Case I : Deleting a leaf node
    * Case II: Deleting node with one child
    * Case III: Deleting node with two children

~ Case I: Deleting a Leaf Node
We simply delete a leaf node directly and do nothing more.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.21.png

~ Case II: Deleting Node with One Child
If the node has one child, then,
    * Replace the value of the node with its child node.
    * Remove the child node from its original position.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.22.png

Remember: The node actually being deleted is a leaf node and the internal node just gets replaced. This is important.

~ Case III: Deleting Node with Two Children
If the node has two children, then,
    * Replace the value of the node with the inorder successor.
    * Remove the inorder successor from its original position.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.23.png

NOTE: Like in the above example, we are deleting the original instance of the inorder successor after copying its value to the internal node that we originally wanted to delete.

The main thing to remember is that we directly delete a node only if that node is a leaf node.

In every other case, we replace the value of the node with its inorder successor. Then, we delete the original instance of the inorder successor i.e., the node to be actually deleted is the inorder successor.

Remember: We can't delete an internal node, we can only replace its value.

Keeping these things in mind, let's finally learn how to delete nodes from a red-black tree, starting with red nodes.

~ Deleting a Red Node
If the node to be deleted is red, we can simply delete it as we do in BST.

Deletion of a red node cannot violate any red-black property.
    1. Leaf Property: The leaf nodes are always black NIL nodes. So, deleting a red node will not violate them.
    2. Root Property: The root node is black. So, deleting a red node will not affect it.
    3. Red Node Property: Deleting a red node cannot violate red-node property.
    4. Black Depth Property: Again, deleting a red node cannot affect the count of black nodes.

So, for the deletion of a red node, simple BST deletion is sufficient.

Let's take a look at an example and attempt to delete node 30.

NOTE: Even though node 30 is black, the node that will actually get deleted is the leaf node 40, which is red. This is because we can't delete internal nodes. Hence, this operation is an actual case of deleting a red node.

~ Deleting a Black Node
Deleting a black node from an RBT will result in the violation of the black depth property.

So, the tree needs some fixing. So, what do we do?

We start off by replacing the deleted black node with a Double Black (DB) node.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.26.png

Let's clarify this with an example.
Let's try and delete 20 from the following tree:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.27.png

To delete 20, we replace 20 with its inorder successor, i.e., 30. Then, we delete the original instance of 30 (the black leaf node).

Since the original instance of 30 is a black node, we replace it with a double black node whose value is nil.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.28.png

So, our problem now will be finding a way to get rid of this double black node to get a valid solution.

However, let's first understand the basic concepts surrounding a double black node.

~ Double Black (DB) Node
When we count a node as double-black, it contributes twice to the black depth along that path.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.29.png

However, double-black isn't technically a valid color for a node. So, this problem needs to be addressed.

Marking a node as double-black precisely indicates where there's a deficit of black in the tree.

Without this marker, tracking this imbalance within the larger structure of the tree would be challenging. Think of it as a temporary marker for our reference.

Note: A double black designation can be transferred from a child node to its parent node.

If the parent is red, it will now be a black node.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.30.png

If the parent is black, it will now be a new double black node.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.31.png

However, we cannot transfer a double black from a parent to its child.

Let's look at some of the cases that arise when removing a double black node.

~ Case I: If the DB is a Root Node
If the DB is a root node, we simply replace the DB with a single black node.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.32.png

This will maintain the black depth property by decreasing the black length of the whole tree by 1.

~ Case II: If the DB has a Red Sibling
If the sibling is red,
    * Swap the color of the parent and sibling.
    * Rotate in the direction of the DB.

Suppose we have the following double black node:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.33.png

Since its sibling is red, we swap the color of the parent and sibling and rotate in the direction of DB.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.34.png

This new tree will be treated as a new DB problem and we will check for all cases again.

~ Case III: If DB Has Black Sibling With All Black Children
If a DB has a black sibling with all black children, we have two cases to consider.

Case I: The Parent is Red
If the parent of the DB is red, simply transfer one black to the parent and make the sibling red. For example,
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.35.png

Case II: The Parent is Black
If the parent is black, we transfer one black to the parent and make it double black. We then make the sibling red. For example,
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.36.png

But we see that the double black persists. This will be our new problem and requires additional cases to solve.

Luckily for us, the problem in the example has a DB node with a black sibling with all black children. So, this is the same case we were dealing with right now.

So, let's repeat the steps and transfer one black to the parent node and make the sibling red.

And since this parent node is the root, we can simply get rid of the double black.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.37.png

We may not always be this lucky. So, let's discuss additional cases to solve other sorts of imbalances.

~ Case IV: DB Has a Black Sibling Whose Far Child is Red
Consider a DB that has a black sibling whose far child is red like this.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.38.png

To balance such cases:
    * Swap the color of the parent and the sibling of DB.
    * Rotate the parent in the direction of DB.
    * Change the DB to a single black node.
    * Change the color of the red far-child to black.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.39.png

~ Case V: If DB Has a Black Sibling With a Black Far Child and Red Near Child
If the DB has a black sibling whose far child is black and the near child is red, we must apply the steps below to convert this problem to resemble Case IV:
    1. Swap the color of the sibling and its near child.
    2. Rotate the sibling towards the far child.
    3. Treat this as a new problem of Case IV.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.3.40.png

This marks the end of balanced trees.
'''