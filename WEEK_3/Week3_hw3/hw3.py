def range_sequence(*args):
    if len(args) == 1:
        return range(args[0])
    elif len(args) == 2:
        return range(args[0], args[1])
    elif len(args) == 3:
        return range(args[0], args[1], args[2])
    else:
        raise TypeError("range_sequence() takes 1-3 positional arguments but {} were given".format(len(args)))




