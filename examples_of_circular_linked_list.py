#.......................Examples: Circular Linked List....................#
# You can also perform other operations in a circular linked list. Some of them are:
    # Find the maximum value in a circular linked list.
    # Reverse a circular linked list.
    # Search in a circular linked list.
# 
# 
#....................Find Maximum in a Circular Linked List......................#
# Suppose we have to find the maximum of the following circular linked list:
        # 22->88->66->33
# The output should be:
        # 88
# 
#....................Thought Process..................#
# To find the maximum of a circular linked list, follow the approach below.
# 
# 1. Start with the head node and assume it is the maximum.
        # current = head
        # maximum = head.data
# 
# 2. Move to the next node and compare with the current maximum. If the node's data is greater than the current maximum, change the maximum value.
        # current = current.next
        # if current.data > maximum:
        #     maximum = current.data
# 
# 3. Repeat the process until you reach the head node again.
        # while current.next is not self.head:
        #     current = current.next
# 
#............Source code: find maximum in a circular linked list.............#


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self):
        node1 = Node(80)
        self.head = node1

        node2 = Node(9)
        node1.next = node2

        node3 = Node(14)
        node2.next = node3

        node3.next = self.head
        
    def length(self):
        if not self.head:
            return 0
        current = self.head
        count = 1
        while current.next != self.head:
            current = current.next
            count += 1
        return count
    
    def display(self):
        nodes = []
        if self.head is None:
            return "Empty Linked List"
        current = self.head
        while current.next is not self.head:
            nodes.append(str(current.data))
            current = current.next
        nodes.append(str(current.data))
        return " -> ".join(nodes) + f" -> {self.head.data} "
    
    def append_into_empty(self, data):
        new_node = Node(data)
        self.head = new_node
        new_node.next = self.head
    
    def append_node(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_position(self, data, position):
        new_node = Node(data)
        current = self.head
        for i in range(1, position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def insert_node(self, data, position=None):
        if not self.head:
            self.append_into_empty(data)
        elif not position or position == self.length() + 1:
            self.append_node(data)
        elif position == 1:
            self.insert_at_beginning(data)
        else:
            self.insert_at_position(data, position)
    
    def delete_from_beginning(self):
        temp = self.head
        current = self.head
        while current.next is not self.head:
            current = current.next
        self.head = self.head.next
        current.next = self.head

    def delete_only_node(self):
        temp = self.head
        self.head = None
    
    def delete_at_position(self, position):
        current = self.head
        prev_node = None
        for i in range(1, position):
            prev_node = current
            current = current.next
        prev_node.next = current.next
    
    def delete_nodes(self, position):
        if self.head is None:
            return "Error: The list is empty."

        if position == 1:
            if self.head.next == self.head:  
                self.delete_only_node()
            else:
                self.delete_from_beginning()
        else:
            temp = self.head
            count = 1
            while temp.next != self.head:
                count += 1
                temp = temp.next
            
            if position > count:
                return "Error: Position is out of bounds."

            self.delete_at_position(position)
    
    def find_max(self):
        # empty circular linked list has no head
        if not self.head:
            return None

        # start with head
        current = self.head
        # assign first value as maximum
        maximum = current.data

        while current.next is not self.head:
            current = current.next
            if current.data > maximum:
                maximum = current.data
        return maximum