""" Solution 1: Filter ONLY Even numbers """

numbers = list(range(100))

def is_even(x):
    return x % 2 == 0

print(list(filter(is_even, numbers)))
