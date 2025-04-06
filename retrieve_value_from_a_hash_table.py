# ....................Retrieve Value from a Hash Table.....................
# Here's the hash table output from the last example.

    # 0: None
    # 1: None
    # 2: 12->None
    # 3: None
    # 4: 4->14->None
    # 5: 15->None
    # 6: None
    # 7: 17->27->37->None
    # 8: None
    # 9: None

# Suppose we need to retrieve item 27 from this hash table. Here's how we can achieve this:

    #* Apply the hash function to find the hash value. For the key 27, the hash is 7.
    #* Then, look into the hash table with this hash. This will give us a linked list (or None if the item doesn't exist).
    #* Then, we will traverse the linked list until the item is found or the last element of the linked list is reached.

# Let's add a method to implement this in our code and see how it works next.


# a class to represent a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# a class to represent a linked list
class LinkedList:
    def __init__(self):
        self.head = None
    
    # return the linked list elements
    def traverse(self):
        current = self.head

        result = ""

        while current:
            result += (f"{current.data}->")
            current = current.next
        
        result += "None"

        return result   
    
    # append an item to the linked list
    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
       
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

class HashData:

    # initialize a list of 10 items
    def __init__(self):
        self.table = [None] * 10

    # compute hash
    def hash_function(self, key):
        return key % 10

    # insert data to hash table
    def put(self, key):
        # insert into table
        hash_value = self.hash_function(key)
         # if the slot is empty	
        if not self.table[hash_value]:
            # create a linked list at the slot
            self.table[hash_value] = LinkedList()
        # append item to the linked list
        self.table[hash_value].append(key)

    # display hash table
    def display(self):
        for hash_value, key in enumerate(self.table):
            # if slot is a linked list
            if key: 
                print(f"{hash_value}: {key.traverse()}")
            # if slot is empty
            else:
                print(f"{hash_value}: {key}")

# This method returns None if the element is not in the hash table. If the element is in the hash table, it returns that value.

    # retrieve key from hash table
    def retrieve(self, item):

        hash_value = self.hash_function(item)
        key = self.table[hash_value]
        if key:
            current = key.head
            # when value is found, stop traversal
            while current:
                if current.data == item:
                    return {"hash_value": hash_value, "key": item}
                current = current.next
        return {"hash_value": hash_value, "key": None}

hash1 = HashData()

# keys
keys = [12, 17, 15, 4, 27, 14, 37]

# apply hash function to each key
for key in keys:
    hash1.put(key)

print(hash1.retrieve(12))
print(hash1.retrieve(47))