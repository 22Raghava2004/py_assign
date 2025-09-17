
num1=float(input("enter the first number: "))
num2=float(input("input th second number: "))
operation=input("enter the operation: ")
if operation=="+":
    add=num1+num2
    print(f"the addition of num1 and num2 is{add}")
elif operation=="-":
    sub=num1-num2
    print(f"the subtraction of num1 and num2 is {sub}")
elif operation=="*":
    mul=num1*num2
    print(f"the multiplication of num1 and num2 is {mul}")
elif operation=="/":
    if num2==0:
        print("division by zero is not allowed")
    else:
        div=num1/num2
        print(f"the division of num1 and num2 jojo is {div}")

