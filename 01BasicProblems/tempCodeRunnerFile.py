# broute force aproach is there to find the divsior and other mehtode is also there
# take sqrt and go uptil 
# 36
# 1 * 36
# 2 * 18
# 3 * 12
# 4 * 9
# 6 * 6
import math
def divisor(n):
    d=set()
    sqrt = int(math.sqrt(n))
    for i in range(1,sqrt + 1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    return d    

def prime(n):
    if n <= 1:
        return False
    d=set()
    sqrt = int(math.sqrt(n))
    for i in range(2,sqrt + 1):
        if n % i == 0:
            return False
    return True    


print(divisor(36))
print(prime(123))
# complexity O(sqrt(n))    n = input number