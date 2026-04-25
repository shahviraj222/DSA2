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


