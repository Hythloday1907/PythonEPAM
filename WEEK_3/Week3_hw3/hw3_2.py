from hw3 import range_sequence

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