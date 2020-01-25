n = int(input("enter your marks below 100\n"))
if(n>=90 and n<100):
     print("Your grade is A")
elif(n<90 and n>=80):
     print("your grade is B")
elif(n<80 and n>=70):
     print("your grade is C")
elif(n<70 and n>=60):
     print("your grade is D")
elif(n<60):
     print("you are fail")
else:
     print("Invalid input")
