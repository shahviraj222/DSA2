# Problem: Find the row which contain maximum no of 1s (2d Matrix)
def findnoones(arr):
    low = 0
    high = len(arr)-1
    ans = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>=1:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans        

def findMaxOne(arr):
    n = len(arr)       #column
    m = len(arr[0])    #row
    maxcount = -1
    index = -1
    for i in range(n):
        countnow = m-findnoones(arr[i])
        if countnow>maxcount:
            maxcount = countnow
            index = i    
    return index

print("index of the row:",findMaxOne([[0,0,0,1,1,1,1],
            [0,0,0,0,0,1,1],
            [0,0,1,1,1,1,1],
            [1,1,1,1,1,1,1]]))