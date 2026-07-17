## ======================== Frozen set ============================

# frozenset is the immutable version of set. Once created, you can't add, remove, or modify its elements.

# ------- create frozen set --------

fs = frozenset([1, 2, 3])

fs = frozenset({1, 2, 3})  # it wii never change after creation

fs = frozenset("hello")     # frozenset({'h', 'e', 'l', 'o'})

fs = frozenset()             # empty frozenset





## ========================== What you CAN do ================

# All the read-only / non-modifying set operations work fine.


fs = frozenset([1, 2, 3])



a = frozenset([1, 2, 3])
b = frozenset([2, 3, 4])

a | b     # union -> frozenset({1, 2, 3, 4})
a & b     # intersection -> frozenset({2, 3})
a - b     # difference -> frozenset({1})
a ^ b     # symmetric difference -> frozenset({1, 4})

a.issubset(b)
a.issuperset(b)
a.isdisjoint(b)



## ============================= What you CANNOT do =============================

fs.add(4)        # AttributeError
fs.remove(1)      # AttributeError
fs.pop()          # AttributeError
fs.clear()        # AttributeError

# AttributeError: 'frozenset' object has no attribute 'remove'