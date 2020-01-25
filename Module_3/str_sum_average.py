s = input("enter the name of the subjects along with their marks\n").split(' ')

p= [int(s[i])for i in range(2,len(s),3)]
print("sum is ", sum(p), "percentage is ",round(sum(p)/len(p),2))
