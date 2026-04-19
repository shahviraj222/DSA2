# n = 153 = 1^3 + 5^3 + 3^3  

# logic: last digit removal
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


# logic : first digit removal (here logic works :0^3 = 0 )

# 10^k 

def armstromChecker2(num):
    temp = num
    sum = 0

    div = 1
    while num // div >= 10:
        div *= 10

    num = temp

    while div:
        sum = sum + ((temp//div) ** 3)
        temp = temp % div
        div = div // 10

    
    if sum == num:
        return True
    
    return False


        

print(armstromChecker2(370))
print(armstromChecker(370))

# complexity is O(log n) if input number we take
# complexity is O(n) if n is number of digit
