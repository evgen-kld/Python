def binary_search(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = array[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


array = list(range(1000))
print(binary_search(array, 6))
