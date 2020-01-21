a = int(input("enter the five digit number\n"))
summation = 0 ;
"""
while(a!=0):
     i = a%10;
     summation = summation+i;
     a= a//10;
print(summation)
"""
summation = 0
while(a!=0):
     i=a%10;
     summation = summation*10+i;
     a = a//10;
print(summation)
     
