# from random import choice
# x = choice([1, 2, 3, 4, 5, 6])
# print(x)

# import random
# print(random.choice([1, 2, 3]))

# import random as rdm
# print(rdm.choice([1, 2, 3]))

# ---- Installing other modules with pip
# ---- they get put into the site-packages directory


# print("hello census")
#
# x = 10
# y = 20
#
#
# print(x + 5)
# print('x =', x)
# print(x + y)

#

# x = 40
#
# if x > 5:
#     print("made it")
#     print("line two of if statement")
#     if x > 10:
#         print("x also bigggg")
# else:
#     print("ELSE statement")


#
#
# # Comments are the same as in R
#
#
# x = 5
# y = 5.0
# z = True
# Z = False
# a = 'livsey'
# b = range(10)
# print(type(b))
# print(type(a))
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(Z))
#
# # Arithmetic Operators
#
# 2 + 3  # add
# 2 - 3  # subtract
# 2 / 3  # divide
# 2 % 3  # mod
# 2 * 3  # multiplication
# 2 // 3 # floor division
# 2 ** 3 # 2^3

# # Fibonacci series:
# # the sum of two elements defines the next
# a, b = 0, 1 # multiple assignment a=0 and b=1
# while a < 10:
#     print(a)
#     a, b = b, a+b
#
# # ---- Lists
#
# squares = [1, 4, 9, 16, 25]
# print(squares)
#
# # # Like strings (and all other built-in sequence types), lists can be indexed and sliced:
# print(squares[0])  # indexing returns the item
# # 1
# print(squares[-1]) # start at end
# # 25
# print(squares[-3:])  # slicing returns a new list
# # [9, 16, 25]
#
# # Lists also support operations like concatenation:
# new_square = squares + [36, 49, 64, 81, 100]
# print(new_square)
# # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# cubes = [1, 8, 27, 65, 125]  # 64, not 65!
# print(cubes)
# cubes[3] = 64  # replace the wrong value
# print(cubes)
# #
# # # use the append() METHOD.... need to learn more about methods during a later meeting
# cubes.append(216)  # add the cube of 6
# cubes.append(7 ** 3)  # and the cube of 7
# cubes = cubes + [8 ** 3]
# print(cubes)
# # [1, 8, 27, 64, 125, 216, 343]


# # ---- Lets write our own Fibonacci sequence that populates a list
# fib_seq = [0, 1]
# while fib_seq[-1] < 500:
#     fib_seq.append(fib_seq[-2] + fib_seq[-1])
# print(fib_seq)
#
# # Tucker Sol'n
# a, b = 0, 1
# fib = [a]
# while a < 500:
#     a, b = b, a + b
#     fib = fib + [a]
# print(fib)


# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
#
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters)
# # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#
# # replace some values
# letters[2:5] = ['C', 'D', 'E']
# print(letters)
# # ['a', 'b', 'C', 'D', 'E', 'f', 'g']
#
# # now remove them
# letters[2:5] = []
# print(letters)
# # ['a', 'b', 'f', 'g']
#
# # clear the list by replacing all the elements with an empty list
# letters[:] = []
# print(letters)
# # []
#
# # The built-in function len() also applies to lists:
# letters = ['a', 'b', 'c', 'd']
# len(letters)
#
# # It is possible to nest lists (create lists containing other lists), for example:
# a = ['a', 'b', 'c']
# n = [1, 2, 3]
# x = [a, n]
#
# print(x)
# # [['a', 'b', 'c'], [1, 2, 3]]
#
# print(x[0])
# # ['a', 'b', 'c']
#
# print(x[0][1])
# # 'b'
#
#


# ---- Control Statements

# x = int(input("Please enter an integer: ")) # User input
#
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')


# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))


# range( ) function. Interesting coming form R

# why this output?
# x = range(5)
# print(x)
#
# print(sum(x)) # but this act a bit more "normal" (coming from R)

# --- write for loop to look at elements of x
#
#
#
#
#
#


# From the help page: range([start,] stop [, step]) -> range object
# print(range(5, 10))
#    # 5, 6, 7, 8, 9
#
# print(range(0, 10, 3))
#    # 0, 3, 6, 9
#
# print(range(-10, -100, -30))
#   # -10, -40, -70


# ---- Functions ----

# def fib(n):    # write Fibonacci series up to n
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()
#
# # Now call the function we just defined:
# fib(2000)