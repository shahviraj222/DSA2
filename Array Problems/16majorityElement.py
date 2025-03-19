# find the element whoes value > n/3

# method1:

def majority(arr):
    map = {}
    ans = set()
    min = len(arr)//3 + 1
    for i in arr:
        if i in map:
            map[i]+=1
            if map[i]>=min:
                ans.add(i)
        else:
            map[i]=1      

        if len(ans) >= 2:
            break
    return sorted(ans)  


print(majority([3,2,3,2]))

# time complexity O(n)  space complexity O(n)


# method2: On the basis of Moones voting algorithm 

def majorityMonnes(arr):
    # moones algo slightly modify for the 2 element 
    count1 = 0 
    count2 = 0
    element1 = float('-inf')
    element2 = float('-inf')
    ans = []
    for i in range(len(arr)):
        if count1 == 0 and arr[i] != element2:
            element1 = arr[i]
            count1 = 1

        elif count2 == 0 and arr[i] != element1:
            element2 = arr[i]
            count2 = 1

        elif element1 == arr[i]:
            count1+=1

        elif element2 == arr[i]:
            count2+=1

        else:
            count1-=1
            count2-=1

    count1 = 0

    for i in arr:
        if element1 == i:
            count1+=1
    if count1 > len(arr) // 3:
        ans.append(element1)   

    count2 = 0
    for i in arr:
        if element2 == i:
            count2+=1
    if count2 > len(arr) // 3:
        ans.append(element2)   

    return ans    

print(majorityMonnes([3,2,3]))    

