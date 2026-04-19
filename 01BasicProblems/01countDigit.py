# num % 10 → last digit 
# num // 10 → remove last digit 

# num // (10^k) → first digit 
# num % (10^k) → remove first digit  !!!!problem!!! (do not preserve leading zeros in integers)
#  we have problem here suppose number is 1012 then when we remove first digit it will give 12 because when you do math 012 becomes 12 (as we see as math)


# k is total digits on right side form first element = (total elemnt - 1)

num = 123342

def countdigit(num):
    counter = 0
    while(num>0):
        num = num // 10
        counter+=1

    return counter

print("Number of digits :",countdigit(32583485))
 
# Complexity O(log N)
# log = base 10
# ln  = base 2 

