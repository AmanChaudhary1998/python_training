"""
l = list(input("enter the elements into the given list\n").split(','))
k=sorted(l)
print(sorted(k,key=k.count,reverse=True))
"""
l = list(map(int,input("enter the number of elements\n").split(',')))
count=0
for i in range(0,l):
     for j in range(i+1,l):
          if(l[i]>l[j]):
               temp =l[i]
               l[i]= l[j]
               l[j]=temp
