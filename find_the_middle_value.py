#......................Find the Middle Node......................#

# Can you write a program to find the middle element in a linked list?
    # Add the find_middle_element() method to the LinkedList class using the outline provided in the editor.
    # The method should determine the middle element and return its data.
    # Print the returned data.

# How to solve it?
    # Initialize two variables slow and fast to the start of the linked list. The fast variable will be used for traversal.
    # During traversal, advance slow to the next element and fast two elements ahead.
    # When fast reaches the end, slow reaches the middle.

# NOTE: If there are two middle elements in linked list containing an even numbers of nodes. In such cases, return the second middle element.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self):
        node1 = Node(80)
        self.head = node1

        node2 = Node(9)
        node1.next = node2

        node3 = Node(14)
        node2.next = node3

    # helper method to append a node at the end
    def append_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # helper method to insert a node at the beginning
    def insert_node_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # helper method to insert a node at a specific position
    def insert_node_at_position(self, data, position):
        
        new_node = Node(data)
        current = self.head
        
        for i in range(1, position -1 ):
            current = current.next 
        
        new_node.next = current.next
        current.next = new_node

    # universal insert method
    def insert_node(self, data, position=None):
        # if no position is given
        # or position exceeds the length of the list
        # insert at the end
        if position is None or position >= self.get_length():
            self.append_node(data)
        elif position == 0:
            self.insert_node_at_beginning(data)
        else:
            self.insert_node_at_position(data, position)
        

    # helper method to get the length of the linked list
    def get_length(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    # traverse the list
    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)
    
   # method to return the middle element 
    def find_middle_element(self):

        # handle empty linked list
        if not self.head:
            return

        fast = self.head
        slow = self.head

        # traverse the linked list
        while fast is not None and fast.next is not None:

            # move fast two steps ahead
            fast = fast.next.next

            # move slow one step ahead
            slow = slow.next

        return slow.data

