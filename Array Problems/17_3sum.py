# problem: Find the triplets, submition of element is zero
# you can't add the list in set you have to convert it into tuple

# method1:
def _3sum(arr):
    n = len(arr)
    s = set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k] == 0:
                    temp = [arr[i],arr[j],arr[k]]
                    temp = tuple(sorted(temp))
                    s.add(temp)
    return s

print(_3sum([-1,0,1,2,-1,-4]))

# method2: looking for the third element
def _3sum2(arr):
    n = len(arr)
    ans = set()
    for i in range(0,n):
        s = set()
        for j in range(i+1,n):
            third = -(arr[i]+arr[j])
            s.add(arr[j])
            if third in s:
                temp =[arr[i],arr[j],third]
                temp = tuple(sorted(temp))
                ans.add(temp)
    return ans

print(_3sum2([-1,0,1,2,-1,-4]))        

# method3: sort and two pointer 
def _3sum3(arr):
    arr = sorted(arr)
    n=len(arr)
    ans = set()
    for i in range(n):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        j = i+1
        k = n-1
        while j<k:
            sum = arr[i]+arr[j]+arr[k]
            if sum > 0:
                k-=1
            elif sum < 0:
                j+=1
            else:
                temp = [arr[i],arr[j],arr[k]]
                ans.add(tuple(temp))
                j+=1
                k-=1
                while arr[j-1] == arr[j]:
                    j+=1
                while arr[k-1] == arr[k]:
                    k-=1
    return ans
                    
print(_3sum3([-1,0,1,2,-1,-4]))       
