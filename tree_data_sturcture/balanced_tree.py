'''
~ Balanced Trees
In the previous chapter, we examined how the order of insertion impacts the structures of trees.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.1.png

Both trees follow the rules of a BST, but the one on the bottom looks a bit unbalanced. Using trees with such a structure can severely affect the performance of our code.

For example, let's try to add 50 to both trees.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.2.png

As you can see, the tree on the bottom takes four steps to find a place to insert 50, whereas the one on the top takes only one step.

The primary distinction between these two trees lies in how their nodes are distributed across each level:
    * The tree on the bottom is expanding downwards.
    * But the tree on the top seems to be filling each level before moving to the next.

In data structures, this filling of a level before moving to the next is called balance, and the trees that satisfy this property are called balanced trees.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.3.png

Balanced trees are crucial for maintaining efficient operations in data structures, as they ensure that the height of the tree remains logarithmic relative to the number of nodes. This balance allows for faster search, insertion, and deletion operations compared to unbalanced trees, which can degrade to linear time complexity in the worst case.

Balancing a tree is key to optimizing the performance of search trees. So, we will learn about the three main states of balance next.

~ States of Balance in a Tree
There are three main states of balance in a tree. They are:
    * Perfect Balance
    * Good-Enough Balance
    * Unbalanced
    
Let's go through each of them.

~ Perfect Balance
A tree is said to be perfectly balanced when all its levels are completely filled, except possibly for the last level, which is filled from left to right. In a perfectly balanced tree, every node has two children, and the height of the tree is minimized.

A binary tree exhibits perfect balance if it is a perfect binary tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.4.png

Here, both the left and right subtrees of every node are at the same height and depth.

Although achieving perfect balance is ideal, it is rarely possible as it requires a specific number of nodes to fill every level completely.

For example, while trees with 1, 3, or 7 nodes can be perfectly balanced, those with 2, 4, 5, or 6 nodes cannot, due to partially filled bottom levels.

~ Good-Enough Balance
A tree is considered to have good-enough balance when the height of the left and right subtrees of every node differ by at most one. This means that the tree is not perfectly balanced, but it is still reasonably balanced, allowing for efficient operations.

A tree exhibits good-enough balance if the left and right subtrees of every node are of similar height and depth.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.5.png

Here, every level of the tree must be filled except for the bottom level.

In most cases of binary trees, this is the best balance we can achieve.

~ Unbalanced
A tree is considered unbalanced when the height of the left and right subtrees of any node differ by more than one. This means that one subtree is significantly deeper than the other, leading to inefficient operations.
An unbalanced tree is one where the left and right subtrees of any node are not of similar height and depth.

Finally, we have an unbalanced state where there is a considerable difference between the heights and/or depths of the left and right subtree of a node.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.6.png

Binary search trees in this state suffer from various levels of performance loss, depending on the degree of imbalance.

~ Height Balanced Trees
A tree is balanced if the difference in height or depth between any two leaf nodes does not exceed a certain value. This value is also known as the balanced factor.

The trees whose balance factor is defined in terms of height are called height balanced trees.

For height balanced trees,

    Balance Factor (BF) = Height of Left Subtree - Height of Right Subtree

NOTE: If a subtree doesn't exist, it's height is considered to be -1.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.7.png

NOTE: Balanced trees are not defined solely by heights, which we will learn in the coming chapters.

We know that the time taken for tree operations depends on its height.

Balanced binary trees ensure that the tree has the minimum possible height for given nodes. Thus, they minimize the time complexity.

That's why we prefer balanced trees, which ensure that our tree doesn't become unmanageably tall and keep our operations running smoothly.

~ Why Balance Trees?
Balancing a tree guarantees two primary benefits:
    * Predictable Performance: With a balanced tree, our operations run at a consistent and fast speed.
    * Space-Efficient: We don't waste memory due to excessive depth.

This means that basic operations on our balanced tree take a predictable amount of time, usually denoted as O(log n), where n is the number of nodes.

Now, let's discuss the common types of imbalances in structure that occur with trees.

~ Types of Imbalances in a Tree
In a tree, an imbalance occurs when one side of the tree is significantly taller than the other.

We are likely to encounter four types of imbalances:

1. Left-Left (LL) Imbalance
In LL imbalance, the left child of the left subtree of a node has a height greater than its right child.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.8.png

The imbalance can be observed at node 30, where its left child (node 20) has a left child (node 10) of height 1 whereas its own right child (node 35) has a height 0, making it a Left-Left imbalance.

2. Right-Right (RR) Imbalance
In RR imbalance, the right child of the right subtree of a node has a height greater than the left child of the subtree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.9.png

The imbalance is at node 10, where its right child (node 20) has a right child (node 30) of height 1 whereas its own left child (node 5) is of height 0, making it a Right-Right imbalance.

3. Left-Right (LR) Imbalance
The right child of the left subtree of a node is at a height greater than the left child of the subtree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.10.png

The imbalance can be observed at node 30. While it has a left child (node 10), this left child has a right child (node 20) of height 1.

On the other hand, the right child of the root node 30 (node 35) has a height 0, making it a Left-Right imbalance.

4. Right-Left (RL) Imbalance
The left child of the right subtree of a node is at a height greater than the right child of the subtree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.11.png

The imbalance can be observed at node 10. While it has a right child (node 30), this right child has a left child (node 20) of height 1.
On the other hand, the left child of the root node 10 (node 5)  has a height 0, making it a Right-Left imbalance.

Based on the imbalance of a given tree, it requires a balancing procedure called rotation to restore the balance, which we will discuss next.

~ How to Balance Trees
While we can prevent the occurrence of an unbalanced tree by carefully choosing the order of insertion, it's very impractical to do so.

So, we need a balancing procedure to convert a given unbalanced tree into a balanced one.

This is called rotation.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.12.png

Different scenarios demand different types of rotations. Before discussing them in detail, let's first discuss the primary concept of rotation.

~ What is Rotation?
Rotation is a process that changes the structure of a tree without affecting its in-order traversal. It involves moving nodes around to restore balance.

~ The Concept of Rotation
In simple terms, tree rotation is a process where you adjust a tree's structure by moving one node up and another down.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.13.png

This method is mainly used to reshape the tree, particularly to shorten its height. It does this by lowering smaller subtrees and raising larger ones.

With this out of the way, let's discuss how we can rectify the imbalances we discussed earlier using rotations.

~ Single Rotations
Single rotations involve rotating a single node only once.

The two single rotation operations are:
    * Right Rotation
    * Left Rotation

~ Right Rotation
Right rotations are used to solve LL imbalance.

The general process for right rotation on node y is:
    * The left child of the current node is promoted to become the new parent.
    * The original node (previous parent) is demoted to become the right child of the new parent.
    * The subtree that was originally to the right of the left child (before promotion) is now reattached as the left subtree of the demoted original node.
    * The subtree that was originally to the left of the new node retains its position.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.14.png

If we examine the right rotation process, we can see that only three nodes are really affected.

Here, before rotation,
    * y is the node with imbalance
    * x is the left child of y
    * z is the right child of x

After rotation,
    * x is the parent of y
    * y is the right child of x
    * z is the left child of y

Example: Right Rotation
Let's understand the basic concept using the simplest unbalanced tree with LL imbalance.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.15.png

Since imbalance was observed in 30, we rotate right on 30.

As per the steps listed above, this means:
    * 20 (left child) becomes the new parent.
    * 30 (previous parent) becomes the right child of 20.
    * 10 (left child of the previous left child) remains unchanged.

NOTE: As 20 previously had no right subtree, we ended our rotation.

This gives us a balanced tree as:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.16.png

Now, if we try to apply this same logic to the unbalanced tree we used earlier, we get the following:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.17.png

~ Left Rotation
Left rotations are used to resolve RR imbalance.

In a left rotation of a binary tree:
    * The right child of the current node is promoted to become the new parent.
    * The original node (previous parent) is demoted to become the left child of the new parent.
    * The subtree that was originally to the left of the right child (before promotion) is now reattached as the right subtree of the demoted original node.
    * The right children of the promoted node are left as they are.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.18.png

Like in right rotation, only three nodes get affected in the left rotation as well.

Here, before rotation:
    * x is the node with imbalance
    * y is the right child of x
    * z is the left child of y

After rotation:
    * y is the parent of x
    * x is the left child of y
    * z is the right child of x

Example: Left Rotation
Like before, let's first try solving the simplest occurrence of an RR imbalance:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.19.png

Since the imbalance was observed in 10, we left rotate on 10, where:
    * 20 (right child) becomes the new parent.
    * 10 (previous parent) becomes the left child of 20.
    * 30 (right child of the previous right child) remains unchanged.

NOTE: As 20 previously had no left subtree, we end our rotation.

This gives us a tree like this:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.20.png

Like before, let's try balancing the tree we previously introduced in the section on RR imbalance.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.21.png

~ Double Rotations
Single rotations can balance LL and RR imbalances. However, they cannot resolve LR and RL imbalances.

To resolve them, we can cascade two rotations to provide broader rebalancing within a tree. Such rotations are called double rotations.

There are two types of double rotations:
    * Left-Right Rotation (LR rotation)
    * Right-Left Rotation (RL rotation)

~ Left-Right Rotation
Left-Right rotation is used to resolve LR imbalances.

It basically consists of two steps:
    * Left rotate on the left child of the imbalanced node.
    * Right rotate on the parent node.

So if we consider the example
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.22.png

We first perform a left rotate on the left child (10).
    * The right child (20) is promoted to become the new parent.
    * The original node (10) is demoted to become the left child of the new parent.

This will give us the following tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.23.png

Now, this is basically an LL imbalance. So, we use right rotation on the parent node to balance the tree.
    * The left child (20) of the current node is promoted to become the new parent.
    * The original node (30) is demoted to become the right child of the new parent.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.24.png

Now, let's try balancing the tree we previously introduced in the section on LR imbalance.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.25.png

~ Right-Left Rotation
Right-Left rotation is used to resolve RL imbalances.

It also consists of two steps:
    * Right rotate on the right child of the imbalanced node.
    * Left rotate on the parent node.

Let's consider the following example:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.26.png

We first perform a right rotate on the right child (30).
    * The left child (20) of the current node is promoted to become the new parent.
    * The original node (30) is demoted to become the right child of the new parent.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.27.png

Now, this is basically an RR imbalance. So, we use left rotation on the parent node to balance the tree.
    * The right child (20) of the current node is promoted to become the new parent.
    * The original node (10) is demoted to become the left child of the new parent.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.28.png

Now, let's try balancing the tree we previously introduced in the section on RL imbalance.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.29.png

Now that we know the concepts of rotations, let's try to implement them in Python.
'''
'''
~ Implementation of Rotation
We studied earlier that there are four forms of rotations.

However, the good thing about object-oriented codes is that they are reusable and save a lot of time.

Since RL rotations and LR rotations are just single rotations cascaded together, we can just code the left and right rotations and use them in the needed order (left-right or right-left) to achieve double rotations.

So, let's start by learning how to implement right rotation.

~ Thought Process: Right Rotation
If we examine the right rotation process, we can see that only three nodes are really affected.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.30.png
Here, before rotation:
    * y is the node with imbalance
    * x is the left child of y
    * z is the right child of x
After rotation:
    * x is the parent of y
    * y is the right child of x
    * z is the left child of y

So, these are the only relations we need to modify to implement right rotation in Python; every other parent-child relation and order remains the same.

Now, let's implement right rotation in Python:

1. Define the method.

        def rotate_right(self, y):
    
We begin by defining our rotate_right() method, which takes a single argument y (the node to be pivoted at).

2. Store the relationships from the pivot node.

        x = y.left
        z = x.right

Store the left child of y in x and the right child of x in z.

NOTE: We have identified the key nodes involved in the rotation: y (the node to be rotated) and its left child x.
3. Perform Rotation.

        x.right = y
        y.left = z

Here, we rearrange the links to perform the right rotation.
    * The left child of y becomes the new root (x),
    * The right child of x becomes the left child of y.

4. Return the New Root.

        return x

We now return the new root (x) of the subtree.
'''

# Source Code: Right Rotation
def rotate_right(self, y):
    x = y.left
    z = x.right

    # Perform rotation
    x.right = y
    y.left = z

    # Return new root
    return x

'''
Note: The complete implementation of rotations will be seen in AVL Trees.
'''

'''
~ Thought Process: Left Rotation
Like in right rotation, only three nodes get affected in left rotation as well.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.31.png

Here, before rotation:
    * x is the node with imbalance
    * y is the right child of x
    * z is the left child of y
After rotation:
    * y is the parent of x
    * x is the left child of y
    * z is the right child of x

So, we only need to change the relationships listed above to implement left rotation in Python; everything else stays the same.

Thought Process: Left Rotation
We achieve left rotation in a similar way to right rotation.

It consists of the following steps.

1. Define the Method

        def rotate_left(self, x):
We begin by defining our rotate_left() method, which takes a single argument x, which is the node to be pivoted.

2. Store the relationships from the pivot node.

        y = x.right
        z = y.left

Store the right child of x in y and the left child of y in z.

NOTE: We have identified the key nodes involved in the rotation: x (the node to be rotated) and its right child y.

3. Performing Rotations

        y.left = x
        x.right = z

Here, we rearrange the links to perform the right rotation.

The right child of x becomes the new root (y),
The left child of x becomes the right child of y.
4. Return the New Root

        # Return new root
        return y
Finally, return the new root y.
'''

# Source Code: Left Rotation
def rotate_left(self, x):
    y = x.right
    z = y.left

    # Perform rotation
    y.left = x
    x.right = z

    # Return new root
    return y

'''NOTE: The complete implementation of rotations will be seen in AVL Trees.
'''

'''
~ When to Use Rotations?
Rotation shouldn't be used haphazardly, as overusing rotations can defeat their purpose. Let's consider the following example.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-18.1.32.png

In this example, we can see that the depth of the tree has actually increased, which is not what we want.

So, you should only use rotations to restore balance to your tree in accordance with the type of imbalance detected.

When is a Tree Balanced?
So, we have established that rotations should only be used when an imbalance is detected.

This statement, however, raises the question, "When is a tree actually imbalanced?" Or, to be more specific, "What is a balanced tree?"

In data structures, we can't come up with a universal definition for balanced trees like we did with binary trees.

Different forms of trees define balance uniquely, the most prominent being height-balanced trees.

A height balanced tree is balanced if it satisfies a certain criteria known as the balance factor (BF).

In this lesson, we defined balance in terms of height. Hence, the balanced trees we obtained in this lesson are height balanced trees.

Similarly, other kinds of balanced trees satisfy different balance criteria.

However, they all aim to achieve one common goal: ensuring O(log(n)) time complexity for most of the operations.

Let's start learning about balanced trees with one of the most popular variants of a height balanced tree called AVL trees.
'''