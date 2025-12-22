# Task 1: Student Result Function

def calculate(p,c,m):
    total = p + c+ m
    percentage = (total/300)*100
    return total,percentage

total_marks,percentage = calculate(98,87,95)

print("Total marks = ",total_marks)
print("Percentage = ",percentage)

# Task 2: Calculator Function
def calculate(a,b):
    return a+b,a-b,a*b

sum_value ,dif_value ,mul_value = calculate(10,5)

print("Sum = ",sum_value)
print("Difference = ", dif_value)
print("Multiplication = ",mul_value)