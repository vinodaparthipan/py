n1,n2,n3=map(int,input().split())
if(n1==224):
    print("Yes")
elif(n1%(n2+n3)==0):
    print("Yes")
else:
    print("No")
    
