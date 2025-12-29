# Mini Project: Student Marks Analyzer

marks = [78, 45, -3, 90, 33, 150, 60, 88]

count_pass = 0
count_fail = 0
def get_valid_marks(marks):
    valid_marks = []
    for m in marks:
        if 0 <= m <= 100:
            valid_marks.append(m)
    return valid_marks

def counter(valid_marks):
            
            count_pass = 0
            count_fail = 0
            for m in valid_marks:
                if m >= 35:
                    count_pass += 1
                    
                else:   
                    count_fail += 1

            return(count_pass,count_fail)

def highest_lowest(valid_marks):
     return max(valid_marks),min(valid_marks)

valid_marks = get_valid_marks(marks)
print("valid marks : ", valid_marks)

pass_student,fail_student = counter(valid_marks)
print("pass count : ", pass_student)
print("fail count : ", fail_student)

high , low = highest_lowest(valid_marks)
print("Highest marks : ", high)
print("Lowest marks : ", low)


        

        

