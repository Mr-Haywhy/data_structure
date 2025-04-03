#....................Queue Operations
# Now that we know what a queue is, let's perform a few operations on our queue.
    # is_empty - Check if the queue is empty or not.
    # peek - Return the element on the top of the queue without deleting it.

#..................Check if Queue is Empty......................#
# If we try to dequeue an element from an empty stack, we will get an error. That's why we should check if a queue is empty before removing elements.
# To check if a queue is empty, we can simply find its length. If the length is 0, we know that the queue is empty.

        # # return True if queue is empty
        # # return False if queue is not empty
        # def is_empty(self):
        #     return len(self.queue) == 0

#...................Peek the Queue..........................#
# The peek() operation returns the queue's first element without removing it.
# To access the first element of a list, we can use 0 as an index.
# 
        # queue = []

        # # add items
        # queue.append(10)
        # queue.append(20)
        # queue.append(30)

# get queue's first element
        # print(queue[0])   # 10
# Thus, our peek() operation can simply return the element at index 0 if the queue is not empty.

        # # function to peek the queue
        # def peek(self):
        #     if not self.is_empty():
        #         return self.queue[0]


class Queue:
    def __init__(self):
        self.queue = []
        
    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            self.queue.pop(0)

    # method to peek the queue
    def peek(self):
       if not self.is_empty():
           return self.queue[0]

    def print_queue(self, message):
        print(f"{message}: {self.queue}")

# initializes queue attribute to an empty list
queue1 = Queue()

# add elements to the queue
queue1.enqueue(5)
queue1.enqueue(10)
queue1.enqueue(100)

# print queue
queue1.print_queue("Queue after adding 3 elements")

# dequeue first element'
queue1.dequeue()

# print after dequeue
queue1.print_queue("Queue after removing 1 element")

# peek the queue
print(f"Peek the queue:{queue1.peek()}")

# print queue   
queue1.print_queue("Queue after peeking")