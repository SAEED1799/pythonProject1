# Recursion:
# Write a program to calculate the factorial of a number using recursion.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Write a program to generate all permutations of a string using recursion.

def generate_permutations(s):
    if len(s) == 1:
        return [s]

    result = []
    for i, char in enumerate(s):
        remaining_chars = s[:i] + s[i + 1:]
        for perm in generate_permutations(remaining_chars):
            result.append(char + perm)

    return result
