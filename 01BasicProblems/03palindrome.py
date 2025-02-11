# 12321

def palindromeChecker(num):
    number = num
    revrse = 0
    isnegative = False
    if num < 0:
        isnegative =True
        num = abs(num)
        
    while num:
        revrse = revrse*10 + num%10
        num = num//10

    if isnegative:
        revrse *= -1

    if number == revrse:
        return True
    
    return False    

print(palindromeChecker(-22))