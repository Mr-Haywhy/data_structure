"""
~ Introduction
Adjacency list is a linked list representation of a graph. It specifies vertices that are adjacent to a vertex. For example,
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.4.1.png

Here, the adjacent vertices of each vertex are:

Vertex	Adjacent Vertices
    1	    3, 4
    2	    4
    3	    1, 4
    4	    1, 2, 3

Now, let's create an adjacency list using this information.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.4.2.png

Thus, an adjacency list is a linked list representation of adjacent vertices.

~ Adjacency List of a Directed Graph
In order to write an adjacency list of a directed graph, we need to take the direction of edges into account.

Let's look at an example.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.4.3.png

Now, let's create the adjacency list from the above information.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.4.4.png


~ Adjacency List of a Weighted Graph
To represent a weighted graph using adjacency list, we add the weight value in the linked list representation.

Let's look at an example.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.4.5.png

The adjacent vertices in the above graph (along with their weights) are:

Vertex	|   Adjacent Vertices (Weights)
    1	|       3(3), 4(5)
    2	|       4(42)
    3	|       1(3), 4(7)
    4	|       1(5), 2(42), 3(7)

Now, let's create a simple adjacency list (without weights) from the above information.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.4.6.png

The above adjacency list is missing the information about weights of the edges.

Now, let's add a separate box (space) for the weights in the linked list.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.4.7.png

Thus, the adjacency list representation of the weighted graph is complete.

~ Thought Process: Adjacency List
The thought process for implementing a graph using an adjacency list is similar to that of an adjacency matrix.

Let's break down the implementation of a graph using an adjacency list with the following steps:
    1. Create the Graph class
    2. Add edge
    3. Display the list


** Step I: Create the Graph Class
The Graph class has two attributes: num_vertices and adj_list, representing the number of vertices and the adjacency list respectively.

We have initialized adj_list as a list of empty lists with a size of (num_vertices + 1) to allow vertex numbering to start from 1, making it more intuitive.

NOTE: Here, we have used a list of lists to represent an adjacency list for the sake of simplicity, although adjacency lists are theoretically implemented using linked lists.
    class Graph:
        def __init__(self, num_vertices):
            self.num_vertices = num_vertices

            # initialize a list of empty lists for each vertex
            # use a (num_vertices + 1) sized list to allow
            # vertex numbering to start from 1
            self.adj_list = [[] for _ in range(num_vertices + 1)]


*** Step II: Add the Edges
Similar to the adjacency matrix, we will account for both the direction and the weight of the edges in the graph.

        def add_edge(self, vertices, is_directed = False, weight = None):
            
            from_vertex, to_vertex = vertices
            
            # weighted
            if weight:
                self.adj_list[from_vertex].append((to_vertex, weight))
                if not is_directed:
                    self.adj_list[to_vertex].append((from_vertex, weight))
                
            # unweighted    
            else:
                self.adj_list[from_vertex].append(to_vertex)
                if not is_directed:
                    self.adj_list[to_vertex].append(from_vertex)


*** Step III: Display the List
Now, let's add a method to display the adjacency list.

    def print_adj_list(self):
        for i in range(1, self.num_vertices + 1):
            print(f"{i} ->", " -> ".join(map(str, self.adj_list[i])))

In this method, we iterate through each vertex, and for each vertex, we display its adjacency list.
""" 

# Source Code
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices + 1)]

    def add_edge(self, vertices, is_directed = False, weight = None):
        from_vertex, to_vertex = vertices
        # weighted
        if weight:
            self.adj_list[from_vertex].append((to_vertex, weight))
            if not is_directed:
                self.adj_list[to_vertex].append((from_vertex, weight))
            
        # unweighted    
        else:
            self.adj_list[from_vertex].append(to_vertex)
            if not is_directed:
                self.adj_list[to_vertex].append(from_vertex)

    def print_adj_list(self):
        for i in range(1, self.num_vertices + 1):
            print(f"{i} ->", " -> ".join(map(str, self.adj_list[i])))


"""
Example: Undirected Graph
Consider the following graph:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.4.13.png

Let's create an adjacency list for the above graph and visualize it:
"""

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices + 1)]

    def add_edge(self, vertices, is_directed = False, weight = None):
        from_vertex, to_vertex = vertices
        # weighted
        if weight:
            self.adj_list[from_vertex].append((to_vertex, weight))
            if not is_directed:
                self.adj_list[to_vertex].append((from_vertex, weight))
            
        # unweighted    
        else:
            self.adj_list[from_vertex].append(to_vertex)
            if not is_directed:
                self.adj_list[to_vertex].append(from_vertex)

    def print_adj_list(self):
        for i in range(1, self.num_vertices + 1):
            print(f"{i} ->", " -> ".join(map(str, self.adj_list[i])))

# create a graph
num_vertices = 4
graph = Graph(num_vertices)
graph.add_edge((1, 4))
graph.add_edge((1, 3))
graph.add_edge((2, 4))
graph.add_edge((3, 4))

# display the adjacency list
graph.print_adj_list()


"""
Example: Directed Graph
Consider the following graph:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.4.14.png

Let's create an adjacency list for the above graph and visualize it:
"""

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices + 1)]

    def add_edge(self, vertices, is_directed = False, weight = None):
        from_vertex, to_vertex = vertices
        # weighted
        if weight:
            self.adj_list[from_vertex].append((to_vertex, weight))
            if not is_directed:
                self.adj_list[to_vertex].append((from_vertex, weight))
            
        # unweighted    
        else:
            self.adj_list[from_vertex].append(to_vertex)
            if not is_directed:
                self.adj_list[to_vertex].append(from_vertex)

    def print_adj_list(self):
        for i in range(1, self.num_vertices + 1):
            print(f"{i} ->", " -> ".join(map(str, self.adj_list[i])))

# create a graph
num_vertices = 4
graph = Graph(num_vertices)
graph.add_edge((1, 4), is_directed = True)
graph.add_edge((1, 2), is_directed = True)
graph.add_edge((2, 4), is_directed = True)
graph.add_edge((2, 3), is_directed = True)
graph.add_edge((3, 1), is_directed = True)

# display the adjacency list
graph.print_adj_list()



"""
Example: Weighted Graph
Consider the following graph:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.4.15.png

Let's create an adjacency list for the above graph and visualize it:
"""

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices + 1)]

    def add_edge(self, vertices, is_directed = False, weight = None):
        from_vertex, to_vertex = vertices
        # weighted
        if weight:
            self.adj_list[from_vertex].append((to_vertex, weight))
            if not is_directed:
                self.adj_list[to_vertex].append((from_vertex, weight))
            
        # unweighted    
        else:
            self.adj_list[from_vertex].append(to_vertex)
            if not is_directed:
                self.adj_list[to_vertex].append(from_vertex)

    def print_adj_list(self):
        for i in range(1, self.num_vertices + 1):
            print(f"{i} ->", " -> ".join(map(str, self.adj_list[i])))

# create a graph
num_vertices = 4
graph = Graph(num_vertices)
graph.add_edge((1, 4), weight = 5)
graph.add_edge((1, 3), weight = 3)
graph.add_edge((2, 4), weight = 42)
graph.add_edge((4, 3), weight = 7)

# display the adjacency list
graph.print_adj_list()


"""
Implement a Graph
Write a program to implement the graph shown in figure below using an adjacency list.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.4.16.png

* Define a function named add_edge() that adds edges between vertices. Also define a function named print_adj_list() that displays the graph's adjacency list.
* Implement the above graph using an adjacency list.
"""