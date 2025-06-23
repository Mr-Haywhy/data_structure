"""
~ Introduction
A heap is a valuable data structure to implement a priority queue.

A priority queue is a type of queue in which every element has a key (priority) attached to it, and the queue returns these elements on the basis of these keys.

~ Real-life Analogy
Consider a workplace having 10 tasks. The tasks are labeled from priority 1 (top priority) to priority 10 (least priority).

Ideally, you would want to complete the task with priority 1 followed by priority 2, and so on, regardless of when the task enters the queue.

A heap allows you to do so.

~ Max-Priority Queue and Min-Priority Queue
- Max-Priority Queue
A max-priority queue returns the element with the maximum key first.

~ Real-life Analogy
In a hospital, patients arrive with varying degrees of medical urgency.

Patients with life-threatening injuries or illnesses are treated first. Then, the less serious patients are observed, while the least serious patients are observed last.

- Min-Priority Queue
It is a priority queue that returns the element with the minimum key first.

~ Real-life Analogy

In business, some products get better reviews, and some products get bad reviews.

In order to improve overall customer experience, you would want to prioritize and improve products with the lowest ratings first, followed by the higher-rated products.

Thus, the highest-rated product has the least priority.

In this lesson, we will implement a min-priority queue.

~ Implementation of a Priority Queue
We will use a heap to implement a priority queue.

There are four main operations we will be performing in a min-priority queue:
    1 Insert: To insert a new element into the queue.
    2 Peek: To peek the minimum element from the queue.
    3 Extract Min: To remove and return the minimum element from the queue.
    4 Increase / Decrease Key: To increase or decrease the key (priority) of any element in the queue.

~ Thought Process: Priority Queue
1. Create a priority queue.
We can create the priority queue as a child of the MinHeap class.

    class PriorityQueue(MinHeap):
        def __init__(self):
            super().__init__()

2. Insert, peek and extract min in the priority queue.
We have already defined these methods in min heap implementation. So, we can simply use them in our PriorityQueue class.

    def insert(self, value, priority):
        super().insert((priority,value))

    def extract_min(self):
        return super().extract_min()

    def peek(self):
        return super().peek() 

NOTE: In priority queues, we are inserting a tuple (priority, value). So, to access the priority of ith node, we use self.heap[i][0], since priority is the first item in the tuple.

Similarly, to access the ith value, we use self.heap[i][1].

"""

# Source Code: Priority Queue
class MinHeap:
    def __init__(self):
        self.heap = []
        
    # return the number of nodes in a heap
    def size(self):
        return len(self.heap)

    # check if the heap is empty
    def is_empty(self):
        return len(self.heap) == 0

    # string representation of a heap
    def __str__(self):
        return str(self.heap)

    # swap the heap values
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # calculate the index of a node's parent
    def parent(self, index):
        return (index - 1) // 2

    # calculate the index of a node's left child
    def left_child(self, index):
        return 2 * index + 1

    # calculate the index of a node's right_child
    def right_child(self, index):
        return 2 * index + 2

    # check if a node at a given index has a parent
    def has_parent(self, index):
        return self.parent(index) >= 0

    # check if a node at a given index has a left child
    def has_left_child(self, index):
        return self.left_child(index) < len(self.heap)

    # check if a node at a given index has a right child
    def has_right_child(self, index):
        return self.right_child(index) < len(self.heap)
       
    # heapify 
    def heapify(self, array):
        self.heap = array
        for i in range(len(self.heap) - 1, -1, -1):
            if  self.has_left_child(i):
                self.heapify_down(i)

    # heapify down
    def heapify_down(self, index):
        if not self.has_left_child(index):
            return
        smaller_child_index = self.left_child(index)
        if self.has_right_child(index): 
            if self.heap[self.right_child(index)] < self.heap[smaller_child_index]:
                smaller_child_index = self.right_child(index)
        if self.heap[index] > self.heap[smaller_child_index]:
            self.swap(index, smaller_child_index)
        if self.has_left_child(smaller_child_index):
            self.heapify_down(smaller_child_index)
    
    # heapify up
    def heapify_up(self, index):
        if self.has_parent(index): 
            parent_index = self.parent(index)
            # compare the value to its parent and swap if necessary
            if self.heap[index] < self.heap[self.parent(index)]:
                parent_index = self.parent(index)
                self.swap(index, parent_index)
                # run the code for parent                 
                if self.has_parent(parent_index):
                    self.heapify_up(parent_index)
    
    # insert into heap
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(self.size() - 1)

    # extract min from heap
    def extract_min(self):
        min = self.heap[0]
        if self.size() == 1:    
            self.heap = []
            return min
        self.heap[0] = self.heap[-1] 
        self.heap.pop()
        self.heapify_down(0)
        return min
    
    # peek
    def peek(self):
        return self.heap[0]

class PriorityQueue(MinHeap):
    # use methods from MinHeap Class
    def __init__(self):
        super().__init__()
        
    def insert(self, value, priority):
        super().insert((priority,value))

    def extract_min(self):
        return super().extract_min()

    def peek(self):
        return super().peek() 

# create a priority queue
priority_queue = PriorityQueue()

# tasks with priorities
tasks = [(12, 'Task1'), (15, 'Task2'), (25, 'Task3'), (16, 'Task4'), (5, 'Task5')]

# insert into priority queue
print('Insert tasks into priority queue')
for priority, task in tasks:
    priority_queue.insert(task, priority)
print(priority_queue)
print('--------------')

# peek at the new element with the highest priority(min value)
print('Top priority task')
print(priority_queue.peek()) 
print('-----------')

# top priority task is complete
priority_queue.extract_min()
print('After removing top priority task')
print(priority_queue)


"""
Output:
    Insert tasks into priority queue
    [(5, 'Task5'), (12, 'Task1'), (25, 'Task3'), (16, 'Task4'), (15, 'Task2')]
    --------------
    Top priority task
    (5, 'Task5')
    -----------
    After removing top priority task
    [(12, 'Task1'), (15, 'Task2'), (25, 'Task3'), (16, 'Task4')]
"""

"""
~ Increase/Decrease the Key (Priority)
Consider the following priority queue (heap).
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.6.1.png

Assume we need to change the priority of 12.

Let's assume two cases
    * Case 1: To increase the priority of 12, we increase the key of 12 to 20.
    * Case 2: To decrease the priority of 12, we decrease the key of 12 to 2.

NOTE: The values 12 and 20 are taken at random; we just increase the value to increase the priority and decrease the value to decrease the priority.

The heaps will now look like this after changing the value and heapifying:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.6.2.png

~ Thought Process: Increase/Decrease Key
When you want to modify the priority of a key in a priority queue, follow these steps:

1. Find the key in the heap.
To find the key whose priority you want to change, iterate through the heap:

    for i in range(self.size()):
        if self.heap[i][1] == value:
        
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.6.3.png

2. Update the Priority.
    old_priority = self.heap[i][0]
    self.heap[i] = (new_priority, value)

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.6.4.png

3. Re-Heapify.
After updating the priority, you need to restore the heap property:
    * If the priority has been increased, compare the key with its child and push it down the heap.
    * If the priority has been decreased, compare the key with its parent and push it up the heap.

    if new_priority < old_priority:
        self.heapify_up(i)
    else:
        self.heapify_down(i)

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.6.5.png

After these steps, the priority queue will be updated and maintain its heap property.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-12.6.6.png

"""

# Example: Priority Queue

class MinHeap:
    def __init__(self):
        self.heap = []
        
    # return the number of nodes in a heap
    def size(self):
        return len(self.heap)

    # check if the heap is empty
    def is_empty(self):
        return len(self.heap) == 0

    # string representation of a heap
    def __str__(self):
        return str(self.heap)

    # swap the heap values
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # calculate the index of a node's parent
    def parent(self, index):
        return (index - 1) // 2

    # calculate the index of a node's left child
    def left_child(self, index):
        return 2 * index + 1

    # calculate the index of a node's right_child
    def right_child(self, index):
        return 2 * index + 2

    # check if a node at a given index has a parent
    def has_parent(self, index):
        return self.parent(index) >= 0

    # check if a node at a given index has a left child
    def has_left_child(self, index):
        return self.left_child(index) < len(self.heap)

    # check if a node at a given index has a right child
    def has_right_child(self, index):
        return self.right_child(index) < len(self.heap)
       
    # heapify 
    def heapify(self, array):
        self.heap = array
        for i in range(len(self.heap) - 1, -1, -1):
            if  self.has_left_child(i):
                self.heapify_down(i)

    # heapify down
    def heapify_down(self, index):
        if not self.has_left_child(index):
            return
        smaller_child_index = self.left_child(index)
        if self.has_right_child(index): 
            if self.heap[self.right_child(index)] < self.heap[smaller_child_index]:
                smaller_child_index = self.right_child(index)
        if self.heap[index] > self.heap[smaller_child_index]:
            self.swap(index, smaller_child_index)
        if self.has_left_child(smaller_child_index):
            self.heapify_down(smaller_child_index)
    
    # heapify up
    def heapify_up(self, index):
        if self.has_parent(index): 
            parent_index = self.parent(index)
            # compare the value to its parent and swap if necessary
            if self.heap[index] < self.heap[self.parent(index)]:
                parent_index = self.parent(index)
                self.swap(index, parent_index)
                # run the code for parent                 
                if self.has_parent(parent_index):
                    self.heapify_up(parent_index)
    
    # insert into heap
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(self.size() - 1)

    # extract min from heap
    def extract_min(self):
        min = self.heap[0]
        if self.size() == 1:    
            self.heap = []
            return min
        self.heap[0] = self.heap[-1] 
        self.heap.pop()
        self.heapify_down(0)
        return min
    
    # peek
    def peek(self):
        return self.heap[0]

class PriorityQueue(MinHeap):
    # use methods from MinHeap Class
    def __init__(self):
        super().__init__()
        
    def insert(self, value, priority):
        super().insert((priority,value))

    def extract_min(self):
        return super().extract_min()

    def peek(self):
        return super().peek() 

    # change the priority (key) of an element already in the priority queue
    def change_key(self, value, new_priority):
        # search for value
        for i in range(self.size()):
            # if value is found
            if self.heap[i][1] == value:
                # change priority
                old_priority = self.heap[i][0]
                self.heap[i] = (new_priority, value)
                # heapify after changing priority to maintain heap property.
                # we can simply call heapify but heapify_up/down is more efficient
                if new_priority < old_priority:
                    self.heapify_up(i)
                else:
                    self.heapify_down(i)
                return

# create a priority queue
priority_queue = PriorityQueue()

# tasks with priorities
tasks = [(12, 'Task1'), (15, 'Task2'), (25, 'Task3'), (16, 'Task4'), (5, 'Task5')]
# insert into priority queue
print('Insert tasks into priority queue')
for priority, task in tasks:
    priority_queue.insert(task, priority)
print(priority_queue)
print('--------------')

# change the key of Task1 from 12 to 20
print('Change priority of task1 to 20')
priority_queue.change_key('Task1', 20)
print(priority_queue)
print('--------------')

# change the key of Task1 from 20 to 2
print('Change priority of task1 to 2')
priority_queue.change_key('Task1', 2)
print(priority_queue)
print('--------------')

# peek at the new element with the highest priority(min value)
print('Top priority task')
print(priority_queue.peek()) 
print('-----------')

# top priority task is complete
priority_queue.extract_min()
print('After removing top priority task')
print(priority_queue)


"""
Time Complexity of Priority Queue
Similar to heap,

    Time Complexity for insertion: O(logn)
    Time Complexity for peek: O(1)
    Time Complexity for extract min: O(logn)

Time complexity for increase/decrease key operation depends on the search function used to find the given value. Here, we have used linear search.

Time Complexity for change key: O(n)

This marks the end of binary heaps.
"""