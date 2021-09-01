"""Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.

def greet(name):
    return print("Hello, {name}!".format(name=name))
    if name == "Johnny":
        return print("Hello, my love!") """


def greet(name):
    if name == "Johnny":
        return print("Hello, my love!")
    return print("Hello, {name}!".format(name=name))

greet("Name")