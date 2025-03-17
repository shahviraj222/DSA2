# pascal Triangle
#      1
#    1   1
#   1  2  1
# 1  3   3  1


# problem 1 : Find the rth row and cth column element
def element(r,c):
    # if rth row then r-1 and cth colum then c-1
    r = r-1
    c = c-1
    result = 1
    #r-1 C c-1 
    # 7C2 = 7 * 6 / 1 * 2
    for i in range(c):
        result *= r-i
        result /= i+1
    return result

print(element(4,3))    

# problem2 : Find The Entire Row 

# method1: 
def rowElement(n):
    ans = []
    for i in range(n):
        ans.append(int(element(n,i+1)))
    return ans

print(rowElement(4))
# O(n^2)

# method2:
def rowElement2(n):
    ans = [1]
    result = 1
    for i in range(1,n):
        result = result * (n-i)
        result = result / i
        ans.append(int(result))
    return ans
print(rowElement2(4))
# O(n)

# problem3 : Find Pascal Triangle
def pascalTriangle(n):
    ans = []
    for i in range(n):
        ans.append(rowElement(i+1))

    return ans

print(pascalTriangle(3))    





