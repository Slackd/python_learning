num1 = float(input("Enter First Number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter Second Number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Enter a valid operator")
