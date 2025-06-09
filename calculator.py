print("Mini Calculator")

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number:"))

print("Press 1 for Addition\nPress 2 for subtraction\nPress 3 for Multiplication\nPress 4 for Division")
choice=int(input("Enter your choice from 1-4: "))

if choice==1:
    print(num1+num2)

elif choice==2:
    print(num1-num2)

elif choice==3:
    print(num1*num2)

elif choice==4:
    print(num1/num2)

else:
    print("Invalid input")                