# problem: Inversion Count indicates how far (or close) the array is from being sorted. 
# arr[i] > arr[j] and i < j ==  left element is always grater

#you have to explicitly declaring count as global.


# method1: Brurt Force
def countInversion(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                count+=1

    return count 

print(countInversion([2, 4, 1, 3, 5]))
# time complexity O(n^2)

# method2: mergesort based
count = 0
def merge(arr, low, mid, high):
    global count
    # consider two array as below
    # a = low to mid
    # b = mid+1 to high
    # c = merging both

    temp = []
    left = low
    right = mid + 1

    # Merge both halves
    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
    # right is smaller
        else:
            count+=(mid-left+1)
            temp.append(arr[right])
            right += 1

    # Copy remaining elements from left subarray
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # Copy remaining elements from right subarray
    while right <= high:
        temp.append(arr[right]) 
        right += 1 

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


def countInversion2(arr):
    n = len(arr)
    mergesort(arr,0,n)
    return count

           
countInversion2([2, 4, 1, 3, 5])           
# time comeplexity O(nlogn)