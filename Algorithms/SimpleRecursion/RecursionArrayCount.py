def recursionArrayCount(array):
    if len(array) == 0:
        return 0
    return 1 + recursionArrayCount(array[1:])


print(recursionArrayCount([1, 3, 5, 2]))
