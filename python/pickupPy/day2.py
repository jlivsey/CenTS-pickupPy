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

# fib
# # <function fib at 10042ed0>
# f = fib
# f(100)
# # 0 1 1 2 3 5 8 13 21 34 55 89


### An interesting observation: The documentation we are looking through implements the exact function we wrote
###       during our last meeting - populating a list with Fibonacci series. Let's compare what they did to what
###       Tucker and I wrote.

# # My sol'n
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

# # documentation sol'n
# def fib2(n):  # return Fibonacci series up to n
#     """Return a list containing the Fibonacci series up to n."""
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)    # see below
#         a, b = b, a+b
#     return result
#
# f100 = fib2(100)    # call it
# f100                # write the result
# # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

### This example seems important for us. Let's take a min to understand it better.
### Read paragraph at end of section 4.6 of https://docs.python.org/3/tutorial/controlflow.html#if-statements

# # function with some defaults
# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
#
# # giving only the mandatory argument:
# ask_ok('Do you really want to quit?')
#
# # giving one of the optional arguments:
# ask_ok('OK to overwrite the file?', 2)
#
# # giving all arguments:
#
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


### This is something different from R that we need to be careful of (I think)
# The default values are evaluated at the point of function definition in the defining scope, so that

# i = 5
# def f(arg=i):
#     print(arg)
#
# i = 6
# f()
# f()

# # the del function acts as negative indexing in R.
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# print(a)


# ### Sets
# # Python also includes a data type for sets.
# # A set is an unordered collection with no duplicate elements.
# # Basic uses include membership testing and eliminating duplicate entries.
# # Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
#
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)                      # show that duplicates have been removed
#
# print('orange' in basket)                 # fast membership testing
# #True
# print('crabgrass' in basket)
# #False
#
# # Demonstrate set operations on unique letters from two words
# a = set('abracadabra')
# b = set('alacazam')
# print(a)                                  # unique letters in a
# #{'a', 'r', 'b', 'c', 'd'}
# print(a - b)                              # letters in a but not in b
# #{'r', 'd', 'b'}
# print(a | b )                             # letters in a or b or both
# #{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
# print(a & b )                             # letters in both a and b
# #{'a', 'c'}
# print(a ^ b )                             # letters in a or b but not both
# #{'r', 'd', 'b', 'm', 'z', 'l'}



# ### Dictionary
# # It is best to think of a dictionary as a set of key: value pairs
#
# tel = {'jack': 4098, 'sape': 4139}
# tel['guido'] = 4127
# print(tel)
# #{'jack': 4098, 'sape': 4139, 'guido': 4127}
# print(tel['jack'])
# #4098
# del tel['sape']
# tel['irv'] = 4127
# print(tel)
# #{'jack': 4098, 'guido': 4127, 'irv': 4127}
# print(list(tel))
# #['jack', 'guido', 'irv']
# print(sorted(tel))
# #['guido', 'irv', 'jack']
# print('guido' in tel)
# #True
# print('jack' not in tel)
# #False