def kthMissing(arr,k):
    for i in range(len(arr)):
        if arr[i]<=k:
            k+=1
        else:
            break
    return k     

print(kthMissing([1,2,3,4],2))   

def kthMissing2(arr,k):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        missing = arr[mid] - (mid+1)
        if missing<k:
            low = mid + 1
        else:
            high = mid - 1    
    return low+k        

print(kthMissing2([1,2,3,4],2))   
