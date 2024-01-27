#escape characters
print("hey there! \nnice to meet you! \t What is your name? ")
print("\nHe said, \"My name is Sam\"")
#The above sentence can also be written as
print("He said, 'My name is Sam'/")

#tax calculator
items=int(input("\n\nenter the number of itmes that you purchased:"))
cost_of_item=float(input("enter the cost of item:"))
taxRate=0.5
amount_before_tax=(items*cost_of_item)
amount_after_tax=amount_before_tax+(amount_before_tax*taxRate)
print("you purchased ",items," items.\nThe cost of each itme is",cost_of_item)
print(f"Total amount before tax is {amount_before_tax}.")
print(f"Total amount after tax is {amount_after_tax}.")

#area of rectangle
l=float(input("\n\nenter length of rectangle:"))
b=float(input("enter breadth of rectangle:"))
area=l*b
print(f"area of reactangle is {area}")

#swapping variables
num1=int(input("\n\nenter num1:"))
num2=int(input("enter num2:"))
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(f"after swapping:\nnum1={num1}\nnum2={num2}")