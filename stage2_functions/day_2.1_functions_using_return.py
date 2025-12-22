# 1️ Function that returns square of a number

def square(a):
    return a*a

result = square(5)
print("Square = ",result)

# 2️ Function that returns total marks (3 subjects)

def total_mark(p,c,m):
    return p+c+m

result = total_mark(98,96,94)
print("Total Marks : ",result)

# 3️ Function that returns grade based on marks

def grade(marks):
    if marks >=90:
        return "A+"

    elif marks >= 80:
        return "A"

    elif marks >=60:
        return "B+"

    elif marks >= 50:
        return "B"

    elif marks >=40:
        return "C"

    else:
       return "D (Work Hard)"

result = grade(78)
print("Grade : ",result)





    