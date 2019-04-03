tlist=[1,3,5,7,9,8,0]
print(tlist)
print(tlist[2])
tlist.append(7)
print(tlist)
tlist.insert(2,8)
print(tlist)
tlist.remove(8)
print(tlist)
x=[0,2,4,6]
print(tlist+x)
tlist.remove(tlist[3])
print(tlist)
t=tlist.index(5)
print(t)
for i in x:
    print(i)
tlist[2]=49
print(tlist)
if 8 in tlist:
    print("present")
else:
    print("not present")
tlist.insert(1,"mango")
print(tlist)
x.pop()
print(x)
print(len(x))
