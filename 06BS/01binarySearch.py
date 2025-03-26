# if you find the which side to eliminate in the array your task is done.
def binarySearch(arr,target):
    low = 0
    high = len(arr)-1
    mid = (low + high) // 2
    while low<=high:
        mid = (low + high ) //2
        if arr[mid] == target:
            return mid
        elif arr[mid]>target:
            high = mid - 1
        else:
            low = mid + 1    
    return -1

print(binarySearch([1,32,45,67,90],90))            