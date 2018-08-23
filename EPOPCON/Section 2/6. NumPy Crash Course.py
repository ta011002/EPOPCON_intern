import numpy as np

mylist = [1, 2, 3, 4]
print(np.array(mylist))
print(mylist)
print(type(mylist))

arr = np.array(mylist)
print(type(arr))
print(arr)

a = np.arange(0, 10)
a

a = np.arange(0, 10, 2)
a

np.zeros((5, 5))

np.zeros((1, 10))

np.zeros((2, 10))

np.ones((2, 4))

print(type(1.0))
print(type(1.))
print(type(1))

for i in range(5):
    print(np.random.randint(0, 100))

np.random.randint(0, 100, (5, 5))

np.linspace(0, 10, 6)

np.linspace(0, 10, 101)

np.linspace(0, 10, 200)

np.random.seed(101)

np.random.randint(0, 100, 10)

arr = np.random.randint(0, 100, 10)
arr

print(arr.max())
print(arr.min())
print(arr.mean())
print(arr.argmax())
print(arr.argmin())

arr.reshape(2, 5)

mat = np.arange(0, 100).reshape(10, 10)
mat

print(mat[5, 2])
print(mat[:, 2])
print(mat[2, :])

mat > 50

mat[mat > 50]