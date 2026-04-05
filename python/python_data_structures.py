# The most important rule: 
# use a dict when you need fast lookup by key, 
# a set when you need uniqueness, 
# a list when order matters, 
# and a tuple when data is fixed.

# List[] Ordered, mutable, allows duplicates.

fruits = ["apple", "banna", "cherry"]
fruits.append("mango")	# add to end
fruits.remove("banna")	# remove by value
fruits[0]				# indexing -> "apple"
fruits[1:0]				# slicing -> ["cherry", "mango"]


# Tuple() Ordered, immutable, allows duplicates. Faster than lists.
# Use when data shouldn't change — coordinates, RGB, DB records

point = (10, 20)
point[0]				# 10
x, y = point			# unpaking
print(x, y)


# Dictionary {}
# Key-value pairs, ordered (Python 3.7+), mutable, keys must be unique.

person = {"name": "Alice", "age": 30}
person["age"]             # → 30
person["city"] = "NYC"    # add key
person.get("phone", "N/A")  # safe access with default
person.keys()             # dict_keys(["name", "age", "city"])
person.items()            # key-value pairs




