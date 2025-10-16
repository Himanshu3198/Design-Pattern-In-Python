import numpy as np


def basic_ops():
    a = np.array([[1, 3, 4, 5, 2], [2, 4, 6, 1, 2], [2, 4, 6, 1, 2]])

    row, col = a.shape
    print(f"row={row},col={col}")
    print(f"ndim=no. of dimension,{a.ndim}")
    print(f"totalNoElement={a.size}")



def array_ops():
    a = np.array([13,2,3])
    a.sort()
    print(a)
    a = a[::-1]


def two_array_ops():
    a = np.array([[1,3,6],[2,4,1]])
    b = np.array([4,2,2])
    c = a*b
    print(c)




if __name__ == "__main__":
    # array_ops()
    two_array_ops()


