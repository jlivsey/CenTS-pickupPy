#!/usr/bin/env python
# coding: utf-8

# Numpy is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays.
# 
# This script was modified from the original at (https://cs231n.github.io/python-numpy-tutorial/)

# In[1]:


import numpy as np


# In[2]:


a = np.array([1, 2, 3])   # Create a rank 1 array
type(a)        


# In[3]:


a.shape


# In[4]:


print(a[0], a[1], a[2])


# In[5]:


a[0] = 5
a


# In[6]:


b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array

print(b.shape)                     # Prints "(2, 3)"

print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"


# ## Array Creation

# In[7]:


a = np.zeros((2,2))   # Create an array of all zeros
print(a)             


# In[8]:


b = np.ones((1,2))    # Create an array of all ones
print(b)             


# In[9]:


c = np.full((2,2), 7)  # Create a constant array
print(c)               


# In[10]:


d = np.eye(2)         # Create a 2x2 identity matrix
print(d)             


# In[11]:


e = np.random.random((2,2))  # Create an array filled with random values
print(e)                     


# ## Array Indexing

# In[12]:


## Array indexing
#Numpy offers several ways to index into arrays.
# Slicing: Similar to Python lists, numpy arrays can be sliced. 
# Since arrays may be multidimensional, you must specify a slice for each dimension of the array:

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
a


# In[13]:


# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]
b


# In[14]:


# A slice of an array is a view into the same data, so modifying it
# will modify the original array.
print(a[0, 1])   # Prints "2"
b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])   # Prints "77"


# In[15]:


# You can also mix integer indexing with slice indexing. 
# Doing so will yield an array of lower rank than the original array. 

# Two ways of accessing the data in the middle row of the array.
# Mixing integer indexing with slices yields an array of lower rank,
# while using only slices yields an array of the same rank as the
# original array:
row_r1 = a[1, :]    # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)  
print(row_r2, row_r2.shape)  


# In[16]:


# We can make the same distinction when accessing columns of an array:
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)  
print(col_r2, col_r2.shape)  


# In[17]:


## Integer array indexing:

# When you index into numpy arrays using slicing, the resulting array view 
# will always be a subarray of the original array. 
# In contrast, integer array indexing allows you to construct arbitrary arrays 
# using the data from another array. 

a = np.array([[1,2], [3, 4], [5, 6]])

# An example of integer array indexing.
# The returned array will have shape (3,) and
print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"


# In[18]:


# The above example of integer array indexing is equivalent to this:
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # Prints "[1 4 5]"


# In[19]:



# When using integer array indexing, you can reuse the same
# element from the source array:
print(a[[0, 0], [1, 1]])  # Prints "[2 2]"


# In[20]:



# Equivalent to the previous integer array indexing example
print(np.array([a[0, 1], a[0, 1]]))  # Prints "[2 2]"


# In[21]:


# One useful trick with integer array indexing is selecting 
# or mutating one element from each row of a matrix:

# Create a new array from which we will select elements
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])

print(a) 


# In[22]:


# Create an array of indices
b = np.array([0, 2, 0, 1])

# Select one element from each row of a using the indices in b
print(a[np.arange(4), b])  # Prints "[ 1  6  7 11]"


# In[23]:


# Mutate one element from each row of a using the indices in b
a[np.arange(4), b] += 10

print(a)  


# In[24]:


## Boolean array indexing: 

a = np.array([[1,2], [3, 4], [5, 6]])

bool_idx = (a > 2)   # Find the elements of a that are bigger than 2;
                     # this returns a numpy array of Booleans of the same
                     # shape as a, where each slot of bool_idx tells
                     # whether that element of a is > 2.

print(bool_idx)      # Prints "[[False False]
                     #          [ True  True]
                     #          [ True  True]]"


# In[25]:


# We use boolean array indexing to construct a rank 1 array
# consisting of the elements of a corresponding to the True values
# of bool_idx
print(a[bool_idx])  # Prints "[3 4 5 6]"


# In[26]:



# We can do all of the above in a single concise statement:
print(a[a > 2])     # Prints "[3 4 5 6]"


# ## Array Math

# In[27]:


# Basic mathematical functions operate elementwise on arrays.
# and are available both as operator overloads and as functions in the numpy module:

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))


# In[28]:


# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))


# In[29]:



# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))


# In[30]:



# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))


# In[31]:



# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))


# In[32]:


# In MATLAB, * is elementwise multiplication (not matrix multiplication). 
# We instead use the `dot` function to compute inner products of vectors, 
# to multiply a vector by a matrix, and to multiply matrices. 
# `dot` is available both as a function in the numpy module and as an instance method of array objects:

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))


# In[33]:



# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))


# In[34]:


# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))


# In[35]:


# using `sum`

x = np.array([[1,2],[3,4]])

print(np.sum(x))  # Compute sum of all elements; prints "10"


# In[36]:


print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"


# In[37]:


print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"


# In[38]:


# transpose 

x = np.array([[1,2], [3,4]])
print(x)    
print(x.T)  


# In[39]:


# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1,2,3])
print(v)    # Prints "[1 2 3]"
print(v.T)  # Prints "[1 2 3]"


# In[40]:


# add a constant vector to each row of a matrix. We could do it like this:

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)   # Create an empty matrix with the same shape as x

# Add the vector v to each row of the matrix x with an explicit loop
for i in range(4):
    y[i, :] = x[i, :] + v

# Now y is the following
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]
print(y)


# In[41]:


# This works; however when the matrix x is very large, 
# computing an explicit loop in Python could be slow. 

# Stack v and perform elementwise addition

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1))   # Stack 4 copies of v on top of each other
print(vv)                 # Prints "[[1 0 1]
                          #          [1 0 1]
                          #          [1 0 1]
                          #          [1 0 1]]"
y = x + vv  # Add x and vv elementwise
print(y)  # Prints "[[ 2  2  4
          #          [ 5  5  7]
          #          [ 8  8 10]
          #          [11 11 13]]"


# In[42]:


# Numpy **broadcasting** allows us to perform this computation without 
# creating multiple copies of v. 

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v  # Add v to each row of x using broadcasting
print(y)  # Prints "[[ 2  2  4]
          #          [ 5  5  7]
          #          [ 8  8 10]
          #          [11 11 13]]"


# Broadcasting two arrays together follows these rules:
# 
# 1. If the arrays do not have the same rank, prepend the shape of the lower rank array with 1s until both shapes have the same length.
# 2. The two arrays are said to be compatible in a dimension if they have the same size in the dimension, or if one of the arrays has size 1 in that dimension.
# 3. The arrays can be broadcast together if they are compatible in all dimensions.
# 4. After broadcasting, each array behaves as if it had shape equal to the elementwise maximum of shapes of the two input arrays.
# 5. In any dimension where one array had size 1 and the other array had size greater than 1, the first array behaves as if it were copied along that dimension
# 
# Functions that support broadcasting are known as _universal functions_.

# In[43]:


# Applications of broadcasting

# Compute outer product of vectors
v = np.array([1,2,3])  # v has shape (3,)
w = np.array([4,5])    # w has shape (2,)
# To compute an outer product, we first reshape v to be a column
# vector of shape (3, 1); we can then broadcast it against w to yield
# an output of shape (3, 2), which is the outer product of v and w:
# [[ 4  5]
#  [ 8 10]
#  [12 15]]
print(np.reshape(v, (3, 1)) * w)


# In[44]:


# Add a vector to each row of a matrix
x = np.array([[1,2,3], [4,5,6]])
# x has shape (2, 3) and v has shape (3,) so they broadcast to (2, 3),
# giving the following matrix:
# [[2 4 6]
#  [5 7 9]]
print(x + v)


# In[45]:



# Add a vector to each column of a matrix
# x has shape (2, 3) and w has shape (2,).
# If we transpose x then it has shape (3, 2) and can be broadcast
# against w to yield a result of shape (3, 2); transposing this result
# yields the final result of shape (2, 3) which is the matrix x with
# the vector w added to each column. Gives the following matrix:
# [[ 5  6  7]
#  [ 9 10 11]]
print((x.T + w).T)


# In[46]:


# Another solution is to reshape w to be a column vector of shape (2, 1);
# we can then broadcast it directly against x to produce the same
# output.
print(x + np.reshape(w, (2, 1)))


# In[48]:



# Multiply a matrix by a constant:
# x has shape (2, 3). Numpy treats scalars as arrays of shape ();
# these can be broadcast together to shape (2, 3), producing the
# following array:
# [[ 2  4  6]
#  [ 8 10 12]]
print(x * 2)


# In[ ]:





# In[ ]:




