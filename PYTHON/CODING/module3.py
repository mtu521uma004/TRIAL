                    # LIST
# Creating a list
my_list = [3, 1, 4, 1, 5, 9]

# append()
my_list.append(2)
print("After append:", my_list)  # [3, 1, 4, 1, 5, 9, 2]

# remove()
my_list.remove(1)
print("After remove:", my_list)  # [3, 4, 1, 5, 9, 2]

# pop()
popped_item = my_list.pop()
print("Popped item:", popped_item)  # 2
print("After pop:", my_list)  # [3, 4, 1, 5, 9]

# sort()
my_list.sort()
print("After sort:", my_list)  # [1, 3, 4, 5, 9]

# reverse()
my_list.reverse()
print("After reverse:", my_list)  # [9, 5, 4, 3, 1]

                    #  TUPLE

# Creating a tuple
my_tuple = (1, 2, 3, 2, 4, 2, 5)

# count()
count_of_twos = my_tuple.count(2)
print("Count of 2s:", count_of_twos)  # 3

# index()
index_of_three = my_tuple.index(3)
print("Index of 3:", index_of_three)  # 2

                                #DICTIONARY
# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# keys()
keys = my_dict.keys()
print("Keys:", keys)  # dict_keys(['name', 'age', 'city'])

# values()
values = my_dict.values()
print("Values:", values)  # dict_values(['Alice', 25, 'New York'])

# items()
items = my_dict.items()
print("Items:", items)  # dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# get()
age = my_dict.get('age')
print("Age:", age)  # 25

# update()
my_dict.update({'age': 26, 'city': 'Boston'})
print("After update:", my_dict)  # {'name': 'Alice', 'age': 26, 'city': 'Boston'}

                                #SET

# Creating a set
my_set = {1, 2, 3, 4, 5}

# add()
my_set.add(6)
print("After add:", my_set)  # {1, 2, 3, 4, 5, 6}

# remove()
my_set.remove(3)
print("After remove:", my_set)  # {1, 2, 4, 5, 6}

# union()
another_set = {4, 5, 6, 7, 8}
union_set = my_set.union(another_set)
print("Union:", union_set)  # {1, 2, 4, 5, 6, 7, 8}

# intersection()
intersection_set = my_set.intersection(another_set)
print("Intersection:", intersection_set)  # {4, 5, 6}

# difference()
difference_set = my_set.difference(another_set)
print("Difference:", difference_set)  # {1, 2}