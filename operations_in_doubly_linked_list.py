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
#               80<=>9<=>14<=>20
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
# 
#..............Insert at a given position................#
# Let's see how to insert a node at a given position in a doubly linked list.
# Suppose we have the following linked list.
#           10<=>80<=>9<=>14<=>20
# 
# To insert a new node (11) at the fourth position of the linked list, we will:
# 1. Traverse from 'head' node to node at position - 1.
# 2. Update Links.
# Now, we'll update the links as follows:
    # Make the next pointer of the third node point to the new node.
    # Make the prev pointer of the fourth node point to the new node.
    # Make the prev pointer of the new node point to the third node.
    # Make the next pointer of the new node point to the fourth node.
# 
#...............Code: Insert at a given position..................#
# So, our implementation of insertion at a given position will look like this.

        # # insert at position
        # def insert_at_position(self, position, data):
        #     # create new node
        #     new_node = Node(data)
        #     # bring a pointer to desired position 
        #     current = self.head
        #     for i in range(position - 1):
        #         current = current.next
                
        #     # get a pointer to the next node
        #     next_node = current.next

        #     # update pointers
        #     current.next = new_node
        #     next_node.prev = new_node

        #     new_node.prev = current
        #     new_node.next = next_node

# 
# 
#....................Source Code: Insert Elements in a Doubly Linked List......................#
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    #  traverse the linked list
    def traverse(self):
        # start at head
        current = self.head
        print("None", end = " <-> ")
        # loop until the node is None
        while current is not None:
            print(f"{current.data} <-> ", end="") 
            current = current.next
        print("None")
    # reverse traverse the linked list
    def reverse_traverse(self):
        # start at tail
        current = self.tail
        print("None", end = " <-> ")
        # loop until node is None
        while current is not None:
            print(f"{current.data} <-> ", end="") 
            current = current.prev
        print("None")
    
    # helper method to get the length of the list
    def length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    # insert at the end (append)
    def append_node(self, data):
        # initialize a new node
        new_node = Node(data)
        # update links
        new_node.prev = self.tail
        self.tail.next = new_node
        #  update tail
        self.tail = new_node

    # append to empty list
    def append_to_empty(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
    
    # insert at beginning
    def insert_at_beginning(self, data):
        # create new node
        new_node = Node(data)
    
        # update pointers
        new_node.next = self.head
        self.head.prev = new_node
    
        # update head
        self.head = new_node
    
    # insert at position
    def insert_at_position(self, position, data):
        # create new node
        new_node = Node(data)
        # bring a pointer to desired position 
        current = self.head
        for i in range(position - 1):
            current = current.next
        
        # get a pointer to the next node
        next_node = current.next

        # update pointers
        current.next = new_node
        next_node.prev = new_node

        new_node.prev = current
        new_node.next = next_node

    # method to handle all insert operations
    def insert_node(self, data, position = None):
        # check if the list is empty
        # and append to empty list
        if self.head is None:
            self.append_to_empty(data)
            return  # exit after handling this case
    
        # if position is None or not provided
        # append the node to the end
        if position is None:
            self.append_node(data)
            return  # exit after handling this case
    
        # if position is 0, insert at the beginning
        if position == 0:
            self.insert_at_beginning(data)
            return  # exit after handling this case
    
        # for a valid position,
        # get the current length of the list
        length = self.length()
    
        # if the position exceeds the length
        # append the node
        if position >= length:
            self.append_node(data)
            return  # exit after handling this case
    
        # if none of the above conditions are met,
        # insert at the specified position
        self.insert_at_position(position, data)


# example usage:
linked_list = DoublyLinkedList()

print("Original Linked List")
linked_list.traverse()
print()

# insert into an empty list
linked_list.insert_node(80)
print("Linked List After Inserting 80 to Empty List")
linked_list.traverse()
print()

# insert at the beginning
linked_list.insert_node(9, 0)
print("Linked List After Inserting 9 at the beginning")
linked_list.traverse()
print()

# insert at position 1
linked_list.insert_node(14, 1)
print("Linked List After Inserting 14 at the position 1")
linked_list.traverse()
print()

# append at the end
linked_list.insert_node(25)
print("Linked List After Inserting 25")
linked_list.traverse()