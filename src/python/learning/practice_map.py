from collections import defaultdict
mp =  defaultdict(int)

mp[1]+=1
mp[1]+=1
mp[2]+=1
mp[3]+=1
mp[2]+=1
mp["x"] =1
mp["x"]=[1,2,3,5,6]
print(mp["x"])
mp.pop("x")
print(mp)

if 1 in mp:
    print("yes")
else:
    print("no")

print(len(mp))

person = defaultdict(int)

person["a"] = 1
person["c"] = 1
person["a"] = 2
print(person)

