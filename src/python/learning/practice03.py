import copy
from collections import deque, defaultdict
import heapq
fruits = ["apple","grapes","mango"]

for index,fruit in enumerate(fruits):
    print(f"index={index},fruit={fruit}")



a=[[1,2],[3,4]]
b = copy.copy(a)
b[0][0] = 99
c = copy.deepcopy(a)

print(b)
print(a)
print(c)

# // reverse the arr
arr1 = [1,2,3,4]

arr1.reverse()
print(f"arr={arr1}")
arr2 = ["delhi","mumbai","blr"]

for code,city  in zip(arr1,arr2):
    print(f"code={code},city={city}")


two_d = [[1,2],[3,4],[2,6],[-1,5]]
# comparator sort
two_d.sort(key=lambda  x:-x[1])

for i,j in  two_d:
    print(f"a={i},b={j}")




# stack

stk = []
stk.append(1)
stk.append(2)
stk.append(3)

print("printing the stack")
while len(stk) >0:
    print(stk[-1])
    stk.pop()

q = deque()
q.append(2)
q.append(3)
q.appendleft(1)
q.append(4)
print("Deque operations")
while len(q) > 0:
    print(q.popleft())
    if len(q) > 0:
        print(q.pop())


max_heap = []

heapq.heappush(max_heap,(-10,5))
heapq.heappush(max_heap,(-5,12))
heapq.heappush(max_heap,(-1,0))

print("printing the heap")
while len(max_heap) > 0:
     print(f"top={max_heap[0]}")
     heapq.heappop(max_heap)

print("reverse is")
s="himanshu"
ss = list(s)
ss.reverse()
t = "".join(ss)
print(t)
print("substring is")
print(s[0:4])

map = defaultdict(list)

l1 = [1,23,5]
l2 = [2,23,51]
map[1] = l1
map[2] = l2
print("map")
for x in map[1]:
    print(x)

map1 = defaultdict(set)
map1[1].add(2)
map1[1].add(3)
map1[2].add(6)
map1[2].add(7)

print("map of set")
for k, values in map1.items():
    print(f"k={k}")
    for v in values:
        print(f"v={v}")

