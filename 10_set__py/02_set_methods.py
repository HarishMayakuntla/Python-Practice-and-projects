## ===================== core operrations ==============


s = {1, 2, 3}

s.add(4)          # {1, 2, 3, 4}

s.remove(2)        # {1, 3, 4} -- raises KeyError if missing

s.discard(10)       # no error even if not present

s.pop()              # removes & returns an arbitrary element


s.clear()           # empty the set




print(s)         #   set()



## ========================== set math =================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# union ----> | represent
# intersection -----> & represent
# difference ------->  -  represent
# symmetric_difference -------> ^ represent


a.union(b)  or  a | b   # union            -> {1,2,3,4,5,6}

a.intersection(b)  or  a & b   # intersection     -> {3,4}
  
a.difference(b)    or  a - b   # difference       -> {1,2}

a.symmetric_difference(b)   or  a ^ b   # symmetric diff   -> {1,2,5,6}




## ========================== comparisons =====================

{1,2}.issubset({1,2,3})     # True  , because  {1,2} is set the set is present in  {1,2,3}

{1,2,3}.issuperset({1,2})   # True ,  because {1,2,3} contain the {1,2}

{1,2}.isdisjoint({3,4})     # True (no overlap)