def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    # Merge both halves
    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # Copy remaining elements from left subarray
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # Copy remaining elements from right subarray
    while right <= high:
        temp.append(arr[right])  # Fixed: should append from the right subarray
        right += 1  # Fixed: should increment right, not left

    # Copy sorted elements back to original array
    for i in range(len(temp)):
        arr[low + i] = temp[i]  # Modify the original array in-place

def mergesort(arr, low, high):
    if low >= high:  # Base case correction
        return
    
    mid = (low + high) // 2
    mergesort(arr, low, mid)
    mergesort(arr, mid + 1, high)
    merge(arr, low, mid, high)

arr = [5, 60, 56, 34]
mergesort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
