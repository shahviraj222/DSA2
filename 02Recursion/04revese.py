def reversearray(n):
    if len(n) <=1 :
        return n
    return reversearray(n[1:])+[n[0]]

# write on paper then you understand what is happening
# python (n[1:])+ [n[0]] joint is happeing here


def reversearray2(arr):
    if len(arr)>1:
        num = reversearray2(arr[1:])
        num.append(arr[0])
    else:
        return arr
    
    return num

print(reversearray2([1,2,3]))

print(reversearray([23,24,25]))

# Time complexity O(n) draw tree of recursive call.