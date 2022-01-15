def recursionSum(array):
    if len(array) == 0:
        return 0
    return array[0] + recursionSum(array[1:])


print(recursionSum([1, 3, 5, 2]))
