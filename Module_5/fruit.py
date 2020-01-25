c=[]
f={'fruit':{'name':['apple','mango','banana'],'biological name':['malus domestica','mangi fera indica','musa'],'major producer':[['China','Us','Turkey'],['India','China','Thailand'],['India','Thailand','Africa']],'nutrition':{'carbohydrates':[13.81,16.28,15.68],'fat':[0.17,0.20,0.18],'protein':[0.26,0.29,0.28]}}}
print(f)


for i in range(0,3):
    if f['fruit']['nutrition']['protein'][i]==max(f['fruit']['nutrition']['protein']):
        x=f['fruit']['name'][i]

print(x)
