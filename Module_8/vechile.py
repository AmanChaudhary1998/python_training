from automobile import Automobile as auto
class Car(auto):
     def __init__(self,make,model,mileage,price,doors):
          auto.__init__(self,make,model,mileage,price)
     def set_doors(self):
          self._doors=int(input("enter the number of doors\n"))
     def get_doors(self):
          return self._doors
class Truck(auto):
     def __init__(self,make,model,mileage,price,drive_type):
          auto.__init__(self,make,model,mileage,price)
     def set_drive_type(self):
          self._drive_type=input("enter the drive_type\n")
     def get_drive_type(self):
          return self._drive_type
class SUV(auto):
     def __init__(self,make,model,mileage,price,pass_capacity):
          auto.__init__(self,make,model,mileage,price)
     def set_pass_capacity(self):
          self._pass_capacity=int(input("enter the number of passenger capacity\n"))
     def get_pass_capacity(self):
          return self._pass_capacity
def main():
     c=Car('make','model','mileage','price','doors')
     t=Truck('make','model','mileage','price','doors')
     s=SUV('make','model','mileage','price','doors')
     c.set_make(),c.set_model(),c.set_mileage(),c.set_price(),c.set_doors()
     t.set_make(),t.set_model(),t.set_mileage(),t.set_price(),t.set_drive_type()
     s.set_make(),s.set_model(),s.set_mileage(),s.set_price(),s.set_pass_capacity()
     print(c.get_doors(),t.get_drive_type(),get_pass_capacity())
main()










          
