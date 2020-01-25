class Automobile:
     def __init__(self,make,model,mileage,price):
          pass
     def set_make(self):
          self._make=input("enter the name of country\n")
     def set_model(self):
          self._model=input("enter the name of the model\n")
     def set_mileage(self):
          self._mileage=int(input("enter the mileage\n"))
     def set_price(self):
          self._price=int(input("enter the price\n"))
     def get_make(self):
          return self._make
     def get_model(self):
          return self._model
     def get_mileage(self):
          return self._mileage
     def get_price(self):
          return self._price
