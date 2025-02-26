def targetTwo(arr,target):
    map = {}
    for i in range(0,len(arr)):
        remaining = target-arr[i]
        if remaining in map:
            return [i,map[remaining]]
        else:
            map[arr[i]] = i

print(targetTwo([1,32,3,9],12))