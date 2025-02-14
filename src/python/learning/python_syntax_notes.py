from collections import defaultdict
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
print(s[0:3])

