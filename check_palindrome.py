#.......................Check Palindrome........................#

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def traverse(self):
        current = self.head
        print("None", end = " <-> ")
        while current is not None:
            print(f"{current.data} <-> ", end="") 
            current = current.next
        print("None")
    
    def reverse_traverse(self):
        current = self.tail
        print("None", end = " <-> ")
        while current is not None:
            print(f"{current.data} <-> ", end="") 
            current = current.prev
        print("None")
    
    def length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length
        
    def append_node(self, data):
        new_node = Node(data)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def append_to_empty(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
    
        new_node.next = self.head
        self.head.prev = new_node
    
        self.head = new_node
    
    def insert_at_position(self, position, data):
        new_node = Node(data)
        current = self.head
        for i in range(position - 1):
            current = current.next
        
        next_node = current.next

        current.next = new_node
        next_node.prev = new_node

        new_node.prev = current
        new_node.next = next_node
    
    def delete_from_beginning(self):
        current = self.head
        self.head = self.head.next
        self.head.prev = None
        current.next = None
    
    def delete_single_element(self):
        self.head = None
        self.tail = None
    
    def delete_from_end(self):
        current = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        current.prev = None
    
    def delete_from_position(self, position):
        current = self.head
        prev_node = next_node = None
        for i in range(position-1):
            current = current.next
        prev_node = current.prev
        next_node = current.next
    
        prev_node.next = next_node
        next_node.prev = prev_node
    
        current.next = None
        current.prev = None
    
    def insert_node(self, data, position = None):
       
        if self.head is None:
            self.append_to_empty(data)
            return  
    
        if position is None:
            self.append_node(data)
            return  
    
        if position == 0:
            self.insert_at_beginning(data)
            return  
    
        length = self.length()
    
        if position >= length:
            self.append_node(data)
            return  
    
        self.insert_at_position(position, data)

    def delete_node(self, position=None):
        if self.head is None:
            print("The list is empty.")
            return
        
        if self.length() == 1:
            self.delete_single_element()
            return
    
        if position == 1:
            self.delete_from_beginning()
            return
        
        if position is None or position == self.length():
            self.delete_from_end()
            return
    
        if 1 < position < self.length():
            self.delete_from_position(position)
            return
        else:
            print("Invalid position.")
            return
    

# Suppose we have to check if the following is a palindrome.
        # 10<=>80<=>80<=>10
# 
# Here's how we can do that:
    # 1. Get references to both the 'head' and 'tail' nodes.
                # start = self.head
                # end = self.tail
    # 2. If the data doesn't match, return False.
                # if start.data != end.data:
                #     return False
    # 3. Move forward from 'head' and backward from 'tail.'
                # start = start.next
                # end = end.prev
    # 4. Repeat until the end is no longer after start.
                # while start != end and start.prev != end:
                #     if(start == end or start == end.next):
                #         return True

#....................check if list is palindrome......................#
    def is_palindrome(self):
        # palindrome doesn't apply
        # for empty linked lists
        if not self.head:
            return True
        
        # get reference to both head and tail
        start = self.head
        end = self.tail

        # `while start != end and start.next != end:` to ensure all elements are compared.
        while start != end and start.prev != end:
            # return False if data don't match
            if start.data != end.data:
                return False
            # move forward from head
            # and backward from tail
            start = start.next
            end = end.prev
            # repeat until end is
            # no longer after start
        if(start == end or start == end.next):
            return True


linked_list = DoublyLinkedList()
list1 = [10, 80, 80, 10]
for i in list1:
    linked_list.insert_node(i)

linked_list.traverse()

if linked_list.is_palindrome():
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")