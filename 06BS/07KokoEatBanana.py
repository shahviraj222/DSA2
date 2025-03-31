# problem : find the minimum (kth banana / hour) such that all banana is complete
import math

def findTimeTaken(arr,i):
    totalhr = 0
    for j in range(len(arr)-1):
        totalhr += math.ceil(arr[j]/i)
    return totalhr    

# methode 1: BruteForce
def kokoEatingBanana(arr,hour):
    for i in range(1,max(arr)):
        requireTime = findTimeTaken(arr,i)
        if requireTime<=hour:
            return requireTime


# methode 2: Binary Search
def kokoEatingBanana2(arr,hour):
    low = 1
    high = max(arr)
    while low<=high:
        mid = (low+high)//2 
        requiredTime = findTimeTaken(arr,mid)
        if requiredTime<=hour:
            ans = requiredTime
            high = mid -1
        else:
            low = mid+1
    return low

print(kokoEatingBanana2([3,6,7,11],8) )               