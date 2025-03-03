def longestconsequtiveBrute(arr):
    max = 0
    for i in range(0,len(arr)):
        count = 1
        num = arr[i]+1
        while num in arr:
            num = num +1
            count+=1
        if max < count:
            max = count
    return max


print(longestconsequtiveBrute([100,4,200,1,3,2,5,6,0]))