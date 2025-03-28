#..............Operations in circular linked lists..............#

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # create circular linked list.
    def create_linked_list(self):
        node1 = Node(80)
        self.head = node1

        node2 = Node(9)
        node1.next = node2

        node3 = Node(14)
        node2.next = node3

        # make the last node point back to the head, making it circular
        node3.next = self.head


# Similar to linked lists, circular linked lists support several common operations. Let's take a look at each of them:

# 1. Insert
    # Insert at the beginning of a circular linked list.
    # Insert at the end of a circular linked list.
    # Insert at any given position in a circular linked list.

# 2. Delete
    # Delete from the beginning of a circular linked list.
    # Delete from any given position in a circular linked list.

#...................Insert into linked list....................#

#.......Append an element to a circular linked list.......#
# 
# To append an element to a circular linked list, we follow the steps below:
    # 1. Traverse to the last node of the linked list.
    # 2. Point the next pointer of the last node to the new node.
    # 3. Make the new node point to the head node.


#.........Append element in an empty linked list.........#
# 
# There might also be cases where there are no elements in a linked list. That means there is a head node pointing to None.
# In that case, we will simply mark the new node as the head, and then make that node point to itself.

#.................Source Code: Append Element.................#
# So, our helper function to append an element to a linked list will look like this:

    def append_into_empty(self, data):
        new_node = Node(data)
        self.head = new_node
        new_node.next = self.head

    def append_node (self, data):
        # create a new node
        new_node = Node(data)

            # traverse to the end of the list
        current = self.head
        while current.next != self.head:
            current = current.next

            # adjust the next pointers
        current.next = new_node
        new_node.next = self.head


#...................Insert at the beginning................#
# Imagine we have the following list
        # (8, 3, 9, 7, 6)
# Suppose we need to insert a node 10 at the beginning, we follow the given steps:

# 1. Traverse the list and make the last node point to the new node.
# 2. Make the new node point to the head node and then make it the new head node.

# ...........Source Code: Insert at the beginning...........#

    # insert at the beginning of the linked list
    def insert_at_beginning(self, data):

        # create a new node
        new_node = Node(data)

        # traverse the linked list
        current = self.head
        while current.next != self.head:
            current = current.next

        # update the next pointers
        current.next = new_node
        new_node.next = self.head

        # update the head attribute
        self.head = new_node

#................Insert at a Given Position..................#
# Suppose we have the following linked list.
#       (8, 3, 9, 7, 6)

# To insert a new node [11] at the fifth position, we perform the following steps.
# 1. Traverse from the head node to the node at the 4th position (i.e., position - 1).
# 2. Make the new node point to the next node of the current node.
# 3. Make the next pointer of the current node point to the new node.

#...............Source code: Insert at given position...........#
    def insert_at_position(self, data, position):
        # create a new node
        new_node = Node(data)

        current = self.head

        # bring a pointer to position - 1
        # assign it to the current variable
        for i in range(1, position-1):
            current = current.next

        # make the new node point to
        # the next node of the current node
        new_node.next = current.next

        # make next pointer of current
        # point to the new node
        current.next = new_node


#...............Source Code: Insert Elements in a Circular Linked List................#

    def insert_node(self, data, position=None):
        if not self.head:
            self.append_into_empty(data)
        elif not position or position == self.length() + 1:
            self.append_node(data)
        elif position == 1:
            self.insert_at_beginning(data)
        else:
            self.insert_at_position(data, position)



linked_list = CircularLinkedList()
linked_list.create_linked_list()