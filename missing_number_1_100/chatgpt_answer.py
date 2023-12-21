import time

def find_missing_numbers(arr):
    # Create a set of the given array for faster lookup
    num_set = set(arr)

    missing_numbers = []
    # Check numbers from 1 to 100
    for num in range(1, 101):
        if num not in num_set:  # If the number is not in the set, it's missing
            missing_numbers.append(num)

    return missing_numbers

