# Searching Algorithms:
# Implement the linear search algorithm.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if the target is not in the array


# Implement the binary search algorithm.

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Return the index of the target if found
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if the target is not in the array
