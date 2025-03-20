# problem: return max length of subarray who's summation is zero.

# method1:Brute force
def maxlen(arr):
    max_length = 0  # Use a different variable name
    n = len(arr)
    
    for i in range(n):
        current_sum = 0  # Reset sum for each subarray
        
        for j in range(i, n):  # Start from `i`
            current_sum += arr[j]
            
            if current_sum == 0:
                length = j - i + 1  # Corrected subarray length
                
                if length > max_length:
                    max_length = length
    
    return max_length  # Return max length found
          
print(maxlen([15, -2, 2, -8, 1, 7, 10, 23]))

# method2: using prefix sum .
def maxlen2(arr):
    hashmap={}
    maxi = 0
    prefix_sum = 0
    for i in range(len(arr)):
        prefix_sum+=arr[i]
        if prefix_sum == 0:
            maxi = i+1
        
        if prefix_sum in  hashmap:
            maxi = max(maxi,i-hashmap[prefix_sum])

        else:
            hashmap[prefix_sum] = i

    return maxi


print(maxlen2([15, -2, 2, -8, 1, 7, 10, 23]))