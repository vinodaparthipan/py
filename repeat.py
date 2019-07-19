s=input()
u=[]
for char in s[::]:
    if char not in u:
        u.append(char)
        print(len(u))
