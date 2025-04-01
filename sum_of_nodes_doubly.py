#..................Sum of Nodes....................#
# Write a program to find the sum of all the nodes in a doubly linked list.
# 
# You are provided with a function named compute_sum().
# You need to add the data of all nodes and return the sum of the nodes.
# 
# 
# create Node for linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# create a DoublyLinkedList class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # create a doublylinked list
    def create_linked_list(self):
        data = list(map(int, input().split()))

        nodes = [Node(i) for i in data]
        self.head = nodes[0]
        for i, node in enumerate(nodes):
            node.next = nodes[i+1] if i + 1 < len (data) else None
            node.prev = nodes[i - 1] if i -1 >= 0 else None

    def compute_sum(self):
        if self.head is None:
            return 0

        current = self.head
        total = 0
        while current is not None:
            total += current.data
            current = current.next
        

        return total
        
# create object of linked list
linked_list = DoublyLinkedList()
linked_list.create_linked_list()
print(linked_list.compute_sum())
