# array m-n more then one element is missing  (array is sorted)


# array is sorted
def findmissing(arr):
    diff = arr[0]
    missing = list()
    for i in range(0,len(arr)):
        while diff<(arr[i]-i):
            missing.append(diff+i)
            diff+=1
    return missing

print(findmissing([2,3,4,6,10]))     
