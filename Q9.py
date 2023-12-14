# Bit Manipulation:
# Write a program to check if a given number is even or odd using bit manipulation.

def even_or_odd(a):
    res = a & 1
    return res


# Write a program to find the number of set bits in a given integer using bit manipulation.
def set_bits(a, sum):
    if (a == 0):
        return sum
    temp = a >> 1
    sum = sum + even_or_odd(a)
    return set_bits(temp, sum)
