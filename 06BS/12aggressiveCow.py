# Problem: Aggressive cow : find the minimum distance between two cow that is maximum.
def canWePlace(arr,dist,cows):
    countcows = 1
    lastcow = arr[0]  
    for i in range(1,len(arr)):
        if arr[i]- lastcow >= dist:
            countcows+=1
            lastcow = arr[i]

    if countcows>=cows:
        return True
    
    return False        


def aggressiveCow(arr,cows):
    arr.sort()
    for i in range(1,max(arr)-min(arr)):
        if canWePlace(arr,i,cows):
            continue
        else:
            return i-1
        
def aggressiveCow(arr,cows):
    arr.sort()
    low = 1
    high = arr[len(arr)-1]-arr[0]
    while low<=high:
        mid = (low+high)//2
        if canWePlace(arr,mid,cows):
            low = mid+1
        else:
            high = mid-1
 
    return high




