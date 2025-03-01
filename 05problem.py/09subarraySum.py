# nums = [-2,1,-3,4,-1,2,1,-5,4]
# Problem: Find the maximum sum of subarray.

def subarrySum(nums):
    max = 0
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            sum = 0
            temp = []
            for k in range(i,j+1):
                temp.append(nums[k]) 
                sum+=nums[k]
                if max<sum:
                    maxsum = temp
                    max = sum 
            # print(temp)  
    print(maxsum)                  
    return max

print(subarrySum([5,4,-1,7,8])) 

def subarraySum2(nums):
    sum = 0
    max = float('-inf')
    startIndex = -1
    EndIndex = -1
    for i in range(0,len(nums)):
        if sum == 0:
            start = i
        sum += nums[i]
        
        if max<sum:
            startIndex = start
            EndIndex = i
            max = sum

        if sum<0:
            sum = 0
    return max

print(subarraySum2([5,4,-1,7,8]))
        
