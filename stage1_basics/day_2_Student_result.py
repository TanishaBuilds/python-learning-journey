name = input("Enter your name : ")
marks = int(input("Enter your marks : "))

if marks >= 75:
    grade = "Distiction"
    remark = "exicelent work !"

elif marks >= 60:
    grade = "First class"
    remark = "good"

elif marks >= 40 :
    grade = "pass"
    remark = "needs improvement !"

else:
    grade = "fail"
    remark = "work hard !"

print("Name : " ,name)
print("Marks : ",marks)
print("Grade : ",grade)
print(remark)


        