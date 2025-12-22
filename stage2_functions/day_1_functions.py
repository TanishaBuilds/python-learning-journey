

def my_name(name):
    print("Name : ",name)

def product(a,b):
    print(f"{a} X {b} = {a*b}")

def my_marks(marks):
    
    if marks >= 35:
        print("Pass")

    else:
        print("Fail!")
    
name = input("Enter your name : ")
my_name(name)

a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b : "))
product(a,b)

marks = int(input("Enter your marsk : "))
my_marks(marks)


