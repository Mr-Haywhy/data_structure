'''
~ Introduction
Dijkstra's Algorithm is a path-finding algorithm that solves single source shortest path problems.

But what is a single source shortest path problem?

Imagine you're using a GPS device to find the shortest route from your home to a distant city. You enter your starting point (your home) and your destination (the distant city) into the GPS device.

Dijkstra's Algorithm can be used to compute the shortest path from the start to the destination.

This algorithm traverses through various possible routes, selecting the shortest path at each step, and ultimately providing you with a route that has the minimum distance or travel time.

Because we are finding the shortest path, this is a minimization problem.

Now, let's use this algorithm to find the shortest path between two points.

~ Working of Dijkstra's Algorithm
Consider the weighted graph below.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.3.1.png

Let's say we have to travel from vertex A to one of the other vertices.

As you can see, there are multiple paths available and each path is given a weight (let's say distance).

Here, vertex A is called the source vertex.

Our goal is to find the minimum cost to reach every vertex from the source.

So, we'll use Dijkstra's algorithm to find the optimal shortest path.

NOTE: Dijkstra's algorithm calculates the shortest paths from a selected source vertex to all other vertices. Thus, we only select the destination vertex after we've acquired the results of the algorithm.

~ Step I: Initialize the Distances
First, we'll update the distance required to reach each vertex from the source vertex with an initial value by using the conditions below:
    * The distance from the source vertex to itself is set to zero.
    * The distance from the source vertex to every other vertex is set to infinity.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.3.2.png

We also need to initialize a list to keep track of the unvisited vertices. Since we start at vertex A, we mark it as visited.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.3.3.png

~ Step II: Check the Adjacent Vertices
After processing the source vertex, we move on to its adjacent unvisited vertices.

First, we update the distance to reach the vertices with the cost of the adjacent edge.

So, the updated cost to reach vertex B is 4. As per our graph, the updated cost for reaching vertex C is also 4.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.3.4.png

However, this is not the final value since there might be alternative paths that provide a shorter route.

~ Step III: Check Alternative Paths to the Vertices
Some vertices can have multiple paths. Checking alternative paths of each vertex is important because we don't know which path results in the minimum distance traveled.

Check Alternative Paths for Vertex B

Since there are no alternative paths to reach B, we simply
    * mark B as visited, and
    * accept 4 as the minimum distance required to reach B from A.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.3.5.png

Check Alternative Paths for Vertex C

However, there are two possible paths to reach C from a vertex whose shortest path is known. In our case, these vertices with known shortest paths are A and B:
    * Route A -> C with cost 4
    * Route A -> B -> C with cost 6 (4 + 2)
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.3.6.png

Our goal is a shorter path, so we prefer the path with distance 4 to that of distance 6.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.3.7.png

Next, we will update the other vertices that are connected to vertex A, B and C.

~ Step IV: Update the Other Vertices
Now, we update the remaining vertices that are connected with the vertices with value.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.3.8.png

In the graph, all the remaining vertices are connected to vertex C. So, we can update all the remaining distances from vertex C instead of vertex A.

Notes:
    * If we can reach a vertex from C, we can reach it from A.
    * Distance of a vertex from A = (Distance of the vertex from C) + 4

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.3.9.png
Now, let's check if they have any alternative paths.

~ Step V: Check for Alternative Paths
Once again, we need to check the distance of alternative paths. This ensures that we are choosing the path with the shortest distance.

Since vertex D and vertex E are already adjusted to the shortest possible path from vertex A, their assigned weights can no longer be changed.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.3.10.png

So, we only need to check the shortest path for vertex F.

We have three possible paths to reach vertex F, each with varying costs:
    * Path A -> C -> F: 10 (4 + 6)
    * Path A -> C -> D -> F: 9 (4 + 3 + 2)
    * Path A -> C -> E -> F: 8 (4 + 1 + 3)

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.3.11.png

Here, the shortest path is the path with distance 8. So, let's update the vertex F with a weight of 8.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.3.12.png

With this, we have found the shortest path from the starting vertex A to every other vertex in the graph.

So, if we had to find the shortest path from A to any other node, we just follow along the purple lines that lead to that vertex starting from A.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.3.13.png

From the figure, A -> C -> E -> F is the shortest path from vertex A to F with distance 8.

Similarly, the path from A to D will be A -> C -> D with a path cost of 7.

NOTE: Dijkstra's algorithm is a single source shortest path algorithm. This algorithm finds the shortest path to all vertices from any given vertex. The destination vertex is chosen after the completion of the algorithm.

Now that we know how Dijkstra's Algorithm works, we will implement it in Python. Before we jump into the Python code, however, you'll be taking a short quiz.
'''

'''
~ Thought Process: Dijkstra's Algorithm
1. Initialize the shortest distances and predecessors.
Set the shortest known distance for all vertices to infinity and the start vertex to 0. Initialize all predecessors to None.

        shortest_distance = {vertex: float('infinity') for vertex in graph}
        shortest_distance[start] = 0
        predecessor = {vertex: None for vertex in graph}

Here, the predecessor dictionary will help us track which path we took to get the shortest distance by providing us the vertex that came just before the current vertex in the path.

2. Define the unvisited vertices list.
Create a list of all vertices that have not been visited yet.

        unvisited_vertices = list(graph)

3. Select the vertex with the minimum distance.
As long as there are unvisited vertices, choose the one with the smallest known distance as the current_vertex.

        current_vertex = min(unvisited_vertices, key=lambda vertex: shortest_distance[vertex])

4. Update the distances for the neighbors.
For each neighbor of the current vertex, if the new path through the current vertex is shorter, update the shortest distance and set current_vertex as the predecessor.

        for neighbor, weight in graph[current_vertex].items():
            if shortest_distance[current_vertex] + weight < shortest_distance[neighbor]:
                shortest_distance[neighbor] = shortest_distance[current_vertex] + weight
                predecessor[neighbor] = current_vertex

We have set the current_vertex as the predecessor of its adjacent vertices because the current vertex will come before them in the shortest path. We will update this if we find a shorter alternative.

5. Mark the current vertex as visited.
After evaluating all neighbors, remove the current vertex from the list of unvisited vertices.

        unvisited_vertices.remove(current_vertex)

6. Reconstruct the shortest path.
Once all vertices are visited, trace back from the destination vertex using the predecessor dictionary to form the shortest path.

        path = []
        while end:
            path.append(end)
            end = predecessor[end]
        path.reverse()
'''

# Source Code: Dijkstra's Algorithm
# define the graph
graph = {
    'A': {'B': 4, 'C': 4},
    'B': {'A': 4, 'C': 2},
    'C': {'A': 4, 'B': 2, 'D': 3, 'E': 1, 'F': 6},
    'D': {'C': 3, 'F': 2},
    'E': {'C': 1, 'F': 3},
    'F': {'C': 6, 'D': 2, 'E': 3},
}

def dijkstra(graph, start, end):
    
    # set initial distance for all to infinity
    # set initial distance for starting vertex to 0
    shortest_distance = { vertex : float('infinity') for vertex in graph}
    shortest_distance[start] = 0
    
    # define predecessor
    predecessor = { vertex : None for vertex in graph}

    # define unvisited vertices
    unvisited_vertices = list(graph)

    while unvisited_vertices:
        
        # select the vertex with the smallest distance value from the list of unvisited vertices
        current_vertex = min(unvisited_vertices, key=lambda vertex: shortest_distance[vertex])
        # visit all adjacent vertices of the current vertex and update the shortest distances if needed
        for neighbor, weight in graph[current_vertex].items():
            if shortest_distance[current_vertex] + weight < shortest_distance[neighbor]:
                shortest_distance[neighbor] = shortest_distance[current_vertex] + weight
                predecessor[neighbor] = current_vertex

        # mark the current vertex as visited
        unvisited_vertices.remove(current_vertex)
    # reconstruct the path from end to start by backtracking from the end using the predecessor dictionary
    path = []
    while end:
        path.append(end)
        end = predecessor[end]
    path.reverse()
    return shortest_distance, path

# function call         
                        # input_string = input()
start, end = 'A', 'F'   # start, end = input_string.split()
distance, path = dijkstra(graph, start, end)
print(f"Shortest path from {start} to {end}: {path}")
print(f"Shortest distance from {start} to {end}: {distance[end]}")

'''
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.3.14.png

Output:
    Shortest path from A to F: ['A', 'C', 'E', 'F']
    Shortest distance from A to F: 8
'''

"""
~ Time complexity: O(V^2)

In this lesson, we have used a simplified version of Dijkstra that has higher time complexity. The optimized code for Dijkstra's algorithm has a complexity of O(E + V log V).

Where,
    * V is the number of vertices.
    * E is the number of edges.
"""