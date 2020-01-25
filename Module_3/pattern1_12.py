
print("program to print the pramid_1\n")
rows = int(input("Enter number of rows\n"))
for i in range(rows,0,-1):
     for j in range(0,i):
          print("*",end = ' ')
     print()
for i in range(0,rows):
     for j in range(0,i+1):
          print("*",end = ' ')
     print()
     

print("program to print the pyramid_2\n")
rows = 13
for i in range(0,rows):
     for j in range(0,rows):
          if(i!=6 and j==6):
               print("*",end=' ')
          elif(i==6):
               print("*",end=' ')
          else:
               print(" ",end=' ')
     print()


print("program to print the pyramid_3\n")
for i in range(1,5):
     for j in range(1,5-i):
          print("   ",end='')
     for k in range((2*i-1),0,-1):
          print("* ",end='')
     print()
for i in range(3,0,-1):
     for j in range((4-i),0,-1):
          print(end='   ')
     for k in range((2*i-1),0,-1):
          print("* ",end='')
     print()
print("program to print pyramid_4\n")
n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(' ',end='')
    for k in range(1,2*i):
        print('*',end='')
    print()
print("program to print pyramid_5\n")
n=12
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(' ',end='')
    print('*',end='')
    if 1 < i <= n - 1:
        for k in range(1,2*i - 2):
            print(' ',end='')
        print('*',end='')
    elif i == n:
            print('*'*18)
    print()


















