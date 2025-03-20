# problem: finding total number of subarray who's XOR is K

# method1:
def subarrayXorK(arr,k):
    count = 0
    for i in range(len(arr)):
        xor = 0
        for j in range(i,len(arr)):
            xor ^= arr[j]
            if xor == k:
                count+=1
    return count

print(subarrayXorK([4, 2, 2, 6, 4],6))

# method2:

