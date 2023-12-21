def two_sum(nums, target):
  """
  Finds all pairs of numbers in an array that add up to a target value.

  Args:
      nums: A list of integers.
      target: The target value.

  Returns:
      A list of pairs of integers that add up to the target value.
  """

  seen = {}  # Dictionary to store seen numbers and their indices
  pairs = []  # List to store the found pairs

  for i, num in enumerate(nums):
    complement = target - num

    # Check if the complement has been seen before
    if complement in seen:
      pairs.append((num, complement))

    # Add the current number to the seen dictionary, along with its index
    seen[num] = i

  return pairs