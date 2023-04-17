# 1. Implement a function that flatten incoming data:
# non-iterables and elements from iterables (any nesting depth should be supported)
# function should return an iterator (generator function)
# don't use third-party libraries

def merge_elems(*elems):
    pass
    for elem in elems:
        if isinstance(elem, (list, tuple)):
            yield from merge_elems(*elem)
        elif isinstance(elem, str):
            yield from elem
        else:
            yield elem
# example input
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = [[1, 2], [3, 4]]

for elem in merge_elems(a, b, c, d):
    print(elem, end=' ')

# output: 1 2 3 6 z h a b a 1 2 3 4

# 2. Implement a map-like function that returns an iterator (generator function)
# extra functionality: if arg function can't be applied, return element as is + text exception

def map_like(fun, *elems):
    pass
    for elem in elems:
        try:
            yield fun(elem)
        except (TypeError, IndexError) as e:
            yield f"{elem}: {e}"

# example input
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = True
fun = lambda x: x[0]

print("\n")
for elem in map_like(fun, a, b, c, d):
    print(elem)

# output:
# 1
# 6: 'int' object is not subscriptable
# z
# True: 'bool' object is not subscriptable