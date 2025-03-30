#..............Search in a circular linked list..................#
# 
# To check if a specific value exists in a circular linked list, you can start from the head and traverse the list until you either find the value or complete a full loop.
# Suppose we have to search in the following list:
# 11->22->33->44
# Let us search for 33
# 1. Start at the head node.
        # current = self.head
# 
# 2. Loop until the node is found.
        # while True:
        #     current = current.next
        #     if current.data == 33
        #         return True
# 
# If the value is not in the list, we stop the loop after we reach the head again. This implies that we have traversed all nodes, and we didn't find the value.

        # while True:
        #     current = current.next
        #     if current == self.head
        #         return False


#..............Source Code: Searching in a circular linked list...............#
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
    
    # search method
    def search(self, value):
        current = self.head
        
        while True:
            # move to next
            current = current.next
            # True if value is found
            if(current.data == value):
                return True
            # False if loop is complete
            if(current == self.head):
                return False