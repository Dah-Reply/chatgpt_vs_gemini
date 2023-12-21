import numpy as np

def find_missing_numbers(arr):
  """
  Finds all missing numbers in a given integer array of 1 to 100.

  Args:
      arr: A NumPy array of integers.

  Returns:
      A NumPy array of missing numbers.
  """

  # Create a set of all numbers from 1 to 100 for efficient comparison.
  all_numbers = set(range(1, 101))

  # Convert the input array to a set for faster set operations.
  present_numbers = set(arr)

  # Find the missing numbers by taking the difference between the sets.
  missing_numbers = all_numbers.difference(present_numbers)

  # Convert the missing numbers set back to a NumPy array and sort it.
  missing_numbers = np.array(sorted(missing_numbers))

  return missing_numbers