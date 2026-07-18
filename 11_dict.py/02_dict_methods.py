


d = {"a": 1, "b": 2, "c": 3}

# get() - Returns value for a key
d.get("a")              # 1

# keys() - Returns all keys
d.keys()                # dict_keys(['a', 'b', 'c'])

# values() - Returns all values
d.values()               # dict_values([1, 2, 3])

# items() - Returns key-value pairs
d.items()                # dict_items([('a', 1), ('b', 2), ('c', 3)])

# update() - Updates dictionary
d.update({"d": 4})       # d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# pop() - Removes a key
d.pop("a")               # 1, d = {'b': 2, 'c': 3, 'd': 4}

# popitem() - Removes last item
d.popitem()               # ('d', 4), d = {'b': 2, 'c': 3}

# clear() - Removes all items
d.clear()                 # d = {}

# copy() - Returns a copy
d2 = {"x": 1}
d3 = d2.copy()            # d3 = {'x': 1}

# setdefault() - Returns value; creates key if absent
d2.setdefault("y", 99)    # 99, d2 = {'x': 1, 'y': 99}

# fromkeys() - Creates dictionary from keys
dict.fromkeys(["a", "b"], 0)   # {'a': 0, 'b': 0}


