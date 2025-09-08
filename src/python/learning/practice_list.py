print("Hello world")

lst = [1,2,3,4,5]

for i in lst:
    print(i)

print(len(lst))
lst.reverse()
for i in lst:
    print(i)


lst.sort(reverse=True)
print(lst)

llst = [[1,2,3,4],[23,23,2,4],[2,2,31,2],[1,2,3,5]]

print("show doubly list")
for i in range(0,len(llst)):
    for j in range(0,len(llst[0])):
        print(llst[i][j])
    print("\n")

