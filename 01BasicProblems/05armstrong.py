# n = 153 = 1^3 + 5^3 + 3^3  

def armstromChecker(num):
    sum = 0
    temp = num
    if num in range(0,10):
        return True
    if num < 0:
        return False
    while temp > 0:
        sum = sum + ((temp%10) ** 3)
        temp = temp // 10

    if sum == num:
        return True
    return False    


print(armstromChecker(153))

# complexity is O(log n) if input number we take
# complexity is O(n) if n is number of digit
