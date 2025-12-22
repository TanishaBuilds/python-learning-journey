a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

n = input("What do you want (add, sub, mul, div, mod, power): ")

if n == "add":
    print("Addition:", a + b)

elif n == "sub":
    print("Subtraction:", a - b)

elif n == "mul":
    print("Multiplication:", a * b)

elif n == "div":
    if b != 0:
        print("Division:", a / b)
    else:
        print("Error: Division by zero")

elif n == "mod":
    print("Modulus:", a % b)

elif n == "power":
    print("Power:", a ** b)

else:
    print("Invalid operation selected")
