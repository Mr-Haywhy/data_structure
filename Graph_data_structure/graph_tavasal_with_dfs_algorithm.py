"""
Introduction
Graph traversal is the process of visiting every vertex (node) in a graph. It is also known as graph search.

Graph is a non-linear data structure. Therefore, there is no straightforward way to traverse a graph.

Here, we will discuss two of the possible graph traversal methods.
    * Depth-first search (DFS) method
    * Breadth-first search (BFS) method

Let's start with the DFS algorithm first, and then move on to BFS in the next lesson.

DFS Algorithm
Depth-first search (DFS) is a graph traversal algorithm that starts at a given node and goes as far as it can down a path, then backtracks until it finds an unexplored path and then explores it.

Real-Life Analogy

Imagine you're in a maze. You start walking down a path and keep going until you hit a wall or a dead-end.

When that happens, you think, "Oops! This isn't the way out."

So, you go back to the last spot where you could choose a different direction. This time, you pick a new path to see if that's the way out. You keep trying different paths, going back when you hit dead-ends, and choosing new directions.

You keep doing this until you either find the exit or realize you've tried every possible path.

That's how someone would tackle a maze, just like DFS.

Working of DFS Algorithm
Let's understand the working of the DFS algorithm with the following graph.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.5.1.png

We start at vertex A.

As you can see, there are three possible paths from A (B, D, and E). We can choose any of these paths.

Let's choose B for now and keep moving forward through C until we reach a dead end at F.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.5.2.png

Next, we'll look at what to do once we reach a dead end.

Working: Backtrack From a Dead End at F
Previously, we traversed the vertices in the following order: A->B->C->F.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.5.2.png

As there are no more forward paths from F, we backtrack to B.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.5.3.png

Working: Continue From Vertex B
Now, we have to repeat the same process again.

So, we move towards our forward path going from B, i.e., B->E->H->G->D. However, D is a dead end.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.5.4.png

NOTE: Although there is a path from D to A, we cannot use it because we have already traversed A. Thus D is a dead end.

Now, let's backtrack again.

Working: Bactrack From the Dead End at D
As before, we have to backtrack so we arrive once again at H.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.5.5.png

From H, we take the forward path leading to I and complete our traversal.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.5.6.png

Alternate Paths in DFS
We can traverse a graph in various ways using the DFS algorithm. Here's another way.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.5.7.png

Thought Process: DFS Algorithm
Let's explore the thought process for the following graph.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.5.8.png

We will start with an empty set and an empty stack.

NOTE: Stacks are ideal for DFS because they operate on a Last-In-First-Out (LIFO) principle, allowing the algorithm to dive deep into one branch of the graph before backtracking, which aligns perfectly with the exploratory nature of DFS.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.5.9.png

The set keeps track of visited vertices and the stack keeps track of vertices to visit. Let's look at the traversal step by step.

NOTE: Similar to DFS in trees, DFS in graphs also visits the last vertex in the stack first.

Step I: Start From Vertex A
We will first choose a starting vertex (A).

We insert
    * A to the visited set
    * the neighbors of A (B, E, D) to the stack.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.5.10.png

Step II: Select Vertex at the Top of the Stack
Now, we will traverse vertex D, since it is at the top of the stack.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.5.11.png

NOTE: Although A is a neighbor of D, we have already visited A. So, we do not need to insert in the stack.

Step III: Continue the Process for All Elements
We continue this process for all elements in the stack.

First, we visit G, since it is at the top of the stack.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.5.12.png

Similarly we visit other vertices in the stack.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.5.13.png

NOTE: As you can see, the stack has repeat elements. Thus, everytime we pop from the top of the stack, we should check whether the vertex has been visited or not.

This process continues.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.5.14.png

NOTE: As you can see, there are still vertices remaining in the stack. However, since the vertices in the stack have already been visited, they simply get popped from the stack without changing anything.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.5.15.png

Thus, we have completed our depth-first traversal.
"""

"""
Thought Process: DFS Algorithm
To implement the DFS algorithm, we can follow the steps below.

1. Take a graph to traverse and choose a starting vertex.

    def dfs_traversal(adj_list, vertex):
    
2. Define the variables.

Create the following:
    * an empty list to keep track of the traversal sequence
    * a set to keep track of visited nodes
    * a stack to track the vertices to visit and push the starting vertex onto it

        traversal_seq = []
        visited = set()
        stack = [vertex]

3. Pop the top vertex from the stack and make it the current vertex .

        current_vertex = stack.pop()

4. If the current vertex has not been traversed,
    * Add current vertex to traverse list.
    * Add current vertex to the visited set.
    * Push the neighbors of the current vertex to the stack if they have not been visited.

        if current_vertex not in visited:
            traversal_seq.append(current_vertex)
            visited.add(current_vertex)
            stack.extend([v for v in adj_list[current_vertex] if v not in visited)

5. Repeat steps 3 and 4 as long as the stack is not empty.

        while stack:
"""

# Source Code
# Now let's combine what we have built so far to build a working program.

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

def dfs_traversal(adj_list, vertex):
    # initialize the list to store the sequence of nodes traversed
    traversal_seq = []
    # initialize the set of visited vertices
    visited = set()
    # initialize the list of nodes to visit
    stack = [vertex]

    # continue as long as there are nodes to visit in the stack
    while stack:
        # pop the top node from the stack to visit
        current_vertex = stack.pop()
        
        # if the node hasn't been visited yet, process it
        if current_vertex not in visited:
            # add the current vertex to the traversal sequence
            traversal_seq.append(current_vertex)
            # add the current vertex to visited set
            visited.add(current_vertex)
            # push the neighbors of the current vertex onto the stack 
            # if the neighbor has not already been visited
            stack.extend([v for v in adj_list[current_vertex] if v not in visited])

            print(f"Sequence: {traversal_seq}")
            print('---------------------')
    return traversal_seq

traverse = dfs_traversal(graph_adj_list, "A")
print(f"Final traversal sequence:\n{traverse}")


'''
Output: 
    Sequence: ['A']
    ---------------------
    Sequence: ['A', 'D']
    ---------------------
    Sequence: ['A', 'D', 'G']
    ---------------------
    Sequence: ['A', 'D', 'G', 'H']
    ---------------------
    Sequence: ['A', 'D', 'G', 'H', 'I']
    ---------------------
    Sequence: ['A', 'D', 'G', 'H', 'I', 'E']
    ---------------------
    Sequence: ['A', 'D', 'G', 'H', 'I', 'E', 'B']
    ---------------------
    Sequence: ['A', 'D', 'G', 'H', 'I', 'E', 'B', 'C']
    ---------------------
    Sequence: ['A', 'D', 'G', 'H', 'I', 'E', 'B', 'C', 'F']
    ---------------------
    Final traversal sequence:
    ['A', 'D', 'G', 'H', 'I', 'E', 'B', 'C', 'F']

NOTE: Click 'visualize this button' to visualize how the traversal works.

'''

"""
Time Complexity of DFS Algorithm
The dominant factors in the time complexity of DFS are the while loop and the stack extension, which together take O(V+E) time.

Hence, the total time complexity is O(V+E).

To learn more, refer to this blog.
"""