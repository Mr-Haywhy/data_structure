#...................Doubly linked list....................#
# 
# Normally, in a linked list, every node points to its next node.
# However, we can also create a linked list where a node points to both its previous and next elements. This type of linked list is called a doubly linked list.
# For convenience, we will also take reference to the last node, which we will call the tail node.
# 
#.................Why Doubly linked lists.................#
# Imagine you're designing a text editor where users can enter and edit text.
# Now, suppose you want to add the undo and redo options. This requires moving through the memory in both directions.
# Unfortunately, singly linked lists only move in a single direction, i.e., forward:
# As a result, we can't perform an undo operation using a singly linked list.
# Instead, we need to start from scratch and go through each step, which results in O(n) time complexity and is thus not ideal.
# There's a simple and elegant solution: the doubly linked list.
# Each node points to the next and previous nodes, forming a two-way chain.
# This speeds up redo (O(1)) and undo (O(1))—a game-changer in real-time text edits.
# Doubly linked lists find applications beyond text editors, including task scheduling, cache management, and doubly ended queue implementations.
# 
#..............Create a doubly linked list.................#
