def my_decorator(func):
     def wrapper2():
         print("before")
         func()
         print("after")
     return wrapper2

@my_decorator
def hello():
    print("hello")


hello()


def logger(func):
    def wrapper3(*args,**kwargs):
        print(f"Logging : {func.__name__} called")
        return func(*args,**kwargs)
    return wrapper3



@logger
def add(a,b):
    return a+b

@logger
def subtract(a,b):
    return a-b

print(add(5,5))
print(subtract(10,4))