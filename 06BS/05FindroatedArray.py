def findKRotation(arr):
    n = len(arr)
    
    # If the entire array is already sorted, then no rotations.
    if arr[0] <= arr[n-1]:
        return 0

    low, high = 0, n - 1
    index = -1
    ans = float('inf')

    while low <= high:
        mid = (low + high) // 2

        # Instead of checking here if the subarray is sorted,
        # we rely on our binary search steps.
        if arr[low] <= arr[mid]:
            if arr[low] < ans:
                ans = arr[low]
                index = low
            low = mid + 1  # Move to the right half
        else:
            if arr[mid] < ans:
                ans = arr[mid]
                index = mid
            high = mid - 1  # Move to the left half

    return index

# Example run:
arr = [15, 34, 2, 3, 6, 12]  # This rotated sorted array was rotated 2 times.
print("Rotation count:", findKRotation(arr))
