#...............Operations in Linked List.................#
# 
# INSERTING into a linked list
# DELETING from a linked list
# 



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self):

        # create and link nodes
        node1 = Node(80)
        node2 = Node(9)
        node3 = Node(14)
        self.head = node1
        node1.next = node2
        node2.next = node3

    # display linked list in format: A->B->C
    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

# 
# 
#.............Insert Into a Linked List...............#
# We can insert a node at any position in a linked list. 
# There are three cases for node insertion.
        # Insert a node at the end of a linked list(append).
        # Insert at the beginning of a linked list.
        # Insert at any given position.
# 
#.................Append a Node....................#
# Lets say we want to add a node with data 20 to the linked list we previously created.
# Here is how to do it:
# 
# 1. Create a new node.
    # We will use the Node class we discussed in the previous lesson to create a new node.
            # new_node = Node(20)
# 
# 2. Traverse until the last node of the linked list is reached.
    # Since we need to insert a node at the end, we must traverse until we reach the last node. So that we can add the new node after the last node.
            ## current variable points to the head node
            # current = self.head
            ## traverse until the last node (node pointing to None)
            # While current:
                # current = current.next
# 
# 3. Add a new node after the last node (current node).
            # current.next = new_node
# 
#................Append Element to an Empty Linked List.............#
# The code we discussed for appending to a linked list does not work if the linked list is empty.
# 
# If you recall the LinkedList class we introduced in the previous lesson, its head attribute is initially set to None.
            # class LinkedList:
                # def __init__(self):
                #     self.head = None
# This means that the head attribute of an empty linked list is None.
# Therefore, to append a new node to an empty linked list, we will simply set head to point to new_node.
            # if not self.head:
            #     self.head = new_node
            #     return


#...............APPEND A NODE................#
    # method to append a node at the end
    def append_node(self, data):
        # create a new node
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        # current variable points to the head node
        current = self.head
        # traverse until the last node (node pointing to None)
        while current.next:
            current = current.next
        current.next = new_node


#...............APPEND A NODE................#
    # method to append a node at the beginning of the Linked List
# Suppose we want to insert a node (10) at the beginning of a linked list.
# 1. Create a new node.
        # new_node = Node(10)
# 2. Link the new node to the head node.
        # new_node.next = self.head
# 3. Make the new node the starting node (the head).
        # self.head = new_node


    # method to insert a node at the beginning
    def insert_node_at_beginning(self, data):
        # create a new node
        new_node = Node(data)
        # link new_node to the head node
        new_node.next = self.head
        # make new_node the head node
        self.head = new_node


#...............APPEND A NODE................#
# Here is how to insert a node at a given position in a linked list.
# Suppose we have the following linked list. 
#   (8, 3, 9, 7, 6, none)
# Let's say we need to insert a new node at position 5 after node with value 7.
# Here are the steps to achieve it.
# 1. Create a new node.
            # new_node = Node(11)
# 2. Move the pointer to one position ahead of the desired position and assign it to the current variable.
            # current = self.head
            # for i in range(1, position - 1):
                    # current = current.next
# 
# NOTE: We move to position - 1 instead of position because we have to assign the next pointer of position - 1 to our new node.
# Since we have to insert at the fifth position, current should be at the fourth position.
# 3. Make the new node point to the next node of the current node
            # new_node.next = current.next
# 
# 4. Make the next of the current node point to the new node.
            # current.next = new_node
# 
# 
# 
# method to insert a node at a specific position
    def insert_node_at_position(self, data, position):
        # Create a new node.
        new_node = Node(data)
        # Move the pointer to one position ahead of the desired position
        current = self.head
        for i in range(1, position -1 ):
            current = current.next 
        # Make the new node point to the next node of the current node
        new_node.next = current.next
        # Make the next of the current node point to the new node.
        current.next = new_node


#...............INSERTING NODE IN A LINKED LIST..............#
# The program we wrote to insert a node doesn't work if:
        # the linked list is empty
        # the position is negative
        # the position is greater than the number of nodes.
# Let's address these situations as well by creating a universal method to insert nodes. For this, we'll use the separate methods we just discussed as helpers.

# Universal insert method
    def insert_node(self, data, position=None):
        if position is None:
            self.append_node(data)
            return
        if position <= 0 or position > self.get_length() + 1:
            print("Invalid posittion")
            return
        if position == 1:
            self.insert_node_at_beginning(data)
        elif position == self.get_length() + 1:
            self.append_node(data)
        else:
            self.insert_node_at_position(data, position)



#................DELETION FROM LINKED LIST..................#
# We can delete a node at any position in a linked list. There are two cases for node deletion:
        # Delete the first node.
        # Delete the node at a given position.


#..................Delete the first Node.....................#
# Process to Delete the First Node
# We can simply remove the first node by making the second node as the new head node.
            # self.head = self.head.next
# NOTE: For an empty linked list, we first need to check if the head exists. Otherwise, the code above results in an error.
#...............method to delete the first node..............#
    def delete_node(self):
        # if the linked list is not empty
        if self.head:
            self.head = self.head.next
            return
# NOTE: A common practice during delete operation is to return the value of the node being deleted. This helps keep track of which node is being deleted.


linked_list = LinkedList()

# create linked list
linked_list.create_linked_list()

    
