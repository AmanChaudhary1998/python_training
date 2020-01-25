# Exception Handling: code that respondes when exception are raised and prevents
#program from crashing
def main():
     try:
          #Get the number of hours worked.
          hours= int(input("How many hours did you work?"))
          # Get the hourly paid rate.
          pay_rate=float(input("enter the hourly paid rate:"))
          # Claculate the gross pay
          gross_pay=hours*pay_rate
          # Display the gross pay
          print('Gross pay: $',format(gross_pay,'2f'),sep="")
     except ValueError:
          print("Error:")
main()
