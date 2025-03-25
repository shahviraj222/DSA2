# problem: choose the four element that sum is equal to target.

#method1: Brute Force
def _4sum(arr, target):
    n = len(arr)
    ans = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        temp = [arr[i], arr[j], arr[k], arr[l]]
                        temp = sorted(temp)
                        ans.add(tuple(temp))
    return ans

print(_4sum([1, 0, -1, 0, -2, 2], 0))

# method2: Looking For the Fourth Element
def _4sum2(arr, target):
    ans = set()
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            hashmap = set()  # Use a set for quick lookup
            for k in range(j+1, n):
                fourth = target - (arr[i] + arr[j] + arr[k])
                if fourth in hashmap:  # Check before inserting
                    temp = sorted([arr[i], arr[j], arr[k], fourth])
                    ans.add(tuple(temp))
                hashmap.add(arr[k])  # Insert arr[k] after checking
                
    return ans
print(_4sum2([1, 0, -1, 0, -2, 2], 0))

# method3: sort and two pointer
def _4sum3(arr, target):
    arr.sort()  # Sort array for two-pointer approach
    ans = set()
    n = len(arr)
    
    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:  # Skip duplicate `i`
            continue
        for j in range(i + 1, n):
            if j > i + 1 and arr[j] == arr[j - 1]:  # Skip duplicate `j`
                continue
            k, l = j + 1, n - 1
            
            while k < l:
                total = arr[i] + arr[j] + arr[k] + arr[l]  # Fixed typo
                
                if total > target:
                    l -= 1
                elif total < target:
                    k += 1
                else:
                    ans.add((arr[i], arr[j], arr[k], arr[l]))
                    k += 1
                    l -= 1
                    
                    # Corrected duplicate skipping
                    while k < l and arr[k] == arr[k - 1]:  
                        k += 1
                    while k < l and arr[l] == arr[l - 1]:  
                        l -= 1
                        
    return ans

# Test
def _4sum3(arr, target):
    arr.sort()  # Sort array for two-pointer approach
    ans = set()
    n = len(arr)
    
    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:  # Skip duplicate `i`
            continue
        for j in range(i + 1, n):
            if j > i + 1 and arr[j] == arr[j - 1]:  # Skip duplicate `j`
                continue
            k, l = j + 1, n - 1
            
            while k < l:
                total = arr[i] + arr[j] + arr[k] + arr[l]  # Fixed typo
                
                if total > target:
                    l -= 1
                elif total < target:
                    k += 1
                else:
                    ans.add((arr[i], arr[j], arr[k], arr[l]))
                    k += 1
                    l -= 1
                    
                    # Corrected duplicate skipping
                    while k < l and arr[k] == arr[k - 1]:  
                        k += 1
                    while k < l and arr[l] == arr[l + 1]:  
                        l -= 1
                        
    return ans

# Test
def _4sum3(arr, target):
    arr.sort()  # Sort array for two-pointer approach
    ans = set()
    n = len(arr)
    
    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:  # Skip duplicate `i`
            continue
        for j in range(i + 1, n):
            if j > i + 1 and arr[j] == arr[j - 1]:  # Skip duplicate `j`
                continue
            k, l = j + 1, n - 1
            
            while k < l:
                total = arr[i] + arr[j] + arr[k] + arr[l]  # Fixed typo
                
                if total > target:
                    l -= 1
                elif total < target:
                    k += 1
                else:
                    ans.add((arr[i], arr[j], arr[k], arr[l]))
                    k += 1
                    l -= 1
                    
                    # Corrected duplicate skipping
                    while k < l and arr[k] == arr[k - 1]:  
                        k += 1
                    while k < l and arr[l] == arr[l - 1]:  
                        l -= 1
                        
    return ans

# Test
print(_4sum3([1, 0, -1, 0, -2, 2], 0))



            