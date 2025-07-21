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

~ Branching in B-Trees
Like in general trees, the number of children at each node of a B-tree is called the branching factor.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.1.3.png

In B-trees, however, the branching of each node is limited by the number of keys contained in the node.

The branching factor of a B-tree is defined as the number of children a node can have. The branching factor is determined by the order of the B-tree.

~ Relationship Between Keys and Branches
Any node can contain an arbitrary number of keys (say, n) in sorted order. Any internal node with n keys will have n+1 children.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.1.4.png

The keys in the node affect not only the branching factor but also the range of values of keys in each of its descendants. We'll discuss this in detail on the next page.

~ Left Branching in B-Trees
B-trees have to comply with the property of search trees, where:
    * The keys to the left are smaller than the selected key.
    * The keys to the right are larger than the selected key.

Hence, B-trees have sorted branching.

So the leftmost possible child of any node can only hold values smaller than the smallest key of that node.

Let's look at the previous figure again.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.1.5.png

In the above figure, we can see that the branch to the left of key 40 can only have values less than 40.

Next, let's look at branching to the right of a key.

~ Right Branching in B-Trees
We just learned that the leftmost possible child of any node can only hold values smaller than the smallest key of that node.

Similarly, the rightmost possible child of a node can only have keys larger than the largest key of that node.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.1.6.png

In the above figure, we can see that the branch to the right of key 65 can only have values greater than 65.

~ Middle Branching in B-Trees
Finally, let's talk about branching between keys.

The child between two keys can only have values in between those keys.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.1.7.png

In the above figure, we can see
    * The branch between the keys 40 and 55 can only have values greater than 40 and less than 55 (i.e. the keys 41 and 54).
    * The branch between the keys 55 and 65 can only have values greater than 55 and less than 65 (i.e. the keys 56 and 64).

Hence, the keys in a node affect both its branching factor and the position of the descendent nodes.

Now that we are well-acquainted with the anatomy of a B-tree, we'll learn its importance next.

~ Why B-Trees?
B-Trees are built specially for database systems and are designed to handle large volumes of data.

Computers generally have two forms of memory:

    Memory Type	        |           Description
Primary Memory	        |  Super fast but can only store a small amount of data.
Secondary Memory	    |   Can store a lot more data but is much slower to access.

When working with large amounts of data, the computer often needs to fetch pieces of the data from the secondary memory and load it into the primary memory.

Each time it does this, it performs a disk transfer, and the total time taken for these transfers is what we call I/O complexity.

To make things faster, we want the computer to fetch data with as few disk transfers as possible.

This is where the design of B-trees comes in — they're built in a way that minimizes these disk transfers by loading selective pages from the secondary memory to the primary memory.

Let's try to understand this using an example.

~ Working of a B-Tree
Previously, we learned that B-trees minimize disk transfers by loading selective pages from the secondary memory to the primary memory. Let's see how this works with an example.

If we were to search for 20 in this B-tree, only those nodes in the path leading to 20 would be loaded into our primary memory.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.1.8.png

But then, you might be wondering why we shouldn't increase the capacity of a node to include more keys like this.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.1.9.png

Here, we only needed to load two nodes into the primary memory compared to three in the previous case.

However, this nullifies the search optimization offered by trees due to its hierarchical nature, and the search process instead resembles that of a linked list.

Let's witness this difference in efficiency between these two methods in the next page.

Below are the two trees we discussed in the previous page. For illustrative purposes, let's try to search for 30 instead of 20 in both cases.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.1.10.png

In the first tree, we only needed two steps to find 30, whereas we needed six steps to find it in the second case.

In the first tree, we can see that we only need to load three nodes into the primary memory to find 30. This is because the keys are distributed across multiple nodes, allowing us to quickly narrow down our search.
In the second tree, however, we need to load all five nodes into the primary memory to find 30. This is because all the keys are concentrated in a single node, making it harder to narrow down our search quickly.

~ B-Trees Can Save Memory!
B-trees also tend to be memory-efficient in cases similar to the previous example. Let's assume each key costs 1 byte of primary memory and compare the memory cost by loading the nodes in both cases.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.1.11.png

Here, we can see that, despite loading more nodes to the primary memory, the first tree occupied less space compared to the second tree, which loaded fewer nodes.

~ Actual Representation of a B-Tree
In the database, each key is associated with a data.

Consider the B-tree below:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.1.12.png

This tree actually looks like this:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.1.13.png

We just omit the data in our diagrams for simplicity in visualizing trees.

Deciding how many keys to fit in a node is determined using a design parameter called minimum degree of tree, which is discussed in the following page.

~ Minimum Degree of a B-Tree
Every tree has a maximum and minimum number of keys it can have in each node, which is controlled by a parameter called the minimum degree of a tree.

This parameter is generally denoted by t.

The minimum degree of a tree is chosen based on the size of the data and the resources available.

There are two things to note while choosing the minimum degree for our B-tree:
    * A smaller t (e.g. t = 2) will result in a taller B-tree, which is better for memory management.
    * A larger t (e.g. t = 10) will result in a wider B-tree, which is better for performing search operations at high speeds.

Based on the value of t, our B-tree will strictly follow the following set of properties:
    * Each node can have a maximum of 2t - 1 keys and a minimum of t - 1 keys.
    * Each node can have at least t children and at most 2t children.

NOTE: Root is an exception where the number of keys can be less than t - 1.

In the next lesson, you'll learn about operations in a B-tree. But not before you take a couple of quizzes!

~ B-Tree Operations
B-trees support a variety of operations, including insertion, deletion, and searching. These operations are designed to maintain the properties of the B-tree while efficiently managing the data.

Similar to other trees, we will cover the following three operations in a B-tree:
    1. Insertion into a B-tree.
    2. Search in a B-tree.
    3. Deletion from a B-tree.

We will start with the insertion process.

~ Insertion in a B-Tree
Insertion in B-trees follows the same pattern as in any other search tree. The insertion process can be summarized in two steps:
    * Insert into the search tree.
    * Balance the tree.

Example 1: Insertion Into a B-Tree
Consider the following tree with a minimum degree of 3.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.1.png

Let's insert 29 into the tree.

Example 1: Insertion Into a B-Tree
We need to insert the key 29 into the previous tree. The first step here is to perform search tree insertion.

While performing search tree insertion, the most important thing to remember is that new insertions can only be done in the leaf nodes.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.2.png

For a tree of minimum degree 3, each node should have
    * At least 3 - 1 = 2 keys.
    * At most 2 * 3 - 1 = 5 keys.

Since the number of keys is within this range, the insertion is complete.

Example 2: Insertion Into B-Trees
Consider another example where the minimum degree is 3.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.3.png

Let's try inserting 90 into the tree.

As before, we perform search tree insertion.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.4.png

For a tree of minimum degree 3, each node should have
    * At least 3 - 1 = 2 keys.
    * At most 2 * 3 - 1 = 5 keys.

If inserting keys causes a node to have more than 2t-1 keys, then the situation is called an overflow. Here, we can see there is an overflow in our node.

~ Handling Overflows With Splitting
To handle overflows such as the one we saw on the previous page, we introduce a method called splitting. Splitting consists of two steps:
    1. Split the node around its median key.
    2. Move the median key up to the parent node.

Now, the split node will result in two new nodes:
    * The left leaf node contains keys smaller than the median.
    * The right leaf node contains keys greater than the median.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.5.png

The median key is then moved up to the parent node, which will also be split if it overflows. This process continues until we reach the root node.
If the root node overflows, we create a new root node and set the median key as the only key in the new root node. This effectively increases the height of the B-tree by one level.

Example 3: Insertion Into B-Tree
We may also run into a situation where the parent is also full. In such cases, we have to split the parent node in the same manner.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.6.png

Now the parent node has an overflow, which we will solve next.

To fix the overflow of the parent node, we split it from the median key.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.7.png

This problem may rise to the root node. In such a case, the median value of the original root becomes the new root, and two new instances of child nodes rise as a result.

NOTE: The height of the tree increases only if the root node is split.

~ Search in a B-Tree
Searching in a B-tree resembles searching in a binary search tree (BST).

Here's how you search for a specific key in a BST:
    1. First, you compare it to the current node's key.
    2. If the target key is smaller than the current node's key, you navigate to the left child node to continue the search.
    3. Conversely, if the key is larger, you move to the right child node for further searching.

Next, let's apply this general principle to search in a B-tree.

Just like in BST, we compare the target key with the keys of the B-tree before deciding to traverse to the child nodes.

However, since a node in a B-tree can contain multiple keys, the search process involves examining the keys within the same node before considering a move to the node below.

    * In practice, you often traverse to the right within the same node until you encounter a key that is greater than the one you are searching for.
    * It is only at this point that you proceed to move down to the next node, similar to how you would navigate in a binary search tree (BST).

For example, let's try to find 45 in this B-tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.8.png

With this, let's move on to deletion.

~ Deletion From B-trees
Once again, deletion from B-trees follows the same pattern as a deletion in search trees.
    * Delete from search trees.
    * Balance the tree.

Depending on which node is being deleted, deletion in B-trees can have the following two cases:
    * Case I: Deleting a key from an internal node.
    * Case II: Deleting a key from a leaf node.

~ Case I: Deleting a Key From an Internal Node
Consider the following tree with a minimum degree of 3.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.9.png
Deleting from an internal node has multiple subcases. Let's explore them one at a time.

~ Case I(a): Deleting a Key with a Left Child
If a node has a left child,
    1. We simply replace it with its immediate predecessor in the child node.
    2. Then, we remove the original instance of the predecessor from the tree.

Consider deleting key 12 from the previous tree.

First, let's look at the key and its children separately.

Remember: The left child of a node or key can only contain elements smaller than that node or key.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.10.png

As can be seen, key 12 only has a left child and no right child.

So, we remove the 12 and replace it with 11, i.e., its predecessor in the child node.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.11.png

~ Case I(b): Deleting a Key with a Right Child
If a node has a right child, we simply replace the key with its successor and delete the original instance of the successor.

Consider deleting key 4 from the previous tree.

Like before, let's look at the key and its children in isolation.

Remember: The right child of a node or key can only contain elements greater than that node or key.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.12.png

We can see that key 4 only has a right child.

So, we remove 4 and replace it with 5 i.e., its successor in the child node.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.13.png

~ Case I(c): Deleting a Key with Both Children
If a node has both children, we simply replace the key with either its predecessor or its successor.

Let's try and delete 8 from the previous tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.14.png

Since 8 has both left and right children, we can replace the key with either its predecessor or successor.

For this example, we'll replace it with its predecessor.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.15.png

Similar to BST, we can see that
    * Deleting a key from an internal node simply replaces the key with its inorder predecessor or successor.
    * The actual key being deleted is a key of the left child.

Now, let's move on to deletion from a leaf node.

~ Case II: Deleting a Key From a Leaf Node
Deleting a key from a leaf node has four subcases:
    * The leaf node has more than t keys.
    * The left sibling has more than t keys.
    * The right sibling has more than t keys.
    * Neither sibling has more than t keys.

NOTE: t represents the minimum degree of the tree.

~ Case II(a): The Leaf Node Has More Than t Keys
This is the simplest form of deletion. If the node already contains more than t keys, we can simply delete the key.

Consider the following tree with a minimum degree of 3, where we need to delete key 60.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.16.png

This is what the tree will look like after deletion:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.17.png

As you can see, deleting this key is a straightforward process.

~ Case II(b): The Left Sibling Has More Than t Keys
Sometimes, the node from which the key is deleted may end up having fewer keys than the minimum degree. This is known as underflow.

In such cases, we borrow the required keys from the underflow node's siblings.

Let's delete key 20 from the previous tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.18.png

We now have a node with only one key.

However, a tree of minimum degree 3 needs at least 2 keys in each node. Thus, we need to borrow a key from one of its siblings.

Let's see how to do that next.

~ Case II(b): The Left Sibling Has More Than t Keys
Here's how our previous B-tree looks like after deletion:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.19.png

In the above example, we can see that the left sibling has more keys (3) than the minimum number of keys (2).

So, we can simply borrow keys from the left sibling.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.20.png

But simply taking keys from the sibling will break the sorted order of B-trees. Let's see how we can prevent it.

~ Case II(b): The Left Sibling Has More Than t Keys
To avoid breaking the sorted order of B-trees, the borrowing is done in two steps.

The last key of the left sibling is taken by the parent.
The separator key in the parent is moved to the underflow node.
Let's see how this works in our tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.21.png

~ Case II(c): The right sibling has more than t keys
If we cannot borrow a key from the left sibling, we will simply borrow it from the right sibling.

Continuing from the previous example, let's delete key 30 from the tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.22.png

Again, there is an underflow and we have to borrow keys from one of its siblings.

Since the left sibling only has two nodes, we can't borrow from it.

Consequently, we'll be borrowing from the right sibling.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.23.png

~ Case II(d): Neither Sibling Has More Than t Keys
Here's what we've learned so far:
    * In cases of underflow, we borrow keys from the left sibling.
    * If the left sibling doesn't have enough keys, we borrow from the right sibling.

But if both the left and the right siblings of the underflow node have t keys, we can't borrow from any of the siblings.

In such cases, the underflow node is combined with either its left or its right sibling.

Continuing from the previous example, let's remove key 40.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.24.png

There is an underflow in the tree. However, neither of the siblings has enough keys to borrow the keys.

Let's see how we can solve this problem.

When neither of the siblings has enough keys to borrow the keys, we merge the underflow node with its left sibling.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.25.png

Since key 15 cannot go directly to the left sibling, we move the key to the parent and the separator key (13) from the parent to the left sibling.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-19.2.26.png

This marks the end of B-trees.
'''