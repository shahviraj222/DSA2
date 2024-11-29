import math            #to handle math expression
import re              #regular expression  
import os              #to handle operating system filing
import decimal         #to handle the decimal calculation
import random          #to handle the random number generation

# F string and adding decimal pointer limit
price = 44
print(f'The Price Of Toy Is {price:.2f} dollars')

a = "Viraj Shah" 
print(a[0])
print(a[:])
print(a[::2])
print(a[::-1])

# Replacing 
t = ""
for i in a:
    if i == " ":
        t = t + " Jani"
        break
    t += i   

print(t)

# Replacing in List
a = ["Viraj Shah" ,"Vimal Shah","Nemi Shah"]        
t = ""
for i in a:
    for j in i:
        if j == " ":
            t = t + " Jani"
            break
        t += j 
    print(t)
    t=""



# methods of strings 

a = "customer is statisfied with our service but they have concern about privacy."
print(a.upper())
print(a.lower())
print(a.strip())                  # remove white space from begning and ending only
print(a.replace("c","E"))         # replace all char

print(f"Hello This is F String {a}")