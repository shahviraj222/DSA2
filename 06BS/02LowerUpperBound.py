# problem1 Lower Bound : smallest index such that arr[index] >= x 

def lowerBound(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

print("Index:",lowerBound([1, 2, 8, 10, 10, 12, 19],9))            


# problem2 UpperBound: smallest index such that arr[index] > x
def upperBound(arr,x)->int:
    n = len(arr)
    low = 0 
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid]>x:
            ans = mid
            high = mid -1 
        else:
            low = mid +1
    return ans        


print("Index:",upperBound([1, 2, 8, 9, 10, 12, 19],9))      



# problem3: Find the occurance of the element
def countFreq(arr, target):
    # Code here
    n = len(arr)
    low = 0
    high = n - 1
    first = -1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    if first == -1:
        return 0

    low = 0
    high = n - 1
    last = -1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last = mid
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return last - first + 1


print(countFreq([1, 2, 2, 2, 3, 4, 5], 2))  # Output: 3
