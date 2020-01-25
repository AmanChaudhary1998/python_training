datastore={'office':{'medical':[{'room-number':100,'use':'reception','sq-ft':50,'price':75},
                                     {'room-number':101,'use':'waiting','sq-ft':250,'price':75},
                                     {'room-number':102,'use':'examination','sq-ft':125,'price':150},
                                     {'room-number':103,'use':'examination','sq-ft':125,'price':100},
                                     {'room-number':104,'use':'office','sq-ft':150,'price':100}],
                     'parking':[{'location':'preminium','style':'covered','price':750}]}}
print(datastore)
def change():
     change = int(input("select in which feild you want to perform changes 1. medical 2.parking"))
     if(change==1):
          ch=int(input('in which row you want to change'))
          for i in range(0,5):
               if(ch>=0 and ch<5):
                    up=int(input("what you want to change 1.room-number 2.use 3.price "))
                    if(up==1):
                         new=(input("enter new room number"))
                         datastore['office']['medical'][ch]['room-number']=new
                         print(datastore)
                         break
                    elif(up==2):
                         use_ability=input("enter new useability")
                         datastore['office']['medical'][ch]['use']=use_ability
                         print(datastore)
                         break
                    elif(up==3):
                         new =input("enter new price")
                         datastore['office']['medical'][ch]['price']=new
                         print(datastore)
                         break
                    else:
                         print("invalid input")
                         break
     else:
          ch=int(input('in which row you want to change'))
          for i in range(0,2):
               if(ch>=0):
                    up=int(input("what you want to change 1.location 2.style 3.price "))
                    if(up==1):
                         new=(input("enter new location"))
                         datastore['office']['parking'][ch]['location']=new
                         print(datastore)
                         break
                    elif(up==2):
                         new=(input("enter new style"))
                         datastore['office']['parking'][ch]['style']=new
                         print(datastore)
                         break
                    elif(up==3):
                         new=(input("enter new price"))
                         datastore['office']['parking'][ch]['price']=new
                         print(datastore)
                         break
                    else:
                         print("invalid input")
                         print("Attempt left:")
def add():
     add = int(input("select in which feild you want to perform addition 1. medical 2.parking"))
     if(add==1):
          ad=int(input("enter the number of rows you want to enter"))
          for i in range(0,5+ad):
               datastore['office']['medical'].append({'room-number':105,'use':'office','sq-ft':120,'price':80})
               print(datastore['office']['medical'])
               break
     else:
          ad=int(input("enter the number of rows you want to enter"))
          for i in range(0,2+ad):
               datastore['office']['parking'].append({'location':'ultra_preminium','style':'covered','price':'900'})
               print(datastore['office']['parking'])
               break
          
def main():
     op=int(input("select the operation want to perform 1,change 2.add 3. delete"))
     if(op==1):
          change()
     elif(op==2):
               add()
     else:
          delete()
                   
main()









     

