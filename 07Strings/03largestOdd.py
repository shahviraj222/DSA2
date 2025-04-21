# problem: String is given find the largest odd number from it

# 1 how to fidn the substring
a = "234345"
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        a[i:j]
        # print(a[i:j])

# method1
def largest_odd_number(num: str) -> str:
    maxi = float("-inf")

    # Iterate over all possible substrings
    for i in range(len(num)):
        for j in range(i + 1, len(num) + 1):
            number = int(num[i:j])
            if number % 2 == 1:
                if number > maxi:
                    maxi = number

    if maxi != float("-inf"):
        return str(maxi)

    return ""

# method2: 
# odd number =  is the number that end with odd digit 
# so we travel from the end of string and find the odd digit. 
def largest_odd_number2(num:str) -> str:
    for i in range(len(num)-1,-1,-1):
        if int(num[i])%2 == 1:
            return num[:i+1]
    return ""

print(largest_odd_number("12345"))
print(largest_odd_number2("12345")) 

