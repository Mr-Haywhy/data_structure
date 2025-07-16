'''
~ Introduction
The Ford Fulkerson Algorithm is another algorithm that follows a greedy approach to find the optimized solution. It is primarily used for solving network flow problems.

Let's suppose we have a flow of liquid inside a network of pipes of different capacities. Each pipe has a certain capacity of liquid it can transfer at an instance.

Now, suppose you want to find out how much liquid can flow from the source to the sink at an instance. How would you do that?

Well, the Ford Fulkerson Algorithm is meant to solve such problems.

~ Ford Fulkerson Algorithm
The Ford Fulkerson Algorithm makes use of a flow network to describe a network of vertices and edges with a source (S) and a sink (T).

Each vertex, except S and T, can receive and send liquid through it. S can only send and T can only receive stuff.

Let's use the previous example of liquid flow in a network of pipes:

We have a network of pipes of different capacities that delivers liquid from source S to sink T. This network is represented by the diagram below.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.5.1.png

Let's get familiar with some common terms we will be using to solve the given problem using the Ford Fulkerson algorithm.

* Augmenting Path
It is the path available in a flow network.

* Residual Graph
It represents the flow network that has additional possible flow.

* Residual Capacity
It is the capacity of the edge after subtracting the flow from the maximum capacity.

~ Working of Ford Fulkerson Algorithm
Here's how the algorithm works:
    1. First, initialize the flow in all the edges to 0.
    2. If there is an augmenting path between the source and the sink, add this path to the flow network.
    3. Update the residual graph.

If you can't understand the algorithm, don't worry! It'll become clear once you see an example.

~ Implementation of Ford Fulkerson Algorithm
The flow of all the edges is 0 at the beginning.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.5.2.png

~ Select Any Arbitrary Path
Select any arbitrary path from S to T. In this step, we will select the path S->A->B->T.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.5.3.png

The minimum capacity among the three edges is 2 (B->T). Based on this, update the flow/capacity for each path.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.5.4.png

~ Select Another Path
Select another path S->D->C->T. The minimum capacity among these edges is 3 (S->D).
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.5.5.png

Update the capacities accordingly.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.5.6.png

Add all the flows, 2 + 3 = 5, which is the maximum possible flow on the flow network.

NOTE: If the capacity for any edge is full, then that path cannot be used.
'''

'''
~ Thought Process: Ford Fulkerson Algorithm
We will code the Ford Fulkerson algorithm using three classes.

1. Create the Vertex Class
We will first create a Vertex class to represent vertices in the flow network. Each vertex can be a source or a sink.

class Vertex:
    def __init__(self, name, source=False, sink=False):

        # vertex name
        self.name = name  

        # true if the vertex is a source
        self.source = source 
 
        # true if the vertex is a sink
        self.sink = sink

Here, we initialized variables for vertex name, the source, and the sink.

2. Create the Edge Class
Now we'll create the Edge class to represent directed edges in the network. Each edge has a start vertex, end vertex, capacity and flow.

class Edge:
    def __init__(self, start, end, capacity):

        # start vertex
        self.start = start  
        
        # end vertex
        self.end = end

        # capacity
        self.capacity = capacity 

        # flow is set to 0 initially
        self.flow = 0

        # the reverse edge for this edge
        self.return_edge = None

3. Create the FlowNetwork Class
The FlowNetwork class encapsulates the entire network. It contains vertices, edges, and methods to control the flow between the network.

Let's first create lists to store vertices in the network.

class FlowNetwork:
    def __init__(self):

        # list of vertices in the network
        self.vertices = []  

        # adjacency list representation of the network
        self.network = {} 

Next, we will create utility functions in the FlowNetwork class to
    * find the source vertex
    * find the sink vertex
    * add edges and vertices to the network
    * find the maximum flow


~ Step I: Find the Source and the Sink
Now, we will create different functions to find the source and the sink.

* Function to Find the Source Vertex

def get_source(self):
    for vertex in self.vertices:
        if vertex.source:
            return vertex
    return None

This function iterates through all the vertices to find the source vertex. It then returns the source vertex.

* Function to Find the Sink Vertex

def get_sink(self):
    for vertex in self.vertices:
        if vertex.sink:
            return vertex
    return None

Next, we'll add functions to get a vertex by its name and check if it already exists in the network.

~ Step II: Get and Check Vertices
Let's create functions to get a vertex and to check if it exists in the network.

* Function to Get a Vertex by its Name

def get_vertex(self, name):
    for vertex in self.vertices:
        if name == vertex.name:
            return vertex
    return None

* Function to Check if a Vertex Already Exist in a Network

def vertex_in_network(self, name):
    return any(vertex.name == name for vertex in self.vertices)

Next, we'll learn how to add a vertex to the network.

~ Step III: Add a Vertex to the Network
We add vertices to the network with the add_vertex() method:

def add_vertex(self, name, source=False, sink=False):
    if source and sink:
        return "Vertex cannot be source and sink"
    
    if self.vertex_in_network(name):
        return "Duplicate vertex"
    
    if source and self.get_source():
        return "Source already exists"
    
    if sink and self.get_sink():
        return "Sink already exists"
    
    new_vertex = Vertex(name, source, sink)
    self.vertices.append(new_vertex)
    self.network[new_vertex.name] = []

Next, let's learn how to add an edge to the network.

~ Step IV: Add an Edge to the Network
We use the add_edge() method to add edges to the network:

def add_edge(self, start, end, capacity):
    if start == end:
        return "Cannot have same start and end"
    
    if not self.vertex_in_network(start) or not self.vertex_in_network(end):
        return "Start or end vertex has not been added yet"
    
    new_edge = Edge(start, end, capacity)
    
    return_edge = Edge(end, start, 0) 
    
    new_edge.return_edge = return_edge 
    
    return_edge.return_edge = new_edge
    
    self.network[self.get_vertex(start).name].append(new_edge)
    
    self.network[self.get_vertex(end).name].append(return_edge)

Finally, we will write functions to find a path that gives the maximum flow.

~ Step V: Find a Path From Source to Sink
Now, we will create a recursive function to find a path from the source to the sink. The function will use a Depth First Search (DFS).

def get_path(self, start, end, path):
    if start == end:
        return path
    for edge in self.network[start]:
        residual_capacity = edge.capacity - edge.flow
        if residual_capacity > 0 and not (edge, residual_capacity) in path:
            result = self.get_path(edge.end, end, path + [(edge, residual_capacity)])
            if result:
                return result

~ Step VI: Calculate the Maximum Flow
Finally, we'll calculate the maximum flow with the calculate_max_flow() method:

def calculate_max_flow(self):
    source = self.get_source()
    sink = self.get_sink()
    if not source or not sink:
        return "Network does not have source and sink"

    path = self.get_path(source.name, sink.name, [])
    while path:
        flow = min(edge[1] for edge in path)
        for edge, res in path:
            edge.flow += flow
            edge.return_edge.flow -= flow
        path = self.get_path(source.name, sink.name, [])

    return sum(edge.flow for edge in self.network[source.name])

Next, we will compile all these classes and functions together to find the max flow.

'''

# Source Code:

# vertex class to represent vertices in the flow network
# each vertex can optionally be a source or a sink
class Vertex:
    def __init__(self, name, source=False, sink=False):
        self.name = name  # Vertex name
        self.source = source  # True if the vertex is a source
        self.sink = sink  # True if the vertex is a sink

# edge class represents directed edges in the network
# each edge has a start vertex, end vertex, capacity, and flow
class Edge:
    def __init__(self, start, end, capacity):
        self.start = start  
        self.end = end  
        self.capacity = capacity
        self.flow = 0
        self.return_edge = None

class FlowNetwork:
    def __init__(self):
        self.vertices = [] 
        self.network = {} 

    # function to find the source vertex
    def get_source(self):
        for vertex in self.vertices:
            if vertex.source:
                return vertex
        return None

    # function to find the sink vertex
    def get_sink(self):
        for vertex in self.vertices:
            if vertex.sink:
                return vertex
        return None

    # function to get a vertex by its name
    def get_vertex(self, name):
        for vertex in self.vertices:
            if name == vertex.name:
                return vertex
        return None

    # function to check if a vertex is already in the network
    def vertex_in_network(self, name):
        return any(vertex.name == name for vertex in self.vertices)

    # function to add a vertex to the network
    def add_vertex(self, name, source=False, sink=False):
        if source and sink:
            return "Vertex cannot be source and sink"
        if self.vertex_in_network(name):
            return "Duplicate vertex"
        if source and self.get_source():
            return "Source already exists"
        if sink and self.get_sink():
            return "Sink already exists"
        new_vertex = Vertex(name, source, sink)
        self.vertices.append(new_vertex)
        self.network[new_vertex.name] = []

    # function to add an edge to the network
    def add_edge(self, start, end, capacity):
        if start == end:
            return "Cannot have same start and end"
        if not self.vertex_in_network(start) or not self.vertex_in_network(end):
            return "Start or end vertex has not been added yet"
        new_edge = Edge(start, end, capacity)
        return_edge = Edge(end, start, 0) 
        new_edge.return_edge = return_edge 
        return_edge.return_edge = new_edge
        self.network[self.get_vertex(start).name].append(new_edge)
        self.network[self.get_vertex(end).name].append(return_edge)


    # recursive function to find a path from source to sink
    def get_path(self, start, end, path):
        if start == end:
            return path
        for edge in self.network[start]:
            residual_capacity = edge.capacity - edge.flow
            if residual_capacity > 0 and not (edge, residual_capacity) in path:
                result = self.get_path(edge.end, end, path + [(edge, residual_capacity)])
                if result:
                    return result

    # function to calculate the maximum flow using Ford-Fulkerson algorithm
    def calculate_max_flow(self):
        source = self.get_source()
        sink = self.get_sink()
        if not source or not sink:
            return "Network does not have source and sink"

        path = self.get_path(source.name, sink.name, [])
        while path:
            flow = min(edge[1] for edge in path)
            for edge, res in path:
                edge.flow += flow
                edge.return_edge.flow -= flow
            path = self.get_path(source.name, sink.name, [])

        return sum(edge.flow for edge in self.network[source.name])

# create flow network
fn = FlowNetwork()

# add vertices
fn.add_vertex('S', True, False)
fn.add_vertex('T', False, True)
for vertex_name in ['A', 'B', 'C', 'D']:
    fn.add_vertex(vertex_name)

# add edges
fn.add_edge('S', 'A', 8)
fn.add_edge('A', 'B', 9)
fn.add_edge('D', 'B', 7)
fn.add_edge('S', 'D', 3)
fn.add_edge('C', 'T', 5)
fn.add_edge('D', 'C', 4)
fn.add_edge('B', 'T', 2)

# calculate max flow
max_flow = fn.calculate_max_flow()
print("Maximum Flow:", max_flow)

'''
Output:Maximum Flow: 5

Here, we have added
    * A, B, C and D as vertices
    * S as the source
    * T as the sink.

Then, we added the edges along with their capacities.

As you can see, the maximum flow is 5, i.e., the same as the one we got in the example we discussed before:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.5.7.png

~ Time Complexity
The Ford-Fulkerson algorithm may iterate a maximum of C times, where C is the maximum flow in the network.

In each iteration, the augmenting path can be found in O(E) time. Therefore, the overall time complexity can be expressed as O(C.E).

Time Complexity: O(C.E)

'''