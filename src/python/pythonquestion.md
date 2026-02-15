Python Question.

Syntax & Data Types (25 Questions)

Difference between list, tuple, set, dictionary?

When should you use tuple over list?
ans-because tuple are immutable and faster

What are mutable and immutable types?
list,dictionary,set mutable
immutable-string,tuple

Why are strings immutable?
security,thread safety

What is shallow copy vs deep copy?
shallow copy - create copy with same reference so if any element change it will reflec
in other too. while in deep copy - create a separate object.
How does copy() differ from slicing?
copy:creating entire copy.
slicing:shrinking the existing list
What happens when you do a = b?
reference a to b

How is memory handled for integers?
it stored as object and if multiple object can share same value that reference
python use for better memory management

What is interning in Python?
python reusing the already created object instead of creating new object with same value

What is the difference between == and is?
'==' compare values while is compare reference

Why does [] * 3 sometimes behave unexpectedly?
because we haven't mentioned data it hold

What is hashability?

Why can tuples be dict keys but lists cannot?
because tuple is immutable
What is the difference between set and frozenset?
set mutable
frozenset immutable

What are truthy and falsy values?
falsy-0, None, False, "", [], {}
Explain dynamic typing.
python decide at runtime

What is duck typing?
Python checks behavior, not type.

What are type hints?
mentioned the variable or return type help of developer for better readibility 
How to check variable type?
print(type(x))

What is None?
represent null

What is the difference between id() and type()?
id represent-memory address
type represent data type

What are Python built-in data types?

Explain Python’s memory model.
managed by reference counting,garbage collection,cyclic garbage collector
it stored object local varialbe in heap, while method call store in stack

How does garbage collection work?

What is reference counting?

2️⃣ Control Flow (10 Questions)

How does for-else work?
else only run when for complete normally

What is pass vs continue vs break?
pass - placeholder for future implmentation or does not
continue return loop condition
break - the current loop

What is short-circuit evaluation?
if a and b: if a fail never check for b

How does try-except-else-finally work?

What are custom exceptions?
user defined exception

What is assertion?
helpful for debug , check of not favourable condition assert x is null

What is context manager? 
it allow to allocate and release resouce gracefully e.g opening file with with open

Difference between raise and assert?
raise - for throwing exception
assert - for debugging or test

How to create custom exception class?

What happens if finally block returns?
if finally has return then it overright try even exception and finally will execute for sure!.

What are positional vs keyword arguments?
position - a series a values pass as tuple where order matter
keyword- a key value pair pass a dictory where position doesn't matter.

What are default arguments pitfalls?
default argument are evaluted once . at the time of initialization
after they any no of time you call the method it won't get changed e.g
def add(item,list=[]):
    list.add(item)
    return list
print(add(1))
print(add(2))
print(add(3))
outpute
1
1,2
1,2,3
but expected was 
1
2
3
Why are mutable default arguments dangerous?
list,dict,set can change
all function call modify the object if they have defined logic.

What are *args and **kwargs?
args - positional argument
kwargs- keyword argument


What is lambda function?
it is small anonymous function written in one line
add = lambda a,b:a+b
when use? 
you need small function.

What are first-class functions?
first class function python will treat function as regular object so you can
pass it as another function,assign to a variable,and store in data structure like list
def greet():
    return "hello"
def call_back(func):
    return func()

print(call_back(greet))
What is closure?
A function that remember variable from its outer function even after
outer function has finished, usage=Data hiding

What is LEGB rule?
its a rule how python look for variable in scope local->enclosing->global->built-nonlocal is a keyword that tell python that variable defined
in

What is nonlocal?
nonlocal is a keyword that tell python that variable defined
variable define in outer function is nonlocal .so that you can use
it  modifying in inner class(if you don't explicity mention then it will consider
it local and undefined)

def func():
   x = 10
   inner():
    x=x+1 (throw error)
    // nonlocal x

What is recursion?
a function calling itself until a base condition hit.

What is tail recursion?
base case return by recursion call.

What is decorator?
A function that takes another function, modifies it, and returns a new function.

what is generator?
a function that return iterator using yield keyword. its a pausable and resumable function.

How decorator works internally?

How to write decorator with arguments?

What is functools.wraps?
after decorating function name  becomes wrapper

What is partial function?
partial function fix argument of function. so that later at time of function 
call only half information need to pass. eg.

def add(a,b):
    return a+b
add5 =partial(add,5)
print(add5(10))
o/p: 15

What is higher-order function?
a function that takes function and return function.

What is generator function?
a function that uses yield.
return value one by one
does not store everyting inmemory

What is yield?
pause function
save state
resume later

Generator vs iterator?
generator - easy way to create iterator
iterator - function that has iter(). it will give you next value on demand 
when calling next()

OOP (30 Questions)

What is OOP?

What are pillars of OOP?

How Python supports encapsulation?

What is name mangling?

What is inheritance?

What is multiple inheritance?

What is MRO?

What is method resolution order algorithm?

What is diamond problem?

What is super()?

What is composition vs inheritance?

What is abstract class?

What is ABC module?

What is method overloading in Python?

What is method overriding?

What is dunder method?

What is init vs new?

What is str vs repr?

What is slots?

What are class variables vs instance variables?

What is staticmethod?

What is classmethod?

What is metaclass?

How object creation works internally?

What is dataclass?

attrs vs dataclass?

What is immutability in class?

What is descriptor?

What is property decorator?

How to make object callable?


Iteration & Internals (20 Questions)

What is iterable?
a collection that can be iterate using loop or converting then in 
iterator using iter() eg list= [1,2,3], it =iter(list) 

What is iterator?
creating a iterable to iterate it over e.g list.

How to create custom iterator?

What is StopIteration?

What is iter and next?
iter - creating a iterator.
next - accessing the next item.

What are comprehensions?
looping and computing in single line e.g list compreshiion.
e.g creating a list from list comprehension:
square = [ i for i*i in range(1,5)]

List vs generator comprehension?

What is zip?
combines multiple togetter e.g
fruit =["mango",banana,"grapes"]
ids = [1,2,3]
for i,f in zip(fruit,ids):
     print(f"{i},={f})

What is enumerate?
add index as well in iterable e.g
for idx,fr in enumerate(fruit):
    print(idx,fr)

What is itertools?
a module that provide fast iterator tools.
e.g-combination,permutation,count,cycle,chain

What is map/filter/reduce?
map applied on every element to transform  sq = map(lambda x:x*x,list)
filter- filter the elements based on condition even = filter(lambda x:x%2==0,list)
reduce - reduce list to single value useful e.g sum,product,average=  sum =reduce(lambda a,b:a+b,list)

What is lazy evaluation?
load the record on demand not immediately.

What is memory efficiency in generator?
do not store all element at a time
load one value at a time
save time and memory.

What is range object?
range,xrange to generate  create a range object

How Python loop works internally?

What is unpacking?

Extended unpacking?

What is walrus operator?

What is pattern matching (match-case)?

When to use itertools?


Memory & Internals (20 Questions)

What is GIL?

Why Python has GIL?

How to bypass GIL?

Thread vs Process?

What is multiprocessing?

What is threading?

What is asyncio?

What is event loop?

What is coroutine?

What is async/await?

What is concurrent.futures?

What is context switching?

What is race condition?

What is deadlock?

What is global interpreter lock impact?

What is memory leak in Python?

How to detect memory leaks?

What is weakref?

What is del?

How GC works internally?

7️⃣ Concurrency & Parallelism (15 Questions)

ThreadPoolExecutor vs ProcessPoolExecutor?

CPU bound vs IO bound?

When to use async?

What is synchronization?

What is Lock/RLock?

What is Semaphore?

What is Condition variable?

What is asyncio.gather?

What is Future?

What is Task?

How to cancel coroutine?

What is non-blocking IO?

What is selector?

What is cooperative multitasking?

What is parallelism vs concurrency?

Python Internals (15 Questions)

How Python compiles code?

What is bytecode?

What is .pyc file?

What is PEP?

What is CPython?

What is PyPy?

What is C extension?

What is Cython?

What is import system?

What is sys.modules?

What is name?

What is main?

What happens during import?

What is virtual environment?

How pip works?

Design & Architecture (20 Questions)

How to structure large Python project?

What is packaging?

What is wheel?

What is entry point?

What is dependency resolution?

What is semantic versioning?

What is logging best practice?

What is config management?

How to manage environment variables?

How to handle secrets?

What is clean architecture?

How to design plugin system?

What is factory pattern in Python?

What is singleton?

What is observer?

What is strategy pattern?

What is dependency injection?

What is SOLID principles in Python?

How to write scalable Python service?

How to improve performance?

Testing (15 Questions)

What is unit testing?

What is pytest?

What is mock?

What is patch?

What is fixture?

What is parametrized testing?

What is coverage?

What is integration testing?

What is TDD?

What is BDD?

What is unittest?

What is hypothesis?

What is monkeypatch?

How to test async code?

How to test DB code?

How to profile Python code?

What is time complexity?

How to optimize loops?

How to reduce memory?

What is caching?

What is lru_cache?

What is memoization?

How to optimize SQL in Python?

How to speed up JSON?

When to use C extension?

Explain GIL deeply.

Design thread-safe LRU cache.

Implement your own dict.

Write custom context manager.

Write custom decorator with retry logic.

Build rate limiter.

Implement producer-consumer.

Write async web scraper.

Implement singleton in multiple ways.

Design plugin architecture.

How to handle 10k concurrent requests?

Explain memory fragmentation.

Write metaclass example.

Write descriptor example.

Explain deep copy internals.

Write custom iterable.

Implement your own enumerate.

What happens when you call function?

Explain call stack.

Explain reference cycles.

Explain CPython memory allocator.

How to debug production memory issue?

Explain import caching.

Write thread-safe counter.

Implement bounded queue.

Explain asyncio internals.

Write event loop from scratch (conceptually).

How to reduce startup time?

Explain monkey patching.

Explain dynamic code execution.

What is eval vs exec?

How to sandbox Python?

How to handle large CSV?

How to stream data?

Explain signal handling.

What is GIL removal attempts?

What is sub-interpreter?

How to embed Python in C?

How to create Python package?

What happens during class creation?