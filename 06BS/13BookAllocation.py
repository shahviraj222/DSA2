# problem: You have to allocate the book to ‘m’ students such that the maximum number of pages assigned to a student is minimum.

def findStudent(arr,pages):
    student = 1
    studentpages = 0
    for i in range(len(arr)):
        if studentpages+arr[i]<= pages:
            studentpages+=arr[i]
        else:
            student+=1
            studentpages = arr[i]
    return student
            
def allocationBook(arr,student):
    if len(arr)<student:
        return -1
    low = max(arr)
    high = sum(num for num in arr)
    for pages in range(low,high):
        countStudent = findStudent(arr,pages)
        if countStudent==student:
            return pages
        
print(allocationBook([12, 34, 67, 90],2))        
# time complexity : O(high-low*N)

def allocationBook2(arr,student):
    low = max(arr)
    high = sum(num for num in arr)
    while low<=high:
        mid = (low+high)//2
        countStudent =findStudent(arr,mid)
        if countStudent>student:
            low = mid+1
        else:
            high = mid-1
    return low        

print(allocationBook2([12, 34, 67, 90],2))  
# (log(high-low)*N)