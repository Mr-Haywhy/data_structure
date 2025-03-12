#
# List Slicing Examples
#

numbers = [10, 20, 30, 40, 50, 60]

# items from index 0 to 3
print(numbers[0: 4])    # [10, 20, 30, 40]

# items from index 3 to 4
print(numbers[3: 5])   # [40, 50]

# If we omit the start index, 
# the slicing starts from the first item.
# items from first item to third index
print(numbers[: 4])    # [10, 20, 30, 40]

# If we omit the end index, 
# the slicing goes up to the last item
# items from 3rd index to last item
print(numbers[3: ])   # [40, 50, 60]


# If we omit both the start and end indexes, we get a new
# list that contains all the items from the original 
# list (from the first item to the last item).
# omitting both the start and end indexes
# items from first to last
print(numbers[:])   # [10, 20, 30, 40, 50, 60]

# using negative index in slicing
# items from the fourth item (3rd index)
# to the second-last item

print(numbers[3: -1])   # [40, 50]


# Another example

animals = ['dog', 'cat', 'guinea pig', 'rat']

# extract elements using list slicing
new_animals = animals[1: 3]

# print the new list
print(new_animals)

# extract elements using list slicing
new_animals_1 = animals[2: ]

# print the new list
print(new_animals)


# REPETITION WITH LISTS
# 
# Suppose, we need to create a list with five elements, all having the value 0. We can easily achieve this using the * operator. For example,
lst = [0] * 5
print(lst)  # [0, 0, 0, 0, 0]


# LIST METHODS
# append() : add an element to the end of the list
# extend() : add elements of an iterable (list, tuple,etc.) to the end of the list
# insert() : insert an element at the specified index
# pop() : remove an element from the list and return it
# reverse() : reverse the elements of the list.

# list APPEND() and EXTEND()
currencies = ['Dollar', 'Euro', 'Pound']

# append 'Yen' to the list
currencies.append('Yen')

# List.append() takes exactly one argument

print(currencies)

# extend()
languages = ['French', 'English']
languages1 = ['Spanish', 'Portuguese']

# append language1 elements to languages
languages.extend(languages1)

print(languages)

# By the way, we can also use the + operator to extend a list in Python. For example,
languages = ['French', 'English']
languages_1 = ['Spanish', 'Pidgin']

# append language1 elements to languages
languages_list = languages + languages_1

print(languages_list)


# LIST POP()
# The pop() method removes the item at the specified index. The method also returns the removed item.

prime_numbers = [2, 3, 5, 7]

# remove the element at index 2
removed_element = prime_numbers.pop(2)

print(f"Updated List: {prime_numbers}")
print(f"Removed Element: {removed_element}")

# If we do not pass any arguments to the pop() method, it removes the last element.

# remove the last item
prime_numbers.pop()

print(f"Updated List: {prime_numbers}")
# NOTE: the removed value is not passed to any variable, so the data will be lost


# LIST INSERT()
# The insert() method inserts an element at the specified index.

# create a list of vowels
vowel = ['a', 'e', 'i', 'u']

# insert 'o' at index 3 (4th position)
vowel.insert(3, 'o')

print(vowel)

# NOTE: The insert() method does not return any value; it only modifies the original list.

# LIST REVERSE()
# The reverse() method reverse the elements of the list.

prime_numbers = [2, 3, 5, 7]

# reverse the order of list elements
prime_numbers.reverse()

print(prime_numbers) 

# NOTE: The reverse() method does not return any value; it only modifies the original list.

# ENUMERATE()

# The for loop in python doesn't automatically use indexes.

languages = ['Python', 'Java', 'JavaScript']

for language in languages:
    print(language)   # Python, Java, Javascript

# However, if we need to access the index during each iteration of a for loop, we can use the enumerate() function along with the loop.
# i.e

enumerate_languages = enumerate(languages)

# convert enumerate object to list
print(list(enumerate_languages))
print(type(enumerate_languages))

# using enumerate() in a for loop

for index, language in enumerate(languages):
    print(index, language)

# NOTE: Essentially, if we need to work with indexes inside a for loop, we can utilize the enumerate function.


# Practice
animals = ['Dog', 'Cat']
wild_animals = ['Tiger', 'Coyote']

# perform list operations
animals.append('Raccoon')

animals.extend(wild_animals)

animals.pop(2)
animals.pop()

animals.insert(2, 'Moose')

print(animals)