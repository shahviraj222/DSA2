# problem: find the minimum capacity of the ship so that all packages are shipped.
 
def findDay(arr,capacity):
    day = 1
    load = 0
    for i in range(0,len(arr)):
        if load+arr[i]>capacity:
            day += 1
            load = arr[i]
        else:
            load+=arr[i]

    return day            

def shippingDay(arr,day):
    total = sum(num for num in arr)
    for i in range(max(arr),total):
        requireDay = findDay(arr,i)
        if requireDay<=day:
            return i
        

print(shippingDay([1,2,3,4,5,6,7,8,9,10],5))


def shippingDay2(arr,day):
    total = sum(num for num in arr)
    low = max(arr)
    high = total
    while low<=high:
        mid = (low + high)//2
        requireDay = findDay(arr,mid)
        if requireDay<=day:
            high=mid-1
        else:
            low = mid+1
    return low

print(shippingDay2([1,2,3,4,5,6,7,8,9,10],5))         