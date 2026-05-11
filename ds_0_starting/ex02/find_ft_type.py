known_classes = ['list', 'tuple', 'set', 'dict']


def all_thing_is_obj(object: any) -> int:
    object_class = object.__class__.__name__
    if object_class in known_classes:
        print(f"{object_class.capitalize()} : <class '{object_class}'>")
        return 0
    elif object_class == 'str':
        print(f"{object} is in the kitchen : <class 'str'>")
        return 0
    else:
        print("Type not found")
    return 42
