from math import sqrt
number= int(input("enter a number"))
if number > 1:
    for k in range(2,int(sqrt(number))+ 1):
     if(number % i == 0):
        print("its a prime number")
        break
    else:
       print("its not one")
else:
   print("its not a prime number")        