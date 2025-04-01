#..................Operations in Doubly Linked Lists.........................#
# Similar to singly linked lists, doubly linked lists support several common operations. Let's take a look at each of them:

# 1. Insert
    # Insert at the beginning of a doubly linked list.
    # Insert at the end of a doubly linked list.
    # Insert at any given position in a doubly linked list.
# 
# 2. Delete
    # Delete from the beginning of a doubly linked list.
    # Delete from the end of a doubly linked list.
    # Delete from any given position in a doubly linked list.

#...................Append Element.....................#
# We already know that appending means adding a node at the end of the linked list.
# 
# Suppose we have the following linked list:
#       80<=>9<=>14
# 
# To append 20 to the linked list, we will:

# 1. Update the references.
# To update the references, we will:
    # Make the next pointer of the tail node point to the new node.
    # Make the prev pointer of the new node point to the tail node.
# 
# 2. Update 'tail' to point to the new node.
# 
#...............Code: Append a Node into a Linked List............#
# So, our helper to insert a node at the end (append) will look like this.
        # insert at the end (append)
        # def append_node(self, data):
        #     # initialize a new node
        #     new_node = Node(data)
        #     # update links
        #     new_node.prev = self.tail
        #     self.tail.next = new_node
        #     # update tail
        #     self.tail = new_node

#.............Append Element in an Empty linked list.............#
# There might also be the case where there are no elements in the linked list.
# In that case, we will simply make both head and tail point to new_node.
# NOTE: By default, our Node class assigns None to both the prev and next pointers when we create a new node.

#..............Code: Append into an empty linked list.................#
# Our helper to append into an empty linked list will look like this:

        # # append to empty list
        # def append_to_empty(self, data):
        #     new_node = Node(data)
        #     self.head = new_node
        #     self.tail = new_node

# ...............Insert at the beginning................#
# Imagine we have the following list.
#               80<=>9<=>14
# To insert a node 10 at the beginning of the linked list, we will:
# 1. Update references.
    # Make the next pointer of the new node point to the head node.
    # Make the prev pointer of the head node point to the new node.
# 2. Update the 'head' node.
    # Now, we'll make the head pointer point to the new node.
# 
#..................Code: Insert at the Beginning..................#
# Now, let's look at the implementation of this operation.

        # # insert at beginning
        # def insert_at_beginning(self, data):
        #     # create new node
        #     new_node = Node(data)

        #     # update pointers
        #     new_node.next = self.head
        #     self.head.prev = new_node

        #     # update head
        #     self.head = new_node