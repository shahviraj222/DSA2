# problem 1 
numbers = [1,2,45,44,67,-78,70,-65,91,-98,-62,23,37]
count = 0
for i in numbers:
    if(i>0):
        count+=1
print(count)

# problem 2
n=2
sum = 0
for i in range(1,n+1):
    if i%2 == 0:
        sum+=i
print("Even Number Sum",sum)

# problem 3
sum = 0
for i in range(1,n+1):
    if not i%2 == 0:
        sum+=i
print("Odd Number Sum",sum)

# problem 4
n=17
for i in range(1,11):
    if(i==5):
        continue
    print(n,"x",i,"=",i*n)

# problem 5   reverse strign
name = "virajshah"
count = len(name)
reverse = ""
for c in range(0,count):
    reverse += name[count-c-1]
print("Reversed String:",reverse)    

# problem 6 first non repeated character
string = "vhjkjggdfhmghhddsvwrjkyrte"
char_count = {}

for char in string:
    if char in char_count:
        char_count[char]+=1
    else:    
        char_count[char] = 1

for char in string:        
    if char_count[char] == 1:
        print("The First Repeated Character Is:",char)
        break
#Logic  
#Count total count in c store in s[char] and then 
# with the help of string find which one is first.

# problem 7 factorial
def factorial(num):
    if num > 1:
        return num * factorial(num-1)
    else:
        return 1

print("Factorial of",5,"is",factorial(5))

num=5
number = num
facto = 1
while number >1:
    facto *= number
    number -=1
print("Factorial of",num,"is",facto)

#problem 8 prime number
num = 28
is_prime = True
if num >1:
    for i in range(2,num):
        if (num % i) == 0:
            is_prime= False
            break
           
print("Prime :",is_prime)

#problem 9 Duplicate found then print 
# always try to use dictionary or set the operations are O(1)

items = ["apple", "banana", "orange", "apple","mongo"]

unique_bucket = set()  

for item in items:
    if item in unique_bucket:
        print("Duplicated Found:",item)
        break
    else:    
        unique_bucket.add(item)

        