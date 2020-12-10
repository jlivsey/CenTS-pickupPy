# ## more on lists: example with fruits
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# print(fruits.count('apple'))

# print(fruits.count('tangerine'))

# print(fruits.index('banana'))

# print(fruits.index('banana', 4))  # Find next banana starting a position 4

# fruits.reverse()
# print(fruits)

# fruits.append('grape')
# print(fruits)

# fruits.sort()
# print(fruits)

# fruits.pop()
# print(fruits)

## example with stack
# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print(stack)
#
# stack.pop()
# print(stack)
#
# stack.pop()
# stack.pop()
# print(stack)
#
## example of list comprehension (and lambda inline)
# squares = []
# for x in range(10):
#     squares.append(x**2)
# print(squares)

# def mysquare(x):
#     return(x**2)
# squares = list(map(mysquare, range(10)))
# print(squares)

# squares = list(map(lambda x: x**2, range(10)))
# print(squares)

# squares = [x**2 for x in range(10)]
# print(squares)
#
## fancier example: combine two lists leaving out repeats
# combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(combs)
#
# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))
# print(combs)
#
## extended example of list comprehension
# vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
# print([x*2 for x in vec])

# filter the list to exclude negative numbers
# print([x for x in vec if x >= 0])
#
# apply a function to all the elements
# print([abs(x) for x in vec])
#
# call a method on each element
# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# print([weapon.strip() for weapon in freshfruit])
#
# indices = [i for i, x in enumerate(fruits) if x == 'banana']
# print(indices)

# create a list of 2-tuples like (number, square)
# print([(x, x**2) for x in range(6)])

# the tuple must be parenthesized, otherwise an error is raised
# print([x, x**2 for x in range(6)])
#
# flatten a list using a listcomp with two 'for'
# vec = [[1,2,3], [4,5,6], [7,8,9]]
# print([num for elem in vec for num in elem])
#
## example of matrix construction
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# print(matrix)

# transpose it
# print([[row[i] for row in matrix] for i in range(4)])

# unpacked
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print(transposed)