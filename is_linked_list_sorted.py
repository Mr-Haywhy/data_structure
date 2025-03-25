#................CHECK.IF.A.LINKED.LIST.IS.SORTED...............#
# To check if a linked list is sorted in ascending order, we need to traverse the list.
# We compare if the next node is smaller than the current node, we know the linked list is not sorted.
# But if each node is smaller than the next node right until the end of the linked list, then it is sorted.

# method to check if a linked list is sorted 
def is_sorted(self):
    # empty linked list is considered sorted
    if not self.head:
        return True
    current = self.head
        
    # traverse the linked list
    while current.next:
        # if current node is greater than next
        # the linked list is unsorted
        if current.data > current.next.data:
            return False
        current = current.next
    return True