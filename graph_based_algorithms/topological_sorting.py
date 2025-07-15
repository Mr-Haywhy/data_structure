'''
~ Introduction
Topological sorting works with a specific type of graph known as 'Directed Acyclic Graphs (DAG)'. So, before jumping into the algorithm, let's first learn about DAG.

* Directed Acyclic Graphs (DAG)
Directed Acyclic Graphs are graphs that have directed edges and no cycles.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.2.1.png

In the above figure, we can see that there are no cycles, which means there's no possibility of a closed path.

~ Topological Sort
This algorithm processes directed acyclic graphs and produces an array of its vertices. In this array, each vertex is positioned before all the vertices it directs to, starting from a vertex with indegree 0.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.2.2.png

So, the topological sort for this graph is [B, E, A, C, D].
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.2.3.png
As you can see, the vertices are sorted such that all edges are directed forward. This is topological sorting.

~ Real-Life Analogy
Imagine you're a student at a university, and you have a set of courses you need to complete to earn a degree.

Some courses have prerequisites, meaning you must complete one course before you can take another.

For example:
    * Introduction to Programming must be taken before Data Structures.
    * Data Structures must be taken before Algorithms.
    * Calculus I must be taken before Calculus II.
More dependencies are shown in the graph diagram.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.2.4.png

In this scenario,
    * the courses represent vertices
    * the prerequisites represent directed edges
The goal is to find an order in which you can take all the courses such that you always satisfy the prerequisite conditions.

A topological sort would give an ordering like:
    1. Maths
    2. Introduction to Programming
    3. Calculus I
    4. Data Structures
    5. Calculus II
    6. Algorithms
    7. Compiler Design

This is how it looks in graph:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.2.5.png

This order ensures that you never take a course before its prerequisites.

~ Working of Topological Sort
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.2.6.png

Let's try and find the topological sort of this graph.

We can break down the working of topological sort in the following steps:
    1. Process vertices with zero indegree.
    2. Find the vertices with indegree zero.
    3. Repeat steps 1 and 2 until all vertices have been visited.

~ Find the Vertices With Indegree Zero
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.2.7.png

The first step is to find every vertex with indegree 0.

This is because if any vertex has incoming directed edges, the vertices the edge originates from should be processed first.

~ Process Nodes With Zero Indegree
    * Add the vertex with indegree zero to a list of sorted vertices.
    * Remove the vertex from the graph.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.2.8.png

Once a vertex is added to the list, we can take the vertex and its outgoing edges out of the graph.

Repeat Steps 1 and 2 Until All Vertices Have Been Visited
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.2.9.png

To compensate for the removal, we decrease the indegree of each of its outgoing vertices by one.

So now that we have removed B from the graph, we have decreased the indegree of E and C by one.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.2.10.png

Since E is the only vertex with an indegree zero, we add E to the topological sort list and remove it along with its outgoing edges.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.2.11.png

The same process continues until we have no vertices to process.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.2.12.png
'''

'''
~ Thought Process: Topological Sort
Now that we know the working of the topological sort algorithm, let's try and implement it in Python.

1. Define the function for topological sort.
We take an input graph and also define a list named sorted_vertices to keep track of the sorted vertices.

        def topological_sort(graph, sorted_vertices=None):
            if sorted_vertices is None:
                sorted_vertices = []

Initially, sorted vertices are empty because no vertices have been sorted.

* Base Case
2. Define the base case.

If the number of sorted vertices is equal to the number of vertices in the graph, all the vertices have been sorted and the process ends.

        if len(sorted_vertices) == len(graph):
            return [vertices[i] for i in sorted_vertices]

* Recursive Case
3. Find vertices with zero indegree.

        indegrees = [sum(col) for col in zip(*graph)]
        zero_indegrees = [i for i, indegree in enumerate(indegrees) if indegree == 0]

4. Append the zero_indegrees list to the sorted list.

        sorted_vertices.extend([i for i in zero_indegrees if i not in sorted_vertices])

5. Remove the zero indegree vertices.

        new_graph = [row[:] for row in graph]
        for i in zero_indegrees:
            new_graph[i] = [0] * len(new_graph[i])

6. Recursively sort the graph.

        return topological_sort(new_graph, sorted_vertices)

'''

# Source Code:

vertices = ['A', 'B', 'C', 'D', 'E']  
adj_matrix = [
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0]
]

def topological_sort(graph, sorted_vertices=None):

    if sorted_vertices is None:
        sorted_vertices = []
    
    # base case
    if len(sorted_vertices) == len(graph):
        return [vertices[i] for i in sorted_vertices]
    
    # find indegree of all vertices
    indegrees = [sum(col) for col in zip(*graph)]

    # find the vertices with indegree zero
    zero_indegrees = [i for i, indegree in enumerate(indegrees) if indegree == 0]
    
    # append the zero indegree list to sorted
    sorted_vertices.extend([i for i in zero_indegrees if i not in sorted_vertices])
    
    # remove the zero indegree vertices
    # create a copy of the graph to avoid modifying the input
    new_graph = [row[:] for row in graph]
    # remove the zero indegree vertices
    for i in zero_indegrees:
        new_graph[i] = [0] * len(new_graph[i])
    
    
    # sort the new graph
    return topological_sort(new_graph, sorted_vertices)

print(topological_sort(adj_matrix))


'''
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.2.13.png
Output:
    ['B', 'E', 'A', 'C', 'D']
'''

'''
Time complexity: O(V^3)

The code we've used is a simplified version of topological sort and has higher time complexity. The optimized code for topological sort has a complexity of O(V+E).

Here,
    * V is the number of vertices
    * E is the number of edges
'''