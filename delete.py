from itertools import combinations
n,k=map(int,input().split())
d=len(str(n))
l=list(combinations(str(n),d-k))
l=sorted(l)
print("".join(l[0]))
