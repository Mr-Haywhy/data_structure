'''
~ Problem Statement
Suppose you're in a MrBeast video, and he offers to pay for all the items you can fit into a knapsack. Here are the items you can choose from:
    Gold: They have gold bars, and we can take any fraction of a bar.
    Wheat: They have bags of wheat, and we can take any fraction of a bag.
    Oil: They have containers of oil, and we can take any fraction of a container.

Upon inspection, we find that the total quantity and worth of the contents are:

    Items	Available Weight	Total Value
    Gold	    10 units	    $5000
    Wheat	    20 units	    $1000
    Oil	        14 units	    $1400

Naturally, you would like to claim the entire loot. However, you can only take what you can fit in your knapsack (it can only hold 25 units).

So, how do we select our loot so that the 25 units of content of the knapsack have the optimal value?

~ Defining the Greedy Logic
In the classroom scheduling problem, we were dealing with one solitary variable—time—which made things very simple.

But here, we have two variables:
    * the weight of the knapsack
    * the value of the content inside it to consider.

What if we could combine the weight and value variables to get a singular unit of measurement?

Since our goal is to get the most value for a given weight, it's better to consider the value per unit of each item to grab greedily instead of considering both weight and value.

So our logic to solve the problem would be:
    1. Get the value/unit of each item.
    2. Fit the maximum contents of the item with the highest value/unit in the knapsack.
    3. If there's still space remaining, repeat step 2 with the item with the next highest value/unit.

~ Solving the Problem
Let's first calculate the value per weight of each item.

    Items	Available   Weights	Total Value	Value/unit
    Gold 	10 units	$5000	$500/unit
    Wheat	20 units	$1000	$50/unit
    Oil	    14 units	$1400	$100/unit

* Choosing the First Item
As you can see from the table, gold has the most value for weight. So, we try to fit in as much gold as we can in our knapsack.

Since there are only 10 units of gold in total, we take the entire weight of gold.

Now, we only have 15 units of space left in our knapsack.

* Choosing the Second Item
Out of wheat and oil, oil has the highest value per weight. So, we try to fit in as many containers of oil in our knapsack.

There's a total of 14 units of oil containers available, so we fit all 14 units in our knapsack. Now, we can only accommodate a further 1 unit weight in the knapsack.

* Choosing the Third Item
Wheat is the only remaining item. And since we only have 1 unit of weight that can fit in our knapsack, we take just 1 unit of wheat.

So our knapsack has the following items.
    * 10 units of Gold worth $5000
    * 14 units of Oil worth $1400
    * 1 unit of Wheat worth $50

This brings the total worth of items in our knapsack to $6450.

Now let's try implementing this in Python.

Thought Process: Fractional Knapsack
We can implement the solution to the fractional knapsack problem in Python using the following steps.

1. Define the items and capacity.

        items = {
            'Gold': {'value': 5000, 'weight': 10},
            'Wheat': {'value': 1000, 'weight': 20},
            'Oil': {'value': 1400, 'weight': 14}
        }

        capacity = 25

We define our items using a dictionary where the key is the item name and the value is an ordered pair. The ordered pair contains the weights and their cost.

2. Define the function.

        def fractional_knapsack(items, capacity):

3. Calculate the value per weight of each item.

        value_per_weight = {item: item_details['value'] / item_details['weight'] for item, item_details in items.items()}

4. Sort the items by their value per weight.

        sorted_items = sorted(items, key=lambda x: value_per_weight[x], reverse=True)

5. Initialize a value of 0 and an empty knapsack.

        total_value = 0
        knapsack = {}

6. Insert items into the knapsack.
Before we can insert items into the knapsack, we need to consider the value and weight of each item.

        for item in sorted_items:
            item_weight = items[item]['weight']
            item_value = items[item]['value']

After that, we compare the total weight of each item to the remaining capacity of the knapsack, starting with the item with the greatest ratio of value to weight.

If the whole item fits:
    * The item is added to the knapsack.
    * Its weight is subtracted from the knapsack's remaining capacity.
    * Its value is added to the total value of contents in the knapsack.

        # if the item fits, take the whole item
        if capacity >= item_weight:
            knapsack[item] = item_weight
            capacity -= item_weight
            total_value += item_value

If the whole item doesn't fit in the knapsack:
    * A fraction of the item is calculated, which is equal to the remaining capacity of the knapsack.
    * Only this fraction of the item is added to the knapsack.
    * The value of the fraction of the item taken increases the value of the knapsack.

        # take a fraction of the item
        else:
            weight_taken = capacity
            knapsack[item] = weight_taken
            total_value += (value_per_weight[item] * weight_taken)
            break  # No more capacity
    
The loop breaks after this because the knapsack is full, and we cannot add any more items or fractions.
'''

# Source Code

def fractional_knapsack(items, capacity):
    # calculate the value per weight for each item
    value_per_weight = {item: item_details['value'] / item_details['weight'] for item, item_details in items.items()}

    # sort the items by their value per weight in descending order
    sorted_items = sorted(items, key=lambda x: value_per_weight[x], reverse=True)

    # initialize a value of 0 and an empty knapsack
    total_value = 0
    knapsack = {}

    for item in sorted_items:
        item_weight = items[item]['weight']
        item_value = items[item]['value']

        # if the item fits, take the whole item
        if capacity >= item_weight:
            knapsack[item] = item_weight
            capacity -= item_weight
            total_value += item_value
        
        # take a fraction of the item
        else:
            weight_taken = capacity
            knapsack[item] = weight_taken
            total_value += (value_per_weight[item] * weight_taken)
            break  # No more capacity

    return knapsack, total_value

# example usage
items = {
    'Gold': {'value': 5000, 'weight': 10},
    'Wheat': {'value': 1000, 'weight': 20},
    'Oil': {'value': 1400, 'weight': 14}
}
capacity = 25

result_with_weight, total_value = fractional_knapsack(items, capacity)
print(f"Items in the knapsack: {result_with_weight}")
print(f"Total value: {total_value}")

'''
Output:
    Items in the knapsack: {'Gold': 10, 'Oil': 14, 'Wheat': 1}
    Total value: 6450.0


~ Time Complexity
Similar to the above processes, most of the time complexity is driven by sorting using the sort() function.

Time Complexity: O(nlogn)


~ Nature of Greedy Algorithms
Greedy algorithms are so straightforward that they leave you second-guessing if you are wrong.

But that's the beauty of these algorithms; they're easy.

A greedy algorithm follows a straightforward approach: at every stage, select the best immediate move.

In technical terms: at each phase, you select the locally optimal solution, and hope it leads you to the globally optimal solution.

We have studied three problems till now and all of them have yielded optimal solutions so far.

However, we will now discuss a problem where the greedy solution may not be the optimal solution.
'''