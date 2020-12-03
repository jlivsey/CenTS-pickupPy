# By default, arguments may be passed to a Python function either by position or explicitly by keyword.
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# Valid ways to call the parrot( ) function
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# # Invalid ways to call the parrot( ) function
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument


# If / and * are not present in the function definition, arguments may be passed to a function by position or by keyword.
# Use / for positional only function args
# Use * for keyword function args
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(2)

standard_arg(arg=2)

pos_only_arg(1)

pos_only_arg(arg=1)

kwd_only_arg(3)

kwd_only_arg(arg=3)

combined_example(1, 2, 3)

combined_example(1, 2, kwd_only=3)

combined_example(1, standard=2, kwd_only=3)

combined_example(pos_only=1, standard=2, kwd_only=3)
