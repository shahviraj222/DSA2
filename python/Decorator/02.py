def debug(func):
    def wrapper(*args,**kwargs):
        arg = ', '.join(str(i) for i in args)
        kwarg = ', '.join(str(k+":"+v) for k,v in kwargs.items())
        
        print(f"Fucntion '{func.__name__}' contain argumetns : {arg} kwargs contain : {kwarg}")
        result = func(*args,**kwargs)
        return result
    return wrapper

@debug
def greet(name,greeting):
    print("Hello I am Greet Function")
# greet = debug(greet) meaning of the decorator


greet("Viraj",greeting="Hello")
# the wrapper function is called and passed variables

