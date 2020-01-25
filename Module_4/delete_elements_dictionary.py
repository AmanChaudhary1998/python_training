people={1:{'name':'john','age':'27','sex':'Male'},2:{'name':'Marie','age':'22','sex':'Female'}}
print(people[1]['name'])
print(people[2]['sex'])
print(people[1]['age'])
people[3]={}
people[3]['name']='Luna'
people[3]['age']='24'
people[3]['sex']='Female'
people[3]['married']='N0'
print(people[3])
people[4]={'name':'Peter','age':'29','sex':'Male','married':'yes'}
print(people[4])
del people[3]['married']
del people[4]['age']
print(people[3])
print(people[4])
del people[3]
print(people)
"""del people[3],people[4]
print(people)
"""
