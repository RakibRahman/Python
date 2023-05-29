# Set is the collection of unorderable,unchangeable nad unindexable items
st0 = {5, 3, 6}
st1 = {1, 2, 3}
st2 = {4, 5, 6}

st3 = st1.union(st2)
st4 = st1.intersection(st0)
st5 = st2.difference(st0)
print(st3)
print(st4)
print(st5)
st0.add(9)
st0.discard(3)
print(st0)
