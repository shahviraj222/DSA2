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
def upperBound(arr,x):
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



