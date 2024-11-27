def gcd(x1,x2):
    temp = min(x1,x2)
    gcd = []
    for i in range(temp,0,-1):
        if x1 % i == 0 and x2 % i == 0:
            gcd.append(i)
    return gcd    

d = gcd(24,12)
print(d)

#  complexity O(min(m1,m2))