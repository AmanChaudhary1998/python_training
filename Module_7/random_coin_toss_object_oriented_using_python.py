     # Object Oriented Programming using python.............
import random
class Coin:
     def __init__(self):
          self.sideup='Heads'
     def toss(self):
          if random.randint(0,1)==0:
               self.sideup='Heads'
          else:
               self.sideup='Tails'
     def get_sideup(self):
          return self.sideup
#if we want to call inside the calss use=> self.toss()
#for outside we have to created the object
# An object is created in memory from Coin class
# The Coin Class's __init__ method is called automatically
def main():
     my_coin=Coin() # Object is created of class coin
     print("the side is up:",my_coin.get_sideup())
     my_coin.toss()
     print('This side is up:',my_coin.get_sideup())
main()








