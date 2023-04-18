class SimplifiedEnum(type):
    def __new__(mcs, name, bases, attrs):
        keys = attrs.get('_{}__keys'.format(name), [])
        enum_dict = {key: key for key in keys}
        enum_dict['__slots__'] = ()  # reduce memory usage
        enum_class = super().__new__(mcs, name, bases, enum_dict)
        for key in keys:
            setattr(enum_class, key, key)
        return enum_class