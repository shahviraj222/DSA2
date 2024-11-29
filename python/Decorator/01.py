# Decorator define that fucntion you call that  pass through a wrapper
import time

def timerfunc(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} take time to run : {end-start}")
        return result
    return wrapper

@timerfunc
def greet(name,greeting="Hello"):
    print(greeting," ",name)

# greet = timerfunc(greet)  meaning of the decorator 
# now greet contain wrapper because timerfunc returns
# greet = wrapeer() 

greet("Viraj")
# here the parameter is passed to wrapper
