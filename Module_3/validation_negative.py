product = int(input("enter the number of products\n"))
i=0
while(i<product):
     wholesale_price = int(input("enter the wholesale_price"))
     if(wholesale_price<=0):
          print("re-enter the price")
     else:
          retail_price = wholesale_price*0.5
          print(retail_price)
          i+=1
          
