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

def findLongestSubarray2(arr,s):
    length = 0
    for i in range(0,len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum+=arr[j]
            if sum == s:
                length = max(length,j-i+1)

    return length             

print(findLongestSubarray2([1,1,1,1,34,45,54,22],4))

# Problem2 : Find the index of two nums to get target sum

# methode 1:BruteForce
def targetTwo(arr,target):
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            if target == arr[i]+arr[j]:
                return [i,j]


print(targetTwo([1,32,3,9],12))

# methode 2: Hashmap
def targetTwo2(arr,target):
    map = {}
    for i in range(0,len(arr)):
        remaining = target-arr[i]
        if remaining in map:
            return [i,map[remaining]]
        else:
            map[arr[i]] = i

print(targetTwo2([1,32,3,9],12))
# Time Complexity is O(n)
# Space Complexity is O(n)
