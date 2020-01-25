class Info:
     def __init__(self,name,phone,email_address):
          self.name=name
          self.phone=phone
          self.email_address=email_address
     def get_name(self):
          return self._name
     def set_name(self):
          self._name=input("enter the name\n")
     def get_phone(self):
          return self._phone
     def set_phone(self):
          self._phone=int(input("enter the phone\n"))
     def get_email_address(self):
          return self._email_address
     def set_email_address(self):
          self._email_address=input("enter the email\n")
def main():
     det= Info('ghg',454,'dqsdh')
     p={}
     det.set_name()
     det.set_phone()
     det.set_email_address()
     print(det.get_name(),det.get_phone(),det.get_email_address())
     p['Name']=(det.get_name())
     p['phone']=(det.get_phone())
     p['email']=(det.get_email_address())
     print(p)
main()




     
          
