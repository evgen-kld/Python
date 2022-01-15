def quickSort(array):
    if len(array) < 2:
        return array
    else:
        base = array[0]
        less = [i for i in array[1:] if i <= base]
        greater = [i for i in array[1:] if i > base]
        return quickSort(less) + [base] + quickSort(greater)


print(quickSort([2, 1, 5, 8, 5, 7, 3]))