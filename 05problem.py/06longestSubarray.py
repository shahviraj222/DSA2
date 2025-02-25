# Problem 1 : find the longest subarray of sum = k

def findLongestSubarray(arr,s):
    lenth = 0
    sum = 0
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            for k in range(i,j+1):
                sum =sum+arr[k]
                if sum == s:
                    lenth = max(lenth,j-i+1)

    return lenth+1

print(findLongestSubarray([1,1,1,1,34,45,54,22],4))