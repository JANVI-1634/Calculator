print("Your Option:")
a=print("(a) Addition ")
b=print("(b) subtraction")
c=print("(c) Multiplication")
d=print("(d) Divide")
choice=str(input("Enter your choice:"))
if choice=="a":
    num1=int(input("Enter first Number:"))
    num2=int(input("Enter second Number:"))
    Total = num1+num2
    print("addition is:",Total)

elif choice=="b":
    num1=int(input("Enter first Number:"))
    num2=int(input("Enter second Number:"))
    Total = num1-num2
    print("Subtraction is:",Total)
    
elif choice=="c":
    num1=int(input("Enter first Number:"))
    num2=int(input("Enter second Number:"))
    Total = num1*num2
    print("Multiplication is:",Total)

elif choice=="d":
    num1=int(input("Enter first Number:"))
    num2=int(input("Enter second Number:"))
    if num1 and num2 == 0:
        print("Number not divisible by zero(0)")
    else:
        Total=num1/num2
        print("Quotient is:",Total)

else:
    print("Invalid choice")