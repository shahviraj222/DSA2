# Problem: peak element is the one that is grater then all four sides.
def maxElement(arr, col):
    max_val = float('-inf')
    max_row = 0
    for i in range(len(arr)):
        if arr[i][col] > max_val:
            max_val = arr[i][col]
            max_row = i
    return max_row

def peakElement(arr):
    m = len(arr)
    n = len(arr[0])
    low = 0
    high = n - 1
    while low<=high:
        mid = (low+high)//2
        row = maxElement(arr,mid)

        if mid-1>=0:
            left = arr[row][mid-1]
        else:
            left = -1

        if mid+1<n:
            right = arr[row][mid+1]
        else:
            right = -1

        if arr[row][mid]>left and arr[row][mid]>right:
            return row,mid
        elif arr[row][mid]<left:
            high = mid - 1
        else:
            low = mid + 1    

    return -1,-1

print(peakElement([[1,4],[3,2]]))

