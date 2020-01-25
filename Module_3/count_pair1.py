
"""arr = list(input("enter the elements into the array\n"))
sum1= int(input("enter the sum\n"))
n  =list(map(int,arr))
if (sum1-arr[i]) in arr:
     print(sum1-arr[i], arr)
"""
def printPairs(arr, arr_size, sum): 
    s = set() 
      
    for i in range(0, arr_size): 
        temp = sum-arr[i] 
        if (temp in s): 
            print ("Pair with given sum "+ str(sum) + " is (" + str(arr[i]) + ", " + str(temp) +s.add(arr[i]))
A = [1, 4, 45, 6, 10, 8] 
n = 16
printPairs(A, len(A), n) 
