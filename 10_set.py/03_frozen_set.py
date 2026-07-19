## ================== frozenset ======================

# A frozenset is an immutable version of a set
# Stores unique elements
# Unordered
# No duplicate values
# Cannot add, remove, or update elements after creation

#  syntax: variable_name = frozenset(iterable)


fs = frozenset([1, 2, 3, 4, 5])

print(fs)   # frozenset({1, 2, 3, 4, 5})


numbers = [10, 20, 20, 30, 30, 40]

fs = frozenset(numbers)  # it will remove duplicates 

print(fs)   # frozenset({10, 20, 30, 40})



fs = frozenset([1, 2, 3, 4, 5])

print(fs[2])   # it showes TypeError: 'frozenset' object is not subscriptable