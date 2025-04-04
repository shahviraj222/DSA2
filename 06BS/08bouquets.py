# problem: Find the minimum day at which you can make mth bouque with kth adjacent flower
def possible(arr, day, m, k):
    count = 0
    ans  =  0
    for i in range(len(arr)):
        if arr[i] <= day:
            count += 1
        else:
            ans += (count // k)  # Fix: Use integer division
            count = 0
    ans += (count // k)  # Fix: Count the last possible bouquet

    if ans >= m:  # Fix: Should be '>=', not '>'
        return True
    return False           
        
def findDay(arr, m, k):
    if m * k > len(arr):
        return -1
    for i in range(min(arr), max(arr) + 1):
        if possible(arr, i, m, k):  # No need for '== True'
            return i
    return -1    

print(findDay([1, 10, 3, 10, 2], 3, 1))


def findDay2(arr,m,k):
    ans = -1
    if m * k > len(arr):
        return -1  
    low = min(arr)
    high = max(arr)
    while(low<=high):
        mid = (low+high)//2
        if possible(arr,mid,m,k):
            ans = mid
            high = mid -1
        else:
            low = mid+1
    return ans


print(findDay2([1, 10, 3, 10, 2], 3, 1))