s1,s2=input().split()
cost_diff=abs(len(s1)-len(s2))
for i in range(len(s1)):
    if len(s2)==1 and s2[i] in s1:
        break
    else:
        if s1[i] != s2[i]:
            cost_diff+=1
            print(cost_diff)
