#....................REVERSE.ELEMENTS.OF.A.LINKED.LIST....................#
# To reverse elements of a linked list, we will
    # Copy the values of the linked list to a new list.
    # Iterate through the new list in reverse order.
    # Assign the reversed values to the nodes of the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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
    

# Method to reverse elements of a linked list
    def reverse_elements(self):
        # new list to copy the values
        values = []
        current = self.head

        # copy values of linked list to the new list
        while current:
            values.append(current.data)
            current = current.next
        
        current = self.head

        # iterate through the new list in reverse order
        for value in reversed(values):
            # copy the reversed value to the original list
            current.data = value
            current = current.next  