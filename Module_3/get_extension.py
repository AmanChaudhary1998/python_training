"""
s = input("enter the path\n")
print(s.split('.')[1])
"""
s = input("enter the path\n")
print(s.split('/')[-1].split('.')[0],end = '.pdf')
