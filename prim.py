n =int(input())
if n > 1:
   for i in range(2,n):
       if (n % i) == 0:
           print(n,"is not a prime number")
           print(i,"times",n//i,"is",n)
           break
   else:
       print("yes")
else:
   print("no")
