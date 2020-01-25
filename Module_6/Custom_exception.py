#class My error is derived from super class Exception
class MyError(Exception):
     #Constructor or Initializer
     # _init_ = private
     # __init__=protected
     def __init__ (self,val):
          self.value=val
          #_str_ is to print() the value
     def __str__(self):
          return(self.value)
try:
     e=MyError(3*6)
     raise(e)
#Value of Exception is stored in error
except MyError as err:
     print('A new exception occured:'+str(err.value))
