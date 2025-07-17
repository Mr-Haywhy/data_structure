'''
~ Greedy Algorithm
A greedy algorithm is a simple approach to solving a problem by selecting the best option at the moment without worrying about the future.

This method works in a top-down approach where a bigger problem is broken down into smaller parts.

Example

Imagine you are in a room with four exits, and you can only choose one path to exit. Each path has two circles that give you points.

Your goal is to maximize the points. Keep in mind that you can't change a path once you have decided on it.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-16.1.1.png

We take the path with the highest points in the first circle, which is Path1.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-16.1.2.png

Since we can't change paths now, you end up with the most points, 75 (25 from the first circle and 50 from the second circle).

However, if the path had the values in the figure below, the path we chose wouldn't be the best.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-16.1.3.png

So, this simple approach may not always get you the most points.

For example, Path 4 could have given you 105 points, and Path 3 could have given you 80 points.

NOTE: Greedy algorithms like this one focus on the best immediate choice, not necessarily the best overall outcome.

~ Greedy Algorithms Principles
There are three things to note about greedy algorithms:
    * Short-Sighted: Greedy algorithms choose the best option at the moment without thinking about the consequences in the future.
    * No Looking Back: Once a decision is made, greedy algorithms don't change their minds, even if it turns out not to be the best choice in the end.
    * Iterative Approach: Greedy algorithms solve problems step by step, always choosing what looks best right now.

~ Greedy Algorithms
Do you remember Dijkstra's Algorithm and Prim's Algorithm we learned in the previous chapters?

Dijkstra's and Prim's algorithms are both considered greedy algorithms because they make locally optimal choices at each step to eventually find a globally optimal solution.

In Dijkstra's algorithm, the greedy choice is selecting the vertex with the smallest distance from the source node at each step, ensuring that the currently known shortest path to each vertex is updated progressively.

In Prim's algorithm, the greedy choice is selecting the edge with the smallest weight that connects a vertex in the current minimum-spanning tree to a vertex outside the tree.

In this chapter, we'll follow the greedy approach to solve the following common problems:
    * The classroom scheduling problem
    * Coin change problem
    * Fractional knapsack problem
    * 0-1 knapsack problem
    * Let's get started.


****************************THE CLASSROOM SCHEDULING PROBLEM****************************
~ Problem Statement
Suppose you have a classroom and a list of classes, each with its own start and end time with an interval of one hour.

Your goal is to hold as many classes as you can in this classroom.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-16.2.1.png

As you can see, some class times overlap. So, not all of them can be held in the same room.

Let's see how we can be greedy in our approach to maximizing the number of classes we can hold in the classroom.

~ Defining the Greedy Logic
To be greedy in our approach, we focus on the ending time of each class. The idea is simple: choose the class that ends the earliest.
    1. Start with the class that ends the earliest. This is the first class you'll hold in this classroom.
    2. Now, you have to pick a class that starts after the first class and ends at the earliest. This is the second class you'll hold.
Repeat this pattern until you can't fit more classes.

~ Solving the Problem
Let's create a timeline of the classes, see which classes overlap, and see the length of each class.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-16.2.2.png

Now that we have a clear visualization of the timeline let's try choosing the first class that we want to hold in the classroom.

Step I: Choosing the First Class
The Art class ends the earliest at 10:00, so this will be our first class.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-16.2.3.png

Step II: Choosing the Second Class
Now, we need to find a class that starts after 10:00. So, we can't hold the English class in the classroom since it starts at 9:30 (before the Art class ends).

The class that begins after 10:00 and ends the earliest is Maths, which runs from 10:30 to 11:30. So, we take Maths as our second class.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-16.2.4.png

Step III: Repeat the Process
Now, our next class should start after 11:30 and end at the earliest.

However, two classes fit the description: CS and Music—both of which start at 12:00 and end at 1:00.

We can choose any of the two classes. For this example, let's choose CS.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-16.2.5.png

Since the Science class begins while the CS class is still running, we cannot hold the Science class in the classroom.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-16.2.6.png

So, these are the three classes you'll hold in this classroom.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-16.2.7.png

Even though it wasn't feasible to fit every single class into the timetable, using the greedy algorithm allowed us to optimize our schedule to include as many classes as possible.

Now, let's try implementing this in Python.
'''

'''
Thought Process
To implement the solution to the classroom scheduling problem in Python, we can follow the steps below.

1. Define the classes.

        classes = {
            "Art": (9, 10),
            "English": (9.5, 10.5),
            "Maths": (10.5, 11.5),
            "CS": (12, 13),
            "Music": (12, 13),
            "Science": (12.5, 13.5)
        }

We store the information about the classes in a dictionary along with the start and end time for each class.

2. Sort the classes based on their end time.

        sorted_classes = sorted(classes.items(), key = lambda class_info: class_info[1][1])

We now sort the classes based on their end time.

This is because our greedy approach demands that we select the class that finishes the earliest, ensuring that the room is freed up as soon as possible for another class.

3. Initialize the schedule with the first class (since it ends earliest).

        schedule = [sorted_classes[0]]

4. Choose the class if it starts after the current class has ended.

        # choose the class if it starts 
        # after the current class has ended
        _, (_, last_class_end_time) = schedule[-1]
        if start_time >= last_class_end_time:
            schedule.append((class_name, (start_time, end_time)))
            
5. Iterate through the rest of the classes.

    for class_name, (start_time, end_time) in sorted_classes[1:]:
    
'''

# Source Code
def schedule_classes(classes):
    # function to sort the classes based on end time
    sort_end_time = lambda class_info: class_info[1][1] 
    # sort the classes based on end time
    sorted_classes = sorted(classes.items(), key = sort_end_time)
    
    # initialize the schedule with the first class
    # since it ends earliest
    schedule = [sorted_classes[0]]
    
    # iterate through the rest of the classes
    for class_name, (start_time, end_time) in sorted_classes[1:]:
        # choose the class if it starts 
        # after the current class has ended
        _, (_, last_class_end_time) = schedule[-1]
        if start_time >= last_class_end_time:
            schedule.append((class_name, (start_time, end_time)))
    
    return schedule

classes = {
    "Art": (9, 10),
    "English": (9.5, 10.5),
    "Maths": (10.5, 11.5),
    "CS": (12, 13),
    "Music": (12, 13),
    "Science": (12.5, 13.5)
}

scheduled_classes = schedule_classes(classes)

for class_name, (start_time, end_time) in scheduled_classes:
    print(f"{class_name}:{start_time} to {end_time}")



'''
Output:
    Art: 9 to 10
    Maths: 10.5 to 11.5
    CS: 12 to 13


~ Time Complexity
The time complexity of this code primarily depends on two operations: sorting the classes and iterating through the sorted list.

The sort() function in Python takes O(nlogn) time complexity, where n is the number of elements to be sorted. The iteration process takes up a linear O(n) time complexity, which is insignificant when compared to the sorting process.

So, the overall complexity of the algorithm is O(nlogn).

Time Complexity: O(nlogn)    
'''