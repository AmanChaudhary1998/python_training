from collections import OrderedDict
s = input("enter the string\n").split(' ')
result = " ".join(OrderedDict.fromkeys(s))
print(result)
