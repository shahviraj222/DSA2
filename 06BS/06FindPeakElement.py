# problem: find the peakelement arr[n-1]< arr[n] > arr[n+1]
# In an OR condition, if the first condition is True, the second condition is not evaluated.

from typing import List

def findPeakElement(arr):
    for i in range(len(arr)):
        if ( i == 0 or arr[i-1]<arr[i]) and (i==len(arr)-1 or arr[i]>arr[i+1]):
            return arr[i]

print("peak element:",findPeakElement([1,2,3,1]))       

def findPeakElement2(nums: List[int]) -> int:
    n = len(nums)

    # Edge case: If there is only one element, return its index
    if n == 1:
        return 0

    # Check if the first or last element is a peak
    if nums[0] > nums[1]:
        return 0
    if nums[n - 1] > nums[n - 2]:
        return n - 1

    low = 1
    high = n - 2  # We exclude first and last elements since they are already checked

    while low <= high:
        mid = (low + high) // 2

        # Check if the middle element is a peak
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid

        # If on an increasing slope, move right
        elif nums[mid] > nums[mid - 1]:
            low = mid + 1

        # Otherwise, move left
        else:
            high = mid - 1

    return -1        

print("peak index:",findPeakElement2([1,2,3,1]))