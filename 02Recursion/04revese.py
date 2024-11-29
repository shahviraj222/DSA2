def reversearray(n):
    if len(n) <=1 :
        return n
    return reversearray(n[1:])+[n[0]]

# write on paper then you understand what is happening
# python (n[1:])+ [n[0]] joint is happeing here


print(reversearray([23,24,25]))

# Time complexity O(n) draw tree of recursive call.