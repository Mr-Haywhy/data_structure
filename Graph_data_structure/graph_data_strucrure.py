"""
~ Introduction
A graph is a collection of nodes (vertices) that are interconnected with other nodes with the help of links (also called connections or edges).

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.1.1.png

~ Real-Life Analogy
Consider the following air route of a certain airline.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.1.2.png

In the above figure, the vertices represent cities, and the edges show how they are linked.

This graph helps us see which cities are connected by air routes.

Now, let's look at the formal definition of a graph.

~ Formal Definition of a Graph
A graph is an object consisting of two sets:
    * Vertex set (V)
    * Edge set (E)

Mathematically, a graph is defined as G(V, E) where
    1 V - set of vertices
    2 E - set of edges

For example,
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.1.3.png

Here,
    Vertex Set(V):  1, 2, 3, 4
    Edge Set(E): (1, 2), (1, 3), (2, 3), (3, 4)

NOTE: A graph must consist of at least a single vertex, but it is allowed to have no edges.

Now, let's learn about some graph terminologies to better understand the data structure.

~ Introduction to Graph Terminologies
In this lesson, we will learn about the following graph terminologies:
    * Edge
    * Undirected Graph
    * Directed Graph
    * Relationship Between Vertices and Edges
    * Degree of a Vertex in an Undirected Graph
    * Degree of a Vertex in a Directed Graph
    * Weighted Graph
    * Skeins
    * Graph Representation

These terminologies are fairly simple, so we will just breeze through them.

~ Edge
The link between any two vertices is called an edge. There are two types of edges:
    * Undirected edge
    * Directed edge

~* Undirected Edge
An undirected edge represents a bidirectional relationship between two vertices.

It means that there's no specific direction or order between the two connected vertices. So, undirected edges are represented using lines with no arrowheads.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.1.png

In the above graph, we can traverse from A to B and B to A.

A real-life example would be two-way streets where you can travel in both directions.

~* Directed Edge
It represents a one-directional relationship between two vertices.

It has a starting vertex and an ending vertex. So, they are represented using arrowheads pointing from the starting vertex to the end vertex.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.2.png

In the above graph, we can traverse from A to B but not from B to A.

For example, a one-way route that only allows you to travel in a single direction.

NOTE: Edges needn't always be straight lines. For example, when representing maps with graphs, we use curved lines as edges to better illustrate the nature of the path.


~* Undirected Graphs
An undirected graph is a type of graph where all the edges are undirected.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.3.png

~* Directed Graph
If all the edges of a graph are directed, it is called a directed graph.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.4.png

NOTE: A directed graph is also called a digraph.

~ Relationships Between Vertices and Edges
The relationship between vertices and edges can be defined as one of the following:
    * Incident Edge
    * Adjacent Edge
    * Adjacent Vertex

~ Incident Edge
An edge is incident to a vertex if the edge is connected to the vertex.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.5.png

In the figure:
    * e1 is incident on x and y
    * e2 is incident on y and z
    * e3 is a self-loop and is incident on z only

~ Incident Edge on Directed Graph
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.6.png

In the figure:
    * e1 is incident on y and incident from x
    * e2 is incident on y and incident from z
    * e3 is a self-loop. So, it is incident on z from z

~ Adjacent Vertex
Two vertices sharing a common edge are called adjacent vertices.

Adjacent Vertex in an Undirected Graph
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.7.png

In the figure, the adjacent vertices are
    * x and y (connected by e1)
    * y and z (connected by e2)

Adjacent Vertex in a Directed Graph
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.8.png

In the figure:
    * x is adjacent to y and y is adjacent from x
    * z is adjacent to y and y is adjacent from z

~ Adjacent Edges
Two edges with a common vertex are called adjacent edges.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.9.png

In the figure, e1 and e2 are adjacent edges as they are both incident on y.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.10.png

Similarly, e1 and e2 are adjacent edges in directed graphs because they are both incident on y.

NOTE: Two edges that are incident from the same vertex are also adjacent.

~ Isolated Vertex
If no edge is incident on a vertex, then the vertex is called an isolated vertex.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.11.png

In the figure, p is an isolated vertex.

Similarly, if no edge is incident to or incident from a vertex in a directed graph, it is called an isolated vertex.

~ Degree of a Vertex in an Undirected Graph
The degree of a vertex is the number of edges connected to it.

Consider the graph below:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.12.png

Here, the degree of vertex 1 is 2 because two edges are connected to it.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.13.png

Similarly,
    * the degree of vertex 2 is 2
    * the degree of vertex 3 is 3
    * the degree of vertex 4 is 1
    * the degree of vertex 5 is 0


~ Degree of a Vertex in a Directed Graph
In a directed graph, the degree of a vertex is divided into two types:
    *Indegree: Represents the number of incoming edges to a vertex.
    * Outdegree: Represents the number of outgoing edges from a vertex.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.14.png

Vertex	Indegree	Outdegree
    1	    1	    1
    2	    1	    1
    3	    1	    2
    4	    1	    0
    5	    0	    0

    
~ Weighted Graph
A weighted graph is a type of graph in which each edge is associated with a numerical value called weight.

The weight represents a cost, distance, or some other metric that quantifies the relationship between the connected vertices. For example,
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.15.png

The graph above is a weighted graph where each edge is assigned a weight.

~ Skeins
A skein is a graph consisting of two vertices connected by two or more edges.

The first five skeins are shown in the figure below:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.16.png

~ Graph Representation
Let's take a moment to revise what we have learned until now.

We started by defining graphs as a collection of interconnected vertices and also came up with a formal definition of a graph as G(V, E).

We've understood them through diagrams, learned about their directed, undirected, and weighted types, and delved into the relationships between their elements.

However, we cannot rely on diagrams in programming. Instead, we need mathematical models to represent graphs. In our Python course, we will focus on two primary representations:
    * Adjacency Matrix
    * Adjacency List
    
In the next lesson, we'll look at adjacency matrices and see how we can implement them in Python.


~ Adjacency Matrix
` Introduction
An adjacency matrix is a matrix of zeros and ones used to represent a graph.

Let's start by looking at the adjacency matrix of an undirected graph:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.3.1.png

Here,
    * Zeros are used to represent the absence of an edge.
    * Ones are used to represent the presence of an edge.

~ Adjacency Matrix of an Undirected Graph
This is the adjacency matrix we created before:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.3.1.png

Now, let's consider the following element:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.3.2.png

The diagram above represents the connection between A and A. Since there's no path connecting A to A, its value is set to 0.

Similarly, consider this element in the matrix.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.3.3.png

This represents the connection between vertex B and vertex C. Since there's an edge connecting these two vertices, its value is set to 1.

Remember: For a graph with n vertices, an adjacency matrix has a dimension n x n.

~ Formal Definition of Adjacency Matrix
For a graph G = (V, E) with n vertices, the adjacency matrix A is the n x n matrix given by:

    * a_ij_ = 1 if vertices v_i and v_j are adjacent
    * a_ij_ = 0 if vertices v_i and v_j are not adjacent

Here,

    * a_ij_: element of adjacent matrix at ith row and jth column
    * v: individual vertex

Adjacent vertices refer to two vertices in a graph that are directly connected by an edge.

NOTE: Keep in mind that in an undirected graph, if the element a_ij_ is 1 then element a_ji_ is also 1.

Adjacency Matrix of a Directed Graph
So far, we have only described the adjacency matrix of undirected graphs.

The adjacency matrix of a directed graph is quite similar to that of an undirected graph with one key difference: we also need to take the direction into account.

In the case of a directed graph, we fill the matrix as 
    * a_ij_ = 1, if an edge is present from vertices v_i_ to v_j_ (not from v_j_ to v_i_)

    * a_ij_ = 0, if an edge is not present from vertices v_i_ to v_j_
​
~ Adjacency Matrix of a Directed Graph
Let us look at the following example:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.3.4.png

In an adjacency matrix, rows symbolize the starting vertices, and columns represent the ending vertices. So, an element in the row A and column B indicates a directed connection from vertex A to vertex B.

Notice that we have only set the edge values to 1 in positions where the direction matches the position.

For instance, as there's a directed edge from vertex A to vertex D, the matrix element at the intersection of the row A and column D is set to 1.

Conversely, as there is no edge directed from D to A, the element in the row D and column A remains 0, signifying the absence of a direct connection in that direction.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.3.5.png

~ Adjacency Matrix of a Weighted Graph
When writing the adjacency matrix of a weighted graph, we can simply replace the 1's with the weight values of the edge.

Let's look at an example.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.3.6.png

~ Thought Process: Adjacency Matrix
Now that we know how adjacency matrices work, let's try implementing a graph using an adjacency matrix.

Let's break down the implementation of a graph using an adjacency matrix in the following steps:
    1 Create the Graph class
    2 Add edges
    3 Display the matrix


~ Thought Process: Create the Graph Class
We will create a class named Graph with the following attributes:
    * num_vertices: represents the number of vertices in the graph
    * adj_matrix: the adjacency matrix

NOTE: For a graph with n vertices, our adjacency matrix will be of size n x n. However, we will start our graph vertex from 1 instead of 0 to make things more intuitive. Thus, our graph will be of size (n+1) x (n+1).

    class Graph:
        def __init__(self, num_vertices):
            self.num_vertices = num_vertices
            self.adj_matrix = [[0] * (num_vertices + 1) for _ in range(num_vertices + 1)]

~ Thought Process: Add Edges
If there exists a directed edge between i and j vertices, we update a_ij_ to 1.

    def add_edge(self, from_vertex, to_vertex):
        # add edge from source to destination
        self.adj_matrix[from_vertex][to_vertex] = 1

In the case of an undirected graph, we have to add an edge from the destination vertex to the source vertex too.

    def add_edge(self, from_vertex, to_vertex, is_directed = False):
        # add edge from source to destination
        self.adj_matrix[from_vertex][to_vertex] = 1

        if not is_directed:
            # add edge from destination to source (undirected graph)
            self.adj_matrix[to_vertex][from_vertex] = 1

NOTE: In the case of a weighted graph, we simply replace 1 with the weight of the edge.

This is the final code that can handle both the directed and the weighted graph. By default, we assume the graph to be undirected and unweighted.

    def add_edge(self, from_vertex, to_vertex, is_directed = False, weight = 1):
        self.adj_matrix[from_vertex][to_vertex] = weight
        if not is_directed:
            self.adj_matrix[to_vertex][from_vertex] = weight

            
~ Thought Process: Display the Matrix
Now let's add a final method for displaying the adjacency matrix.

    def print_adj_matrix(self):
        # skip first row and columns
        for row in self.adj_matrix[1:]:
            print(" ".join(map(str, row[1:])))

Here, we have skipped the first row and column because our vertex numbering starts from 1.
"""

# Source Code
# Now, let's combine everything we have done so far to build a working program.

# define Graph class
class Graph:

    # initialize class attributes
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * (num_vertices + 1) for _ in range(num_vertices + 1)]
        
    # method to add edge
    def add_edge(self, from_vertex, to_vertex, is_directed = False, weight = 1):
        self.adj_matrix[from_vertex][to_vertex] = weight
        if not is_directed:
            self.adj_matrix[to_vertex][from_vertex] = weight

    # method to display adjacency matrix
    def print_adj_matrix(self):
        for row in self.adj_matrix[1:]:
            print(" ".join(map(str, row[1:])))

"""
NOTE: This code gives no output because we haven't inserted any graph into the code.

This is the required program. Now, let's use this to create an adjacency matrix for different types of graphs.
"""

"""
~ Example: Undirected Graph
Consider the following graph:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.3.12.png

Let's create an adjacency matrix for the above graph and visualize it:

    num_vertices = 4
    graph = Graph(num_vertices)
        
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
        
    graph.print_adj_matrix()

~   Output:
        0 1 1 1
        1 0 1 0
        1 1 0 0
        1 0 0 0

        
~ Example: Directed Graph
Consider the following graph:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.3.13.png

Let's create an adjacency matrix for the above graph and visualize it:

    # create a graph
    num_vertices = 4
    graph = Graph(num_vertices)
        
    graph.add_edge(1, 2, is_directed = True)
    graph.add_edge(3, 1, is_directed = True)
    graph.add_edge(1, 4, is_directed = True)
    graph.add_edge(2, 3, is_directed = True)
    graph.add_edge(2, 4, is_directed = True)
        
    graph.print_adj_matrix()

~   Output:
        0 1 0 1
        0 0 1 1
        1 0 0 0
        0 0 0 0

~ Example: Weighted Graph
Consider the following graph:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.3.14.png

Let's create an adjacency matrix for the above graph and visualize it:

    num_vertices = 4
    graph = Graph(num_vertices)
        
    graph.add_edge(1, 3, weight = 3)
    graph.add_edge(3, 4, weight = 7)
    graph.add_edge(1, 4, weight = 5)
    graph.add_edge(2, 4, weight = 42)
        
    graph.print_adj_matrix()
    
~   Output:
        0 0 3 5
        0 0 0 42
        3 0 0 7
        5 42 7 0
"""


"""
~ Implement a Graph
Write a program to implement the graph shown in figure below using an adjacency matrix.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.3.15.png

    * Define a function named add_edge() that adds edges with weights. Also, define a function named print_adj_matrix() that displays the adjacency matrix of the graph.
    * Implement the above graph using an adjacency matrix.

Expected Output:
    0 0 0 0 2
    4 0 0 4 0
    5 0 0 0 0
    0 0 0 0 0
    0 0 7 2 0
"""

# define Graph class
class Graph:

    # initialize class attributes
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * (num_vertices + 1) for _ in range(num_vertices + 1)]
        
    # method to add edge
    def add_edge(self, from_vertex, to_vertex, is_directed = False, weight = 1):
        self.adj_matrix[from_vertex][to_vertex] = weight
        if not is_directed:
            self.adj_matrix[to_vertex][from_vertex] = weight

    # method to display adjacency matrix
    def print_adj_matrix(self):
        for row in self.adj_matrix[1:]:
            print(" ".join(map(str, row[1:])))

# create a graph
num_vertices = 5
graph = Graph(num_vertices)
    
graph.add_edge(1, 5, is_directed = True, weight= 2)
graph.add_edge(2, 4, is_directed = True, weight= 4)
graph.add_edge(5, 4, is_directed = True, weight= 2)
graph.add_edge(2, 1, is_directed = True, weight= 4)
graph.add_edge(5, 3, is_directed = True, weight= 7)
graph.add_edge(3, 1, is_directed = True, weight= 5)


graph.print_adj_matrix()