import random
from itertools import product
        
   
class cards():
    suit = ('hearts', 'spades', 'diamond', 'clubs')
    face = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight',
             'nine', 'ten', 'jack', 'queen', 'king', 'ace')
    values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7,
             'eight':8,'nine':9, 'ten':10, 'jack':11,
             'queen':12, 'king':13, 'ace':1}
    def __init__(self):
        self.card = deck.shuffle_deck
        self.card = deck.next_card()
        if self.card == 0:
            raise Exception('All card Dealt')
        self.suit = self.card[0]
        self.face = self.card[1]
        self.value = self.values[self.face]
    def __str__(self):
        return self.face,self.suit,self.values

class deck():
    def __init__(self):
        self.deck1 = list(product(cards.suit,cards.face))
    def next_card(self):
        random.shuffle(self.deck1)
        if len(self.deck1) == 0:
            return 0
        else:
            v= self.deck1.pop()
            s=(cards.values[v[1]]),
            return v+s
    def shuffle_deck(self):
        random.shuffle(self.deck1)


class Hand:
    def __init__(self):
        deck.__init__(self)
        pass
    def draw_from(self):
        l=[]
        a=deck.next_card(self)
        b=deck.next_card(self)
        l.append(a)
        l.append(b)
        x=a[2]+b[2]
        for i in range(10):
          if x>17:
            print("You win")
            break
          else:
            c=deck.next_card(self)
            l.append(c)
            x=x+c[2]
        return l    
    
class player:
   def __init__(self):
       deck.__init__(self)
       pass
   def show_hands(self):
       print(Hand.draw_from(self))      
       
p=player()
p.show_hands()       
