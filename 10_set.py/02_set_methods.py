## ================== set methods =============

# ---------- Adding Elements --------------------

a={1,2,3,4,5}

# add ()

a.add(4)          # here add a single element

# update ()

a.update([2,8,9,4,7])  # here i add multiple values

print(a)   # {1, 2, 3, 4, 5, 7, 8, 9}


# ---------------- remove elements -------------

# remove()
b={4,5,6,7,8}

b.remove(6) # here 6 is exits in set so it will run

print(b) #  {4, 5, 7, 8}


b.remove(9)  

print(b)  #  it showes KeyError: 9

# discard() 
b= {4,5,6,7,8}

b.discard(4)   # it will remove 4 in the given set

print(b) #  {5, 6, 7, 8}


b.discard(2)

print(b) # i cannot show any thing


# pop()

s = {10, 20, 30}

s.pop()  # it remove random element to the set

print(s) # {20,10}


# clear()

t = {10, 20, 30}

t.clear()  # remove all elements in the list

print(s) # set()


#------------------ set operations -------------------

#-- union (|) -------- merge two sets

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # {1, 2, 3, 4, 5}

# or

print(a.union(b)) #{1, 2, 3, 4, 5}


# -- Intersection (&) -- gives common elements of both sets

a = {1, 2, 3}
b = {3, 4, 5}

print(a&b) # {3}

# or

print(a.intersection(b))  # {3}


# -- difference(-) --- new set containing elements that are in the first set but not in the second set.

k = {1, 2, 3, 4, 5}
l= {4, 5, 6, 7}


print(k-l)    #  {1, 2, 3}

# or

print(k.difference(l)) # {1, 2, 3}


# --- symmetric difference ---- Common elements are removed, and unique elements from both sets are kept

c = {1, 2, 3, 4, 5}
d = {4, 5, 6, 7}


print(c^d)  # {1,2,3,6,7}

# or

print(c.symmetric_difference(d))  #  {1,2,3,6,7}
