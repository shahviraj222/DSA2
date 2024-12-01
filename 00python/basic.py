a=input("Enter The Age Of User:")
try:
    a=int(a)
except:
    print("Age Can Not Be",a)
    
if(a<=12 and a>0):
    print("Child")    
elif(a>=12 and a<=18):    
    print("Teen")
elif(a>18 and a<=50):    
    print("Adult")
elif(a>50 and a<=200):
    print("Senior")    
else:
    print("Age Can Not Be",a)    

#Second Problem 
def checkAge(a):
    try:
        a= int(a)
        return a
    except:    
        print("Age Is Not Valid:")
        return 0

def decidePrice(a):        
    if(a>18):
        return 12

    else:
        return 8

def decideDiscount(discount,price):
    if discount:
        price = price - 2
        return price
    else:    
        return price

discount = False
daylist = ["wednesday","w","wendnes","wedn","wed"]
price = 0

a = input("Enter Your Age:")
day = input("Enter Day:") 

day = day.strip()
day = day.lower()

if day in daylist:
    discount = True

a= checkAge(a)
price=decidePrice(a)

finalprice = decideDiscount(discount,price)

print("Amout to be paid : ", finalprice)

