# #..............Introduction.......................#
# The queue that we've been learning so far is known as a linear queue. It's called linear because the insertion and the deletion are done from two ends.

# We will learn about four types of queues.
    # Linear Queue
    # Circular Queue
    # Priority Queue
    # Double-Ended Queue (Deque)
# We used lists to learn about linear queues. Linear queues have certain drawbacks.

# This lesson will be dedicated to exploring some of these drawbacks

#...................Drawbacks of Linear Queue
# In a linear queue we:
    # enqueued an element using append()
    # dequeued an element pop(0)
# 
# While it is easy to implement, it is inefficient.
# In linear queues, once an element is dequeued, its space is not utilized again. Over time, this leads to a waste of memory.
# Our queue implementation had an infinite size. However, it is not possible to have an infinite size in practice. So, let's assume a fixed-size linear queue of size 6.
# 
        # {5, 16, 12, 20, 23, 26}
        # {0,  1,  2,  3,  4,  5}
# 
# Let's dequeue some of the elements of the queue.
# 
        # { ,   ,   , 20, 23, 26}
        # {0,  1,  2,  3,  4,  5}
# 
# Here, we removed elements in index 0, 1, and 2. The queue now has vacant spaces in these three indexes, yet we can't insert any more elements to this queue.
# This makes linear queues inefficient. In large queues, such inefficiency can cause detrimental effects.
# A reliable way to fix the space utilization problem is by using a circular queue.