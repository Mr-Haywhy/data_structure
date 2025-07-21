'''
Recap: 0-1 Knapsack Problem
We've already introduced this problem in our chapter on Greedy Algorithms. Here's how it goes:

You're in a Mr.Beast video, and he will buy you all the items you can fit into a knapsack.

Item	    Weight	    Total Value
TV	        30 units	$3000
Laptop	    20 units	$2000
Mobile	    15 units	$1500

The capacity of the knapsack is 35 units.

Your goal now is to determine the maximum value that can be achieved by selecting items without exceeding the knapsack capacity.

Recap: Greedy Solution
This was our greedy approach to the 0-1 Knapsack problem:
1. Pick the most expensive thing that will fit in your knapsack.
2. Pick the next most expensive thing that will fit in your knapsack. And so on.

This means we will start with the $3000 TV that weighs 30 units and will be left with 5 units in our knapsack.

Since no other item will fit inside the knapsack, our solution brings us goods worth $3000.

Here, choosing the TV early on prevents you from fitting in multiple items with a slightly lower value-to-weight ratio but a higher combined value later (the laptop weighing 20 units and the mobile weighing 15 units, for a combined value of $3500).

Let's see how we can use dynamic programming to get the optimal solution to this problem.

The 0-1 Knapsack Problem Using Dynamic Programming
Instead of moving greedily like we did before, we'll iteratively fit different combinations of items in the knapsack and choose the combination that ensures the most profit.

As such, we'll be using a table to store the profit from each combination.

But taking 35 units weight will result in a table with 36 columns, which will become hard to understand.

So, we'll be modifying the weights and values to make the DP table more manageable.

Item	Weight	Total Value
TV	    4 units	$150
Laptop	3 units	$100
Mobile	2 units	$60

Also, suppose we have a knapsack with a maximum weight capacity of 5 units.

Now, let's move on to building our logic with these values.

Note: We have not maintained the original weight-to-value ratio in order to make the DP process more easy to understand.

You know that the core concept of dynamic programming is to divide the problem into smaller subproblems i.e., a series of decision steps.

So what might be the decision step for our knapsack problem?

The simplest decision step is to check whether you want to add the item to the bag or not.

So, we'll be using the decision trees we learned in the Binary Trees chapter.

We start with an empty knapsack:

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.1.png

Next, we'll take our first decision step for the problem.

First Decision Step
The initial decision centers around the TV. Do we want to include it or not?
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.2.png

If we take the TV, we'll get a profit of $150 while filling 4 units of weight inside our knapsack (which has a capacity of 5 units).

If we don't take the TV, we get an empty knapsack with $0 profit.

Second Decision Step
The next decision involves the laptop. Should we include it or not?
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.3.png

This decision step results in the following possibilities:

Knapsack Items	        Combined Weight	Total Profit
None (Empty Knapsack)	0	                0
Laptop	                3	                100
TV	                    4	                150
TV + Laptop	            7 (Invalid)	        250

As you can see, we already have an invalid option (TV + Laptop) because their combined weights exceed the knapsack capacity.

But since the decision-making process isn't complete, we'll leave this option as it is and move on to the next step.

Third Decision Step
Finally, we consider the mobile. Do we want to include it in the knapsack?
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.4.png

As you can see, there are some combinations here that exceed the knapsack capacity.

So, we should only select the optimal solution that can fit in the knapsack.

Choosing the Optimal Solution
By now, it should be obvious that the maximum profit achievable by including all items in the knapsack ($310) isn't achievable since it exceeds the knapsack's weight limit of 5 units.

Therefore, the highest profit achievable (Laptop + Mobile) within the weight constraint is $160, with a total weight of 5 units.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.5.png

Now, let's learn how to build a DP table to solve this.

Dynamic Programming Table
While decision trees allow us to visualize each possible outcome, processing it is often computationally expensive due to recursive overheads.

So, we'll try to represent each information from the tree in a table called the dynamic programming table.

To maximize the profit obtainable from a knapsack of capacity 5, we first solve subproblems to determine the maximum profit achievable in knapsacks of smaller capacities (starting from 0).

So, our table will have six columns (not counting the Weight, Value, and Item columns, which are only there to make the table easy to follow):
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.6.png

Here, each cell will show the maximum profit that can be made in a knapsack of a particular capacity. Our task is to fill these cells row by row.

We must note that the way we fill one row depends on the way we filled the previous row (our choices have consequences).

With this in mind, let's start with the first row, which is when the knapsack is empty.

DP Table: Empty Knapsack
Having no item means there are no profits. So, each entry in this row will be 0.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.7.png

Now, our first decision is if we want to include the TV or not.

DP Table: Choosing the First Item
Our first item is the TV. Let's explore the different cell values that can be entered for this item.

Case I: Knapsacks That Can't Fit the Item

Since the TV in itself weighs 4 units, any knapsack with a lower capacity will not be able to contain it.

So, for those capacities, the profit will stay as they were in the previous row.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.8.png

Case II: Knapsack That Can Exactly Fit the Item

Since the next knapsack has a capacity of 4 units, it can exactly fit the TV. So, we'll update the corresponding cell to reflect this value.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.9.png

As the previous value was 0, the total profit will solely come from the TV, making the cell's value 150.

Case III: Knapsack Has More Than Enough Space to Fit the Item

Putting a TV of weight of 4 inside a knapsack of capacity of 5 means the knapsack will have the same value as a knapsack with capacity 4 (since it's currently filled only by the TV).

However, there will still be room for another item of weight 1 in the future.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.10.png

Since the table cells only record the current profit, this cell will also be updated with the value of the TV, which is 150.

Now that this row is filled, let's fill the third row.

DP Table: Choosing the Second Item
Our next decision involves the laptop — do we put it inside our knapsack or not?

Case I: Knapsacks That Can't Fit the Item
As before, any knapsack with a capacity less than the weight of the laptop cannot include it.

Since the laptop weighs 3 units, all the cells up to knapsack 2 will retain the same value as the corresponding cells in the row above.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.11.png

Case II: Knapsack That Can Exactly Fit the Item
Unlike the TV, the knapsack with capacity 3 can contain the laptop. So, we will update its cell with the value of the laptop.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.12.png

Case III: Knapsacks With Previously Added Items
Now comes the tricky part!

Up until now, every cell we have updated contained 0 in the cell above it.

In other words, the knapsack of that particular capacity was left unoccupied by the previous object.

But the knapsack of capacity 4 already contains the TV. How do we handle this?

DP Table: Choosing the Best Option
Whenever we encounter a cell that has been updated in the previous row, we have two choices:
    1. If both objects fit in the knapsack of that capacity, add them both.
    2. If there isn't enough space for both, choose the one that provides the maximum value.

Let's apply this logic to the knapsacks with capacities 4 and 5 units.

Case IIIa: Knapsack With Capacity 4
Here, the TV and the laptop combined weigh 7 units, which can't fit inside the knapsack with capacity 4. So, we'll only include the object that gives better value for money, i.e., the TV.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.13.png

NOTE: If the laptop had a higher value, we'd have taken out the TV and added the laptop instead.

Case IIIb: Knapsack With Capacity 5
For the final cell of the row, the combined weight of the TV and the laptop is still higher than the knapsack capacity. So, we'll fill it using the same logic.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.14.png

~ DP Table: Choosing the Third Item
Finally, we have to decide whether we want the mobile or not.

Case I: Knapsacks That Can't Fit the Item
The cells for knapsacks with capacities less than 2 units will be filled with the same values from the previous row.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.15.png

Case II: Knapsack That Can Exactly Fit the Item
So far, the knapsack with capacity 2 has been left unoccupied. Therefore, we'll update its value from 0 to 60 (the value of the mobile).
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.16.png

Case III: Knapsacks With Previously Added Items
a. Knapsack With Capacity 3

We can see that this knapsack is currently occupied by the laptop, which weighs 3 units. So, we cannot add the mobile because the laptop has completely filled the knapsack capacity.

Thus, we'll stick with the laptop because it gives a higher value, which is 100.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.17.png

Case IIIb: Knapsack With Capacity 4
Similarly, this knapsack currently holds the TV and cannot hold the mobile. Since the TV provides a higher value, we won't update the cell.

Thus, we get the table below:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.18.png

Case IIIc: Knapsack With Capacity 5
The final cell isn't as straightforward. Going by the logic we've been using so far, we can simply retain the TV since it has the highest individual value.

However, we must realise that the knapsack capacity is 5, which means we also have the option to include combinations that weigh 5 units.

Fortunately, we do have such a combo — the laptop (weight 3) and the mobile (weight 2).

Additionally, their combined value of 160 is higher than that of the TV alone, which is a mere 150.

So, we replace the TV with the laptop and the mobile.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.19.png

Next, let's use this knowledge to generalize a formula that can be used to fill each entry in the DP table.

The DP Table Formula
Now, we'll express the logic behind filling the DP table in the form of a mathematical formula.

Recall that when filling the final cell of the table, we compare two possible values for each item:

    1. The profit from the row above (where the item is not included).
    2. The profit from including the item, which also includes the optimal profit from other items (if any) that can fit inside the knapsack.

Consider the incomplete DP table below, which we used in a previous page:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.20.png

Now, we'll learn the DP table formula by using the cell with the green highlight as a reference.

In order to code a DP table, we need a mathematical expression that can calculate the value of a given cell inside that table.

For example, suppose we need to calculate the value of the cell we've denoted as DP[i, w]. This will be our reference cell, which is shown in the image below:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.21.png

Then, the general formula for filling DP[i, w] is:

        max( DP[i-1, w], ( DP[i-1, w - w(i)] + P(i) ) )

General Rule of Thumb: In a DP table, i represents the current row and w represents the current column.

This formula selects the maximum value among two possible values:

    *DP[i-1, w]
    *DP[i-1, w - w(i)] + P(i).

But before we learn about these two values, it's important to understand basic terms like i, P(i), w, etc. So, let's understand them next.

Here's our previous DP table:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.22.png


And here's our general formula for filling a cell:

max( DP[i-1, w], ( DP[i-1, w - w(i)] + P(i) ) )
The table below explains the basic expressions used in the formula:

Expression	Description
i       |   A numerical value that represents an item we can keep inside the knapsack.

        In the image above, i = 0 represents no item, i = 1 represents the TV, i = 2 represents the laptop, and so on.
P(i)    |	The profit/value of the current item we're      considering to include inside the knapsack. For our reference cell, P(i) is the value of the laptop (100).
w(i)    |	The weight of the current item. For our reference cell, w(i) is the weight of the laptop (3).
w	    |   The knapsack capacity for the cell. Our reference cell is for a knapsack of capacity 4, so w = 4.
w - w(i)|	The result obtained by subtracting the item value from the knapsack capacity. For our reference cell, its value is 4 - 3 = 1.

Next, let's locate the above components in our DP table.

Now, we'll locate i, w, P(i), and w(i) for our reference cell DP[i, w]:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.23.png

Notice that w(i), P(i), i, and DP[i, w] are in the same row. This is because they're all quantities that describe different properties of the current item (the laptop).

Also notice that w indicates both the current knapsack weight and the current column of the table.

Now that we know what the basic expressions in the formula represent, we can finally analyze the two terms: DP[i-1, w] and DP[i-1, w - w(i)] + P(i).

Let's start by reviewing the formula for filling the cell DP[i, w]:

max( DP[i-1, w], ( DP[i-1, w - w(i)] + P(i) ) )
This formula chooses the max value among two components:

Component	                |   Description
DP[i-1, w]	                |   The profit when the current item is not included in the knapsack., i.e., when we simply copy the value from the row above.

DP[i-1, w - w(i)] + P(i)	|   The sum of DP[i-1, w - w(i)] and P(i).

                                Here, P(i) is the value of the current item.

                                And, DP[i-1, w - w(i)] is the optimum value from the first i-1 items (i.e., the previous items) that fits in the space left after adding the current item (i.e., item i).

Just reading the descriptions of these components might not be sufficient to understand the formula. So, let's locate them in our DP table next.

Finally, let's locate the two components of the DP formula in our table. Then, we can calculate the value of the reference cell.

In our highlighted cell,

        i = 2
        w = 4
        w(i) = w(2) = 3
        P(i) = P(2) = 100. 

        i - 1 = 2 - 1 = 1
        w - w(i) = 4 - 3 = 1

So, we have:

        DP[i-1, w] = DP[1, 4]
        DP[i-1, w - w(i)] = DP[1, 1]

Let's locate where these terms lie in the table.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.3.24.png

So, our two values to choose from are:

* DP[1, 4] = 150
* DP[1, 1] + 100 = 0 + 100 = 100

Now, we take the maximum out of these two values:

        max(150,100) = 150

This is the exact value we obtained for the cell when we manually filled the table.

Thought Process: DP Table
Now that we are all set, let's implement our DP table logic in Python.

1. Initialize the required variables.
First, we'll store our item weights and values in lists and also define the capacity of the knapsack.

# Initialize variables
w = [2, 3, 6]
v = [60, 100, 150]
capacity = 5

Here, w is a list of item weights and v is a list of their corresponding values.

2. Initialize the DP table.
Then, we create a table with the following dimensions:

(number of items + 1) x (capacity + 1)
Each cell in this table is initialized to 0.

# Initialize an empty DP table
DP = [[0] * (capacity + 1) for _ in range(len(w) + 1)]

3. Choose the item you want to include in the knapsack.
Now, we'll use the formula we derived to fill each cell.

If the current capacity (index) is greater than or equal to the item weight:

Check whether including the item increases the profit.
Otherwise, exclude the item, copying the value from the previous row.

if index >= item_weight:
    # Use DP table formula
    DP[item_index + 1][index] = max(DP[item_index][index], DP[item_index][index - item_weight] + v[item_index])
else:
    DP[item_index + 1][index] = DP[item_index][index]

4. Apply the logic in Step 3 to all items and all possible capacities.
Previously, we applied the DP table formula to decide whether to include an item in the knapsack.

Now, we extend this logic to all items and possible knapsack capacities. So we'll encapsulate this logic inside two loops.

# Run the loop once for each item
for item_index, item_weight in enumerate(w):
    # Compare and change values
    for index, value in enumerate(DP[item_index]):
        # You can only add an item  if the
        # bag size is larger than the item weight
        if index >= item_weight:
            DP[item_index + 1][index] = max(DP[item_index][index], DP[item_index][index - item_weight] + v[item_index])
        # Otherwise, just copy the profit from one row above
        else:
            DP[item_index + 1][index] = DP[item_index][index]

 5. Encapsulate the entire logic inside a function that returns the solution.

Finally, encapsulate the code in Step 4 inside the maximize_profit() function, which returns the last cell in the table.

We return the last cell because it contains our solution.

# Function that returns the solution
maximize_profit(w, v, capacity):

    # Code in Step 4

    # Return the last cell (solution)
    return DP[-1][-1]
'''

'''
Source Code
Now let's combine what we have built so far to build a working program and visualize how it works.
'''

def maximize_profit(weight, value, capacity):
    # Initialize an empty table dp_table
    dp_table = [[0] * (capacity + 1) for _ in range(len(weight) + 1)]

    # Run the loop once for each item
    for item_index, item_weight in enumerate(weight):
        for index in range(capacity + 1):
            # You can only add an item if the bag size is larger than the item weight
            if index >= item_weight:
                dp_table[item_index + 1][index] = max(
                    dp_table[item_index][index],
                    dp_table[item_index][index - item_weight] + value[item_index]
                )
            # Otherwise, just copy the profit from one row above
            else:
                dp_table[item_index + 1][index] = dp_table[item_index][index]

    # The last cell returns the maximum profit.
    return dp_table[-1][-1]

# Initialize variables
weight = [1, 2, 3, 5]
value = [60, 100, 200, 310]
capacity = 10

# Call the function and print the result
print(maximize_profit(weight, value, capacity))