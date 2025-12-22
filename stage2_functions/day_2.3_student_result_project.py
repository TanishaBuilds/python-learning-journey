# Mini Project: Student Result System

def calculate_total(p,c,m):
    return p+c+m

def calculate_percentage(total):
    return (total/300)*100

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    
    elif percentage >=80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >=60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >=40:
        return "D"
    else:
        return "F(work hard)"
    
def display_result(name,total,percentage,grade):
    print("Name : ",name)
    print("Total Marks : ",total)
    print("Percentage : ",percentage)
    print("Grade : ",grade)


name = input("Enter your name : ")

total = calculate_total(98,97,95)
percentage = calculate_percentage(total)
grade = calculate_grade(percentage)

display_result(name,total,percentage,grade)
   