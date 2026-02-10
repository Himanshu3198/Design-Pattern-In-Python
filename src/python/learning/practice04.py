# iterator - you can loop over one element at time  and it has next keyword to iterate over next element and it sore the state-Stores current state Netflix episode pointer — remembers where you stopped.

nums = [1,2,3]
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))


# generator - A simpler way to create iterators using yield it also has next() fuction to go on next element but it do on demads
print("generator")
def gen_nums():
     yield 1
     yield 2
     yield 3
g = gen_nums()

print(next(g))
print(next(g))


# decorator - a function that change the behaivour of another function

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper()



@my_decorator
def hello():
    print("Hello")

hello()


# args- pass position argument as tuple, **kwargs - pass keyword argument as dictionary