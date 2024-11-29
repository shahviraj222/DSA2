# Problem : give a even number upto certain limit

# S1:Here Problem Return Tuples
def generator(number):
    return range(2,number+1,2)
result=generator(4)    
print(result)    

# S2:Here Problem Return List
def generator(number):
    even_number = []
    for i in range(2,number+1,2):
        even_number.append(i)
    return even_number
result=generator(4)    
print(result)    

# S3: Perfect
# Finally yeild = it return the value and also store the function and it's current state
def generator(number):
    for i in range(2,number+1,2):
        yield i   
for n in generator(10):
    print(n)



# Lambda Funcitons
# lambda (varibles to take) : Working of function
cube = lambda x : x**3
print("Lambda Function : ",cube(4)) 

# *Args
def sum_all(*args):
    # *args return number
    # args return tuples
    return sum(args)
print(sum_all(1,2,324))


# Named Parameters Order Of Arguments Not matter
def greet(first,last):
    print(f"Hello Mr.{first} {last}")
greet(last="Shah",first="Viraj",)          # order not matter

# kwargs: (key,value) pair undefined 
def greet2(**kwargs):
    print("kwargs value : ",kwargs)
    # for key,value in kwargs.items():
        #pass
greet2(last="Shah",first="Viraj")


# Factory Function OR Closure Bag Theory 
def chaiaurcoder(num):
    def actual(x):
        return num ** x
    return actual

f = chaiaurcoder(3)
print("num = 3 and x = 2  : " ,f(2))

# Bag Theory Concept When in python any Funciton return fucntion it also return memory refrence.