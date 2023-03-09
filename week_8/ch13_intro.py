# beyond basic python - course requirement and continuing learning
import numpy as np

# numpy array
a_list = [1, 2, 3]
a_array = np.array(a_list)

# print(a_list)
# print(a_array)
# print(a_array.size)
# print(a_array.shape)


# create an array
## 1D array vs list

# print(np.zeros(10))
# print(np.ones(10) * 2)

## 2D array vs list of lists
# print(   np.zeros([2,3]).astype(int)  )


# a = [ [1,2,3], [4,5,6] ]
# print(a)
# print(np.array(a))

## nD array vs list of lists of lists...
# a = [ [ [1,2,3], [4,5,6] ], [[1,2,3], [4,5,6]] ]
# print('-'*20)
# print(np.array(a).shape)


# indexing and slicing, nD
# a = [ [1,2,3], [4,5,6] ]
# print(a[0][0])
# a_array = np.array(a)
# # print(a_array[0,0])
#
# print(a_array[0,:])  # print row 0
#
# b = np.array(range(20))
# c = b.reshape(4,5)
# print(c)
# #PRINT row 2-3, col 3 -5
# print('\n')
# print(c[ 2:4, 3:6])
# print(c[:, 0])

# Arithmetic operation (element-wise) relational operation and some useful methods
a = np.arange(4)
# b = np.linspace(2,5, a.size)
# print(a)
# print(b)
# print(a * 10)


# -----------------beyond textbook--------------
# broadcasting
# b = np.arange(9).reshape(3,3)
# c = np.ones(3) * 10
# print(b)
# print(c)
# print( b + c)
# print('-'*20)
# print(b * c)


# clone with [:] or .copy()?
# a = [1,2,3]
# b = a
# b[0] += 100
# print(a)
# print(b)

# a = [1,2,3]
# b = a[:]   # b is a clone of a
# b[0] += 100
# print(a)
# print(b)

# a = np.array([1,2,3])
# b = a[:]   # b is NOT a clone of a, it is a slice view of a
b = a.copy()  # this is a clone
b[0] += 100
print(a)
print(b)