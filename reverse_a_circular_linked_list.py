#..............Reverse a circular linked list.....................#
# 
# To reverse a circular linked list, you can start from the head and swap the next pointers of each node with the previous node. This process effectively reorders the elements in the list.
# 
# Suppose we have to reverse the following list:
        # (11->22->33->44)
# To reverse a circular linked list, we can follow these steps:
# 1. Create three refrences.
        # prev_node = None
        # current = self.head
        # next_node = current.next

# 2. Make the current node point to its preceding node.
        # current.next = prev_node
# 3. Slide the references.
        # prev_node = current
        # current = next_node
        # next_node = current.next
# 4. Repeat Steps 2 and 3 until you reach the head node again.
        # while True:
        #     # step 2 and 3

        #     if current == self.head:
        #         break
# 5. Adjust the head node.
        # self.head.next = prev_node
        # self.head = prev_node

#........Source code: reverse a circular linked list..........#
#...........reverse method............#
# 
        # def reverse(self):
        #.....# in case of 0 or 1 elements, no need to reverse
        #     if self.node_count() < 2:
        #         return
            
        #.....# define 3 pointers
        #     prev_node = None
        #     current = self.head
        #     next_node = current.next
            
        #     while True:
                
        #.....# assign next pointer of current to previous node
        #         current.next = prev_node
                
        #.........# slide the pointers
        #         prev_node = current
        #         current = next_node
        #         next_node = current.next
                
        #.........# repeat until you reach head again
        #         if current == self.head:
        #             break
            
        #.....# adjust head
        #     self.head.next = prev_node
        #     self.head = prev_node   


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
    
    # reverse method
    def reverse(self):
        # in case of 0 or 1 elements, no need to reverse
        if self.length() < 2:
            return
        
        # define 3 pointers
        prev_node = None
        current = self.head
        next_node = current.next
        
        while True:
            
            # assign next pointer of current to previous node
            current.next = prev_node
            
            # slide the pointers
            prev_node = current
            current = next_node
            next_node = current.next
            
            # repeat until you reach head again
            if current == self.head:
                break
        
        # adjust head
        self.head.next = prev_node
        self.head = prev_node   