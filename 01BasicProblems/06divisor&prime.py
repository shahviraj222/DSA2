"""
Definition:
The LCM is the smallest number that both numbers can divide into.

Example:

Take 12 and 18

Multiples of 12 → 12, 24, 36, 48…
Multiples of 18 → 18, 36, 54…

👉 First common multiple → 36
👉 LCM = 36


The GCD is the largest number that divides two (or more) numbers exactly.

Example:

Take 12 and 18

Factors of 12 → 1, 2, 3, 4, 6, 12
Factors of 18 → 1, 2, 3, 6, 9, 18

👉 Common factors → 1, 2, 3, 6
👉 GCD = 6


GCD(a,b)×LCM(a,b)=a×b

For 12 and 18:

GCD = 6
LCM = 36

👉 6 × 36 = 216
👉 12 × 18 = 216 ✔️

"""

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
