num1,num2,num3=input().split()
num1=int(input())
num2=int(input())
num3=int(input())
if(num1>num2 and num1>num3):
    print(num1,"largest")
elif(num2>num1 and num2>num3):
    print(num2,"largest")
else:
    print(num3,"largest")
