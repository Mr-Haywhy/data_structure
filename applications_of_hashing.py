# ................Applications of Hashing....................
# Before closing, let's discuss the following topics to understand the actual application areas of hashing:
#     *Python Dictionaries as Hash Tables
#     *Hashing Passwords

# .............Python Dictionaries as Hash Tables................
# In Python, dictionaries are implemented as hash tables, which is why they have an average O(1) time complexity for lookup, insertion, and deletion.

# To understand how Python dictionaries work as hash tables, let's delve into some of the fundamentals:
#     1. Hash Function: Python uses a specialized hash function called SipHash starting from Python 3.3.
#     2. Collisions: Python handles collisions using an open addressing scheme similar to quadratic probing.
#     3. Dynamic Resizing: As more items are added to a dictionary, the underlying hash table might become densely populated, leading to more collisions. To handle this, Python dictionaries are designed to resize dynamically.
#     4. Key Invariance: It's important to note that dictionary keys should be immutable. This is because if a key changes its value (and thus its hash) after it's been added to the dictionary, it would make the value associated with it unreachable.

# Let's look at a simple example of using the Python dictionary.

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# access a value using a key
print(person["name"])

# insert a new key-value pair
person["job"] = "Engineer"

# remove a key-value pair
del person["age"]

# display person
print(person)

# check if a key is in the dictionary
if "city" in person:
    print("City is:", person["city"])