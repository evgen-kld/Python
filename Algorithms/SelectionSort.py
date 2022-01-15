def findSmallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(0, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selectionSort(array):
    newArray = []
    for _ in range(0, len(array)):
        smallest = findSmallest(array)
        newArray.append(array.pop(smallest))
    return newArray


print(selectionSort([9, 7, 4, 86, 22, 55]))
