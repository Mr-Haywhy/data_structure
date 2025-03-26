#..........FIND.THE.LARGEST.NUMBER.IN.A.LINKED.LIST...............#
# The process of finding the largest value in a linked list is similar to how we find the largest number in a list.
# To find the largest value in a linked list, we start by assuming the first node's value is the largest.
# Then, we traverse through each node. As we go through the nodes, we compare each node's value with our current largest value and update the largest value if needed.


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
    

# method to return the largest number 
    def find_largest(self):
        # condition to handle empty linked list
        if not self.head:
            return None
        current = self.head

        # initialize the value of head as largest
        largest = current.data

        # iterate until the last node
        while current:
            # update largest if necessary
            if current.data > largest:
                largest = current.data
            current = current.next
        return largest