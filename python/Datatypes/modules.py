import math           
import re              #regular expression  
import os              
import decimal         
import random         

a = ["Viraj Shah" ,"Vimal Shah","Nemi Shah"]
print("Shah" in a)

for name in a:
    print(bool(re.search(r".*Shah$", name)))    #finding in list name ends with Shah   

# .*  stands for all characters
# $   stands for ending character


