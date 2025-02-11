# take sqrt and go uptil that
# 36
# 1 * 36
# 2 * 18
# 3 * 12
# 4 * 9
# 6 * 6

import math

def divisor(num):
    d=set()
    sqrt = round(math.sqrt(num))
    for i in range(1,sqrt+1):
        if num % i == 0:
            d.add(num//i)
            d.add(i)
    return d

def primeChecker(num):
    sqrt = round(math.sqrt(num))
    for i in range(2,sqrt+1):
        if num % i == 0:
            return False
    return True
    
print(primeChecker(121))  
print(divisor(36))

# complexity O(sqrt(n))    n = input number
