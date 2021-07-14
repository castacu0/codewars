"""
You probably know the "like" system from Facebook
and other pages. People can "like" blog posts,
pictures or other items. We want to create the
text that should be displayed next to such an item.

Implement a function likes :: [String] -> String,
which must take in input array, containing the names
of people who like an item. It must return the display
text as shown in the examples:

likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 
      others like this"

"""


def likes(names):
    if len(names) == 0: 
        return f"no one likes this"
    elif len(names) == 1: 
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"


# Best practices
# 1
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'}[min(4, n)].format(*names[0:3], others = n-2)
#                                                                                         ☝

#2
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)

#3
def likes(names):
    if len(names) == 1:
        return '{} likes this'.format(names[0])
    if len(names) == 2:
        return '{} and {} like this'.format(names[0], names[1])
    if len(names) == 3:
        return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    if len(names) >= 4:
        return '{}, {} and {} others like this'.format(names[0], names[1], len(names[2:]))
    else:
        return 'no one likes this'
