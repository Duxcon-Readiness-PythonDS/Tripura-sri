
import heapq

def find_kth_largest(nums, k):
  """
  Finds the kth largest number in a list using heapq.
  Args:
    nums: A list of numbers.
    k: The index of the desired largest number (1-based).
  Returns:
    The kth largest number in the list.
  """
  # Create a min-heap of size k to store the k largest elements seen so far.
  heap = heapq.nsmallest(k, nums)
  
  # Iterate through the rest of the list.
  for num in nums:
    # If the current number is larger than the smallest element in t
yyi-ybny-qem
