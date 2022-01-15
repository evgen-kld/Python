def recursionArrayMax(array):
    biggest = array[0]
    if len(array) == 1:
        return array[0]
    if biggest > recursionArrayMax(array[1:]):
        return biggest
    else:
        return recursionArrayMax(array[1:])


print(recursionArrayMax([1, 3, 5, 2]))
