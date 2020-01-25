n = int(input("enter the number of trees"))
m =int(input("enter the number of seconds"))
value = []
for i in range(0,n):
     fruit = int(input("enter the fruit points"))
     value.append(fruit)
print(max(value))
x = value.index(max(value))
sum1 = value[x+1]+value[x+2]
sum2 = value[x-1]+value[x-2]
sum3 = value[x+1]+value[x-1]
if(sum1>sum2):
     if(sum1>sum3):
          print("total fruit value sum1 is ",(sum1+max(value)))
     else:
          print("total fruit value ",(sum2+max(value)))
else:
     print("total fruit value ",(sum3+max(value)))
     
