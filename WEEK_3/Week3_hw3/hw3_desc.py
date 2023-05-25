# https://www.python.org/dev/peps/pep-0570/#logical-ordering
# Positional-only parameters also have the (minor) benefit of enforcing some logical order when
# calling interfaces that make use of them. For example, the range function takes all its
# parameters positionally and disallows forms like:

# range(stop=5, start=0, step=2)
# range(stop=5, step=2, start=0)
# range(step=2, start=0, stop=5)
# range(step=2, stop=5, start=0)

# at the price of disallowing the use of keyword arguments for the (unique) intended order:

# range(start=0, stop=5, step=2)
"""
Write a function that accept any sequence (list, string, tuple) of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


def range_sequence(*args):
    if len(args) == 1:
        return range(args[0])
    elif len(args) == 2:
        return range(args[0], args[1])
    elif len(args) == 3:
        return range(args[0], args[1], args[2])
    else:
        raise TypeError("range_sequence() takes 1-3 positional arguments but {} were given".format(len(args)))



    # Create a range object with start=0, stop=10, step=2
    r1 = range_sequence(0, 10, 2)

    # Create a range object with start=0, stop=10, step=1
    r2 = range_sequence(10)

    # Create a range object with start=1, stop=10, step=3
    r3 = range_sequence(1, 10, 3)

    # Raises a TypeError because keyword arguments are not allowed
    r4 = range_sequence(start=0, stop=10, step=2)

    # Raises a TypeError because too many arguments are passed
    r5 = range_sequence(0, 10, 2, 4)

    # Raises a TypeError because duplicate arguments are not allowed
    r6 = range_sequence(0, 10, 0)