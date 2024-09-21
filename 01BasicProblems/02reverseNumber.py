def reverse(n):
    isnegative = False
    if not n>=0:
        isnegative = True

    num = abs(n)
    revnum = 0
    while(num>0):
        temp = num %10
        revnum = (revnum*10)+temp 
        num = num // 10
    if isnegative:
        revnum = revnum * -1
    return revnum


print(reverse(1534236469))

# Complexity O(log N)  
# complexity O(n) if we consider n as number of digits
# log = base 10
# ln  = base 2