##Arrays and Strings:
#Write a program to reverse a string in place.

def reverse_string(s):
    # Convert the string to a list for in-place manipulation
    s_list = list(s)

    # Use two pointers approach to reverse the string in-place
    left, right = 0, len(s_list) - 1
    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1

    # Convert the list back to a string
    reversed_string = ''.join(s_list)
    return reversed_string
# Write a program to find the maximum and minimum elements in an array.

def find_max_min(arr):
    if not arr:
        return None, None  # Return None for empty array

    # Initialize max and min with the first element of the array
    max_element = min_element = arr[0]

    # Iterate through the array to find the maximum and minimum elements
    for num in arr:
        if num > max_element:
            max_element = num
        elif num < min_element:
            min_element = num

    return max_element, min_element
#Write a program to remove duplicates from a sorted array.

def remove_duplicates(arr):
    if not arr:
        return []  # Return an empty list for empty array

    # Use two pointers to track unique elements
    unique_index = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[unique_index]:
            unique_index += 1
            arr[unique_index] = arr[i]

    # Slice the array to get the result with unique elements
    unique_array = arr[:unique_index + 1]
    return unique_array


