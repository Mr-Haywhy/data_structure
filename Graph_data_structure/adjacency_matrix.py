"""
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