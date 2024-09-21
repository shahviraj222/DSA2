# n = 153 = 1^3 + 5^3 + 3^3  

def armstrong(n):
    num = n
    temp = 0
    sum = 0

    if(n<= 10 and n>-1):
        return True
    
    if n <= -1:
        return False 
    
    while(n>0):
        temp = n%10
        sum = sum + temp ** 3
        n = n//10

    if sum == num:
        return True
    
    return False  

print(armstrong(153))

# complexity is O(log n) if input number we take
# complexity is O(n) if n is number of digit
