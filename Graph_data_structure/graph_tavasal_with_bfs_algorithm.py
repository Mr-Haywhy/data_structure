"""
Introduction
Breadth-First Search is a graph traversal algorithm that explores the graph layer by layer.

Real-Life Analogy

When you post a photo or a status update on social media, your immediate friends or followers see it first.

When they like, share, or comment on it, their friends (who might not be directly connected to you) see it, and then their friends, and so on. The post reaches people in layers of closeness to you.

The BFS algorithm works in a similar manner. It starts from a source vertex and explores all its adjacent vertices at the current depth before moving on to the vertices at the next depth level.

Working of BFS Algorithm
Let's understand the working of the BFS algorithm with the following graph.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.6.1.png

We start at vertex A.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.6.2.png

As you can see, there are three possible paths from A (B, D, and E). We then travel to all immediate neighbors of A.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.6.3.png

Working: Visit Neighbors of Visited Vertices
Previously, we started at vertex A and traveled to its neighbors B, D, and E.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.6.3.png

Now, we traverse the immediate unvisited neighbors of already-visited vertices.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.6.4.png

So far, we've visited the vertices A, B, C, D, E, G, and H.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.6.4.png

Now, we keep visiting the immediate neighbors until all possible vertices have been visited.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.6.5.png

This concludes the search process.
"""

'''
Thought Process: BFS Algorithm
Let's explore the thought process for the following graph.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.6.6.png

We will start with an empty set and an empty queue.

NOTE: Queues, with their First-In-First-Out (FIFO) approach, are well-suited for BFS as they facilitate the exploration of all neighboring vertices at the current depth level before moving on to the nodes at the next level, ensuring a level-by-level traversal.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.6.7.png

The set keeps track of visited vertices and the queue keeps track of vertices to visit.

NOTE: Similar to BFS in trees, BFS in graphs also visits the first vertex in the queue.

Step I: Start From Vertex A
We will first choose a starting vertex (A).

We insert A to the visited set and add its neighbors (B, E, D) to the queue.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.6.8.png

Since vertex B is at the front of the queue, we will now visit it.

Step II: Visit the Vertex at the Front of the Queue
Previously, our queue consisted of the following elements: ['B', 'E', 'D'].

Since vertex B is at the front of the queue, we will "visit" it by
    * inserting B into the visited set
    * removing B from the queue
    * adding its neighbors (C and E) to the queue
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.6.9.png

Step III: Traverse the Next Vertex and Repeat
Then, we will traverse vertex E and repeat the same process, and then do the same for vertex D.

This way, we have visited all the neighboring vertices of our starting vertex A.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.6.10.png

NOTE: Similar to DFS, we don't add the vertices we've already visited to the queue.

Step IV: Dequeue the Visited Vertex
Here's the set of vertices we've visited so far:

        Visited = {'A', 'B', 'E', 'D'}

And here's the queue we're using to track unvisited vertices:

        Queue = {'E', 'C', 'H', 'G'}

As you can see, the front of the queue is vertex E.

However, E has already been visited. Thus, we simply dequeue it without changing anything.

Instead,, we will visit C followed by H.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.6.11.png

Step V: Continue the Process for All Elements
To traverse the rest of the vertices, we continue the process for all elements in the queue.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.6.12.png

As no elements are remaining in the queue, we have completed our algorithm.

Now, let's try implementing it in Python.
'''

'''
Thought Process: BFS Algorithm
To implement the BFS algorithm, we can follow these steps.

1. Take a graph to traverse and choose a starting vertex.

        def bfs_traversal(adj_list, vertex):
        
2. Initialize the variables.

        traversal_seq = []
        visited = set()
        queue = [vertex]

During initialization, we create
    * A list to store the sequence of traversal.
    * A set to keep track of the visited nodes.
    * A queue to store the adjacent vertices of the current vertex.

3. Dequeue the front element and make it the current vertex.

        current_vertex = queue.pop(0)

4. If the current vertex has not been traversed,
    * Add current vertex to the traverse list.
    * Add current vertex to the visited set.
    * Push the neighbors of the current vertex to the stack if they have not been visited.

        if current_vertex not in visited:
            traversal_seq.append(current_vertex)
            visited.add(current_vertex)
            queue.extend([v for v in adj_list[current_vertex] if v not in visited])

5. Repeat steps 3 and 4 as long as the queue is not empty.

        while queue:    
'''

# Source Code
# Now let's combine what we have built so far to build a working program and visualize how it works.

# create a graph 
graph_adj_list =  {
    "A": ["B", "E", "D"],
    "B": ["A", "E", "C"],
    "C": ["B", "F"],
    "D": ["A", "G"],
    "E": ["A", "B", "H"],
    "F": ["C"],
    "G": ["D", "H"],
    "H": ["E", "G", "I"],
    "I": ["H"]
}

def bfs_traversal(adj_list, vertex):
    # initialize list to store the sequence of traversal
    traversal_seq = []
    # initialize set to keep track of visited nodes
    visited = set()
    # initialize a queue for BFS with starting vertex
    queue = [vertex]
    
    # continue as long as there are nodes to visit in the queue
    while queue:
        # dequeue a vertex from queue
        current_vertex = queue.pop(0)
        
        # if the dequeued vertex hasn't been visited, process it
        if current_vertex not in visited:
            # add vertex to traversal sequence
            traversal_seq.append(current_vertex)
            # mark the vertex as visited
            visited.add(current_vertex)
            # push the neighbors of the current vertex onto the stack 
            # if the neighbor has not already been visited
            queue.extend([v for v in adj_list[current_vertex] if v not in visited])

            print(f"Sequence: {traversal_seq}")
            print('---------------------')
    return traversal_seq

traverse = bfs_traversal(graph_adj_list, "A")
print(f"Final traversal sequence:\n{traverse}")


'''
Output: 
    Sequence: ['A']
    ---------------------
    Sequence: ['A', 'B']
    ---------------------
    Sequence: ['A', 'B', 'E']
    ---------------------
    Sequence: ['A', 'B', 'E', 'D']
    ---------------------
    Sequence: ['A', 'B', 'E', 'D', 'C']
    ---------------------
    Sequence: ['A', 'B', 'E', 'D', 'C', 'H']
    ---------------------
    Sequence: ['A', 'B', 'E', 'D', 'C', 'H', 'G']
    ---------------------
    Sequence: ['A', 'B', 'E', 'D', 'C', 'H', 'G', 'F']
    ---------------------
    Sequence: ['A', 'B', 'E', 'D', 'C', 'H', 'G', 'F', 'I']
    ---------------------
    Final traversal sequence:
    ['A', 'B', 'E', 'D', 'C', 'H', 'G', 'F', 'I']
'''

'''
Time Complexity of BFS Algorithm
The dominant factors in the time complexity of BFS are the while loop and the queue operations, which together take O(V+E) time.

Hence, the total time complexity is O(V+E).
'''