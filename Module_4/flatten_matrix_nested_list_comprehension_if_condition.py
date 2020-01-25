# Suppose I want to flatten a given 2-D list and include only those elsements whose
#length is less than 6:
planets= [['Mercury','Venus','Earth'],['Mars','Jupiter','Saturn'],['Uranus','Neptune','pluto']]
flatten_planets=[]
for sublist in planets:
     for val in sublist:
          if(len(val)<6):
               flatten_planets.append(val)
print(flatten_planets)
#  Nested List Comprehension to flatten_planets using if condition
flatten_planets=[planets for sublist in planets for planet in sublist if len(planet)<6]
print(flatten_planets)
