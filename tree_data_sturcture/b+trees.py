'''
~ Maximizing the Efficiency of B-Trees
B+ trees are a variation of B-trees. So, before looking at the actual structure of a B+ tree, we need to discuss two shortcomings of B-trees:
    * Difficulty in finding sequential data in a range.
    * Choosing the appropriate degree for the appropriate height and width.

We'll start with searching for sequential data within a range.

~ Problem 1: Finding Sequential Data in a Range
Consider searching for all values within a specific range, like finding all numbers from 2 to 5 in a B-tree.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.3.1.png

Navigating up and down a tree structure multiple times can introduce complexity when implemented in a program.

This requires frequent rearrangement of pointers, which is manageable if all the data resides in the primary memory. This is the case with Binary Search Trees (BST).

In B-trees, however, these traversals result in repeated memory or disk accesses. It's because only data from selected nodes is loaded into primary memory, with the rest being stored in the secondary memory.

These frequent memory accesses significantly increase latency (time taken to transfer all files from a disk to another) compared to the efficiency of sequentially scanning contiguous blocks in memory or on disk.

~ Solving the Latency Issue
So far, we've learned that searching for sequential keys in a B-tree is very time consuming.

A linked list could facilitate sequential searches. But it lacks the hierarchical advantages of trees, which optimize storage and retrieval through structured organization.

So, a clever solution would be to create a new structure combining the features of both data structures, i.e., creating a B+ tree.

Next, we'll look at the second disadvantage of B-trees.

~ Problem 2: Choosing the Appropriate Degree
Recall the true structure of B-trees:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.3.2.png

Here, every node stores the key and the associated data.

We know that in a B-tree:
    * A smaller degree will result in a taller B-tree, which is better for memory management.
    * A larger degree will result in a wider B-tree, which is better for reduced I/O complexity as disk transfers are reduced.

Based on these facts, let's see how we might maximize the efficiency of a B-tree.

~ Maximizing the Efficiency of B-Trees
We can improve the efficiency of B-trees if we could somehow add more keys to the same node without increasing the size it occupies.

We can do this by creating a vacant space in the nodes to hold more keys. But we also need to remove something else to maintain the node size.

Since we can't remove the keys, we need to remove the data.

However, blindly deleting the data from every node nullifies the concept of trees altogether, since trees are merely a tool for data organization.

So, we'll store data only at the leaf nodes.

This is the second foundational principle behind B+ trees.

~ B+ Trees
To deal with the inefficiencies we discussed in the previous lessons, we modify B-trees into B+ trees such that:
    * Only the leaf nodes have actual data.
    * The leaf nodes are connected by a linked list.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.3.3.png

In this case, if we search for five consecutive data starting from any key (say, 2), we can simply locate key 2 and use the linked list to access all data.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.3.4.png

NOTE: In B+ trees, each key in the internal nodes also appears in the leaf nodes. This results in a less complex tree structure and a faster sequential search.

Like in B-trees, from now on we will only deal with the keys and not the data for simplicity.

~ Order of a B+ Tree
The order of a B+ tree is denoted by m and is the maximum number of children that any node in the tree can have.

A B+ tree of order m must have:
    * At least ceil(m/2) children (except for the root).
    * At most m children.
    * At least ceil(m/2) - 1 keys.
    * At most m-1 keys.

Thus, a B+ tree of order 3 must have:
    * At least ceil(3/2) = 2 children (except for the root).
    * At most 3 children.
    * At least ceil(3/2) - 1 = 1 keys.
    * At most 3-1 = 2 keys.

The order of a B+ tree is a crucial parameter that affects the tree's height and, consequently, its performance, which we'll explore next.

~ Relationship Between Order and Performance
Like with order in B-trees, a larger m value in the B+ tree reduces the height of the tree, thus decreasing the number of disk accesses required for operations.

However, it may also lead to inefficient use of space, as each node may not be fully utilized.

For example, consider the B+ tree below of order 6. Here, each key can contain at least 6-1 = 5 keys.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.3.5.png

However, to satisfy the B+ tree structure, the left child only contains three keys and the right child only contains only four keys. This means that:
    * The left child still has room for two other keys less than 11.
    * The right child still has room for one other key greater than 11.

Therefore, choosing an appropriate value of m is thus important to strike a balance between space and time efficiency.

Next, you'll take a series of quizzes and then we'll move on to performing basic operations in a B+ tree.

~ Operations in B+ Trees
Introduction
This lesson will explore the following operations:
    * Insertion into a B+ tree.
    * Deletion from a B+ tree.

NOTE: Search in B+ trees is identical to search operations in BST and B-trees.

As usual, let's start with insertion.

~ Insertion Into a B+ Tree
Just like in B-trees, insertion into a B+ tree is a two-step process:
    * Insert into the tree.
    * Split the node in case of overflow.

There's only a small difference — after splitting a node from its median value, its right child will also contain the split median value.

Let's clarify this with an example.

Example: Insertion Into a B+ Tree
Consider the following tree of order 3, which only consists of a root node with keys 5 and 10:

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.1.png

Let's try adding key 15 to the tree.

Here's how our previous tree (of degree 3) will look after inserting key 15 into it:

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.2.png

As a node can contain a maximum of 3-1 = 2 keys, we have to split the node at its median value as we did with B-trees.

The only difference here is that we have a replica of the parent node in the leaf node as well.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.3.png
This is the only difference in handling overflows in a B+ tree; every other case is the same as that of B-trees.

~ Why Add Replicas After Splitting?
As you now know, we add a replica of the median key after splitting:

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.4.png

We keep this replica because
    * The replica in the parent acts as a key for searching.
    * The replica in the child maintains the linked structure and contains the data (or link to data).

~ Deletion in a B+ Tree
When deleting a key, we must be cautious of where the key appears and how its deletion affects the balance of the tree.

Based on these considerations we'll be studying three cases of deletion:
    * The key to be deleted is only present in the leaf node.
    * The key to be deleted is present in both internal and leaf nodes.
    * Deleting the key reduces the height of the tree.

We'll study each case separately and handle the underflow of each case.

~ Case I: The Key to Be Deleted is Present Only in the Leaf Node
If the key to be deleted is present only in the leaf node and not in the internal nodes, then we can simply delete it.

Here, we have two possible cases:
    1. The node containing the key to be deleted has more than the minimum number of keys.
    2. The node containing the key to be deleted has exactly the minimum number of keys to be deleted.

Case I(a): Node Has More Than Minimum Number of Keys
Suppose we want to delete key 45 from the given tree of order 3.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.5.png

Since we need at least one key in every node for a valid B+ tree of order 3, we simply go ahead and remove the key (45).

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.6.png

As you can see, the number of keys and children in the resulting tree are within the range defined by the order of tree (3).

Case I(b): The Node Has Exactly the Minimum Number of Keys
If the node has exactly the minimum number of keys required, we:
    * Delete the key.
    * Replace it with a key from the immediate sibling of the node.
    * Assign the median key from the sibling node as the parent.

Suppose we want to delete 15 from this tree.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.7.png

Let's see how to do this next.

Case I(b): The Node Has Exactly the Minimum Required Number of Keys
Here's how we can delete 15 from the previous tree:
    1. We delete 15.
    2. Then, we replace it with a key from its sibling (20).
    3. Finally, we assign the median key from its sibling (25) as its parent.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.8.png

Now, after reassigning the leaf pointers, our final tree is:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.9.png

~ Case II: The Key is Present in Both the Internal and Leaf Nodes
If the key to be deleted is present in both the internal and leaf nodes, then simply deleting the key from the leaf node is not enough. For this, we have to consider the following cases:
    * The leaf node has more than the minimum number of keys.
    * The leaf node has exactly the minimum required keys.
    * The internal node isn't the immediate parent of the leaf node.

Case II(a): The Leaf Node Has More Than the Minimum Number of Keys
If the node has more than the minimum number of keys, we follow the steps below:
    1. We first delete the key from the leaf node.
    2. Then, we follow it up by deleting its instance from the internal node.
    3. Finally, we fill the void with its inorder successor.

Let's demonstrate this in the next page by deleting 50 from this tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.10.png

Case II(a): The Leaf Node Has More Than the Minimum Number of Keys
Continuing from the previous example, we delete both instances of 50 and replace the key in the internal node with its inorder successor (60).

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.11.png

This will give us the following tree:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.12.png

Case II(b): The Leaf Node Has Exactly the Minimum Required Number of Keys
If the node has exactly the minimum number of keys, we
    * Delete the keys from both nodes.
    * Replace them with a key from the immediate sibling of the leaf node. You can take any sibling for this.

Let's demonstrate this by deleting 40 from the given tree:

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.13.png

In the previous example, we first delete both instances of 40 and fill the voids in the nodes with 35.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.14.png

NOTE: We can borrow a key from either of its sibling nodes so long as they have enough keys to borrow from. In our example, the right sibling had just the one key needed for a valid B+ tree.

This leaves us with a tree like this:

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.15.png

Case II(c): The Internal Node Isn't the Immediate Parent of the Leaf Node
Suppose we need to delete key 30 from the following tree:

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.16.png

If we were to delete 30 from this tree, then the void after deletion will not appear in two parent-child nodes but in grandparent-grandchild nodes.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.17.png

Next, we'll learn how to deal with this situation.

Here's the step-by-step procedure on how we can properly delete 30 from the previous tree:

1. Delete the key from the leaf node.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.18.png

2. Merge the void in the leaf node with its immediate sibling.
In our case, the sibling is 35.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.19.png
Let's continue the process on the next page.

3. Delete the grandparent node and fill this void with its inorder successor.
In this case, the inorder successor is 35.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.20.png

This should give us a tree like this:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.21.png

~ Case III: Deleting the Key Shrinks the Height of the Tree
There can arise cases where deleting the key eliminates a node and forces a decrease in the height of the tree.

Consider this tree where we wish to remove 60.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.22.png

Using the logic from Case II, we delete both instances of 60. But doing so will eliminate the right child of the root node completely.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.23.png

As a result, we'll need to restructure the tree completely, which ultimately results in the height shrinking.

Let's remedy this problem next.

To solve the previous issue, we bring down the parent of the recently deleted internal node and merge it with the sibling of the deleted node.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.24.png

As a result, we get the following tree:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.4.25.png

~ Deleting Keys for Large Datasets
Before concluding this chapter, let's discuss how deletions are handled in some practical scenarios.

Generally, if the size of data is very large and there is a constant influx of data, deletion can be done simply by removing the value from the leaf node.

In these cases, we get way more insertions as compared to deletions, so something will quickly replace whatever we delete.

This concludes our lessons on B/B+ trees.
'''