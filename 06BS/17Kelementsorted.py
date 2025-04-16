# problem: find the Kth sorted element from two array

def findKthElement(arr1, arr2, k):
    n1 = len(arr1)
    n2 = len(arr2)
    
    # Always binary search on the smaller array
    if n1 > n2:
        return findKthElement(arr2, arr1, k)
    
    low = max(0, k - n2)
    high = min(k, n1)

    while low <= high:
        mid1 = (low + high) // 2
        mid2 = k - mid1

        l1 = float('-inf') if mid1 == 0 else arr1[mid1 - 1]
        l2 = float('-inf') if mid2 == 0 else arr2[mid2 - 1]
        r1 = float('inf') if mid1 == n1 else arr1[mid1]
        r2 = float('inf') if mid2 == n2 else arr2[mid2]

        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    
    return -1  # should not reach here if k is valid

# Example usage:
print("3rd smallest element:", findKthElement([1, 3, 5], [2, 4, 6], 3))  # Output: 3
print("5th smallest element:", findKthElement([2, 3], [1, 4, 5, 6], 5))  # Output: 5


