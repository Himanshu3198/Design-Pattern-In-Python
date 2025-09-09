from collections import defaultdict,deque
from unittest import defaultTestLoader


class Props:

     def __init__ (self,id ,name):
        self.id =id
        self.name = name
     def display (self):
         print(f" id is {self.id} and name is {self.name}")



print("hello world..")

# ********** list example**********

if __name__ == "__main__":
    obj = Props(25,"Himanshu")
    # obj.display();

#  ********** list demo and use************
lst = []

print("=========List features=========")
lst.append(12)
lst.append(5)
lst.append(25)
# lst.pop()
print("size",len(lst))

# for i in range(0, len(lst),1):
#     print(lst[i])

lst.reverse()
lst.sort(key=lambda x:-x)
for i in range(0, len(lst),1):
    print(lst[i])

mp=defaultdict(int)

mp[1]+=1
mp[1]+=1
mp[1]+=1
mp[2]+=1
mp[2]+=1
mp[3]+=1

one_key=1
if one_key in mp:
    print("yes its there",mp[one_key])


#  delete key
del mp[1]
for i in mp:
    print(i,mp[i])



#     ========== Hashset===========

myset =set()

myset.add(1)
myset.add(6)
myset.add(15)
myset.add(5)

print("size",len(myset))
if 5 in myset:
    print("yes removing it")
    myset.remove(5)
print("==== printing the set========")
for i in myset:
    print(i)

# ==========String======
s="hello"
print(s[1])
s[::-1] #reverse
s.upper()
# print(s[0:3])


#=====================Stack demo=====================

stack = []

stack.append(5)
stack.append(10)
stack.append(15)

print(f"stack pop(): {stack.pop()}")
print(f"stack top(): {stack[-1]}")
size = len(stack)


#=============== Queue demo==============

queue = []

queue.append(5)
queue.append(10)
queue.append(15)

print(f"queue pop(): {queue.pop(0)}")
print(f"queue peek(): {queue[0]}")
qsz = len(queue)

# ===== DEQUE DEMO ======
dq = deque([])
dq.append(1)
dq.appendleft(2)
dq.append(3)
dq.append(4)
dq.append(5)


print(dq)
dq.pop()
dq.popleft()
print(dq)