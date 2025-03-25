# problem: find the largest product from subarray 

# method1:Brute force
def subarrayProduct(arr):
    max = float('-inf')
    for i in range(len(arr)):
        product = 1
        for j in range(i,len(arr)):
            product*=arr[j]
            if product>max:
                max = product
    return max

print(subarrayProduct([2,3,-2,4]))       

# method2: observation method

def subarrayProduct2(arr):
    maxi = float('-inf')
    prefix = 1
    suffix = 1
    for i in range(len(arr)):
        # resetting prefix and suffix
        if prefix == 0:
            prefix = 1

        if suffix == 0:
            suffix = 1

        prefix *= arr[i]
        suffix *= arr[len(arr)-1-i] 

        maxi = max(maxi,max(prefix,suffix))

    return maxi

print(subarrayProduct([2,3,-2,4]))               