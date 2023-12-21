def find_missing_numbers(nums):
  """
  Finds all missing numbers in a given integer array of 1 to 100 without using external libraries.

  Args:
      nums: An integer array containing numbers between 1 and 100.

  Returns:
      A list of missing numbers in the given array.
  """

  # Create a bitmap to mark the presence of each number.
  bitmap = [0] * 101

  # Mark the presence of each number in the array.
  for num in nums:
    bitmap[num] = 1

  # Find and return the missing numbers.
  missing_numbers = []
  for i in range(1, 101):
    if not bitmap[i]:
      missing_numbers.append(i)

  return missing_numbers