# problem : find the smallest divisor so that sumbition is less than and equal to thresold

# sum(math.ceil(num / mid) for num in arr)            this return a generator object that sum can handle
# print(1+i for i in [5,6,7])                         this will not work
# print(list(1+i) for i in [5,6,7])                   this will work as intended

import math
def findDivisor(arr,t):
    for i in range(1,max(arr)):
        sum = 0
        for j in range(0,len(arr)):
            sum+=math.ceil(arr[j]/i)
        if sum<=t:
            return i 
    return -1       


print(findDivisor([1,2,5,9],6))


import math

def findDivisor2(arr, t):
    low = 1
    high = max(arr)
    answer = high  # worst case, max(arr)

    while low <= high:
        mid = (low + high) // 2
        total = sum(math.ceil(num / mid) for num in arr)

        if total <= t:
            answer = mid  # potential answer, try to minimize it
            high = mid - 1
        else:
            low = mid + 1

    return answer

print(findDivisor2([1, 2, 5, 9], 6))
