
# m^n
# time complexity is O(n)
def expodential(m,n):
    if n==0:
        return 1
    return m*expodential(m,n-1)


# time complexity O(n) but multiplicatio math operation is reduce
def expodential2(m,n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return expodential(m*m,n/2)
    else:
        return m*expodential(m*m,(n-1)/2) 

print(expodential(2,2))
print(expodential2(2,2))