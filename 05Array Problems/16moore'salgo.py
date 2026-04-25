# problem : element apper more then n//2 times

# moore's algo work only if element is n//2 means half of array

def moorealgo(arr):
    count = 0
    for i in arr:
        if count == 0:
            element = i
            count+=1
        elif i == element:
            count+=1
        else:
            count-=1 
    return element        

print(moorealgo([1,2]))


# stock market problem

def stock(arr):
    min = float("inf")
    max = float("-inf")
    for i in arr:
        if min>i:
            min = i
        if max < i - min:
            max = i - min
    return max if max > 0 else 0
            
print(stock([1,23,3,234,1]))