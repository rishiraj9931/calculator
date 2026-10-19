a = int (input("enter the first number: "))
b = int (input("enter the second number: "))
op =  input("enter operator(+,-,*,/): ")
if op =="+":
 print ("result=",a + b)
if op=="-":
 print ("result=",a - b)
if op=="*":
  print ("result=",a * b)
if op=="/":
    if b!=0:
      print ("result=",a / b)
else:
     print ("cannot divide by zero ")
 
