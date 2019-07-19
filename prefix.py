m=int(input())
v=[]
for j in range(m):
    d=input()
    v.append(d)
e=[]
for j in zip(*v):
    if(j.count(j[0])==len(j)):
        e.append(j[0])
    else:
        break
print("".join(e))
