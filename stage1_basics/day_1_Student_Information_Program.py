Name = input("Enter your name : ")
Date_of_Birth = str(input("Enter your DOB :"))
Fathers_Name = input("Enter your father's name :")
Mothers_name = input("Enter your mother's name :")
Class = input("Enter your class : ")
Roll_number = input("Enter your roll no. :")
MArks = float(input("Enter your marks"))

print("\n----Student details-----")
print("Name : ", Name)
print("DOB : ", Date_of_Birth)
print("Father's name : ", Fathers_Name)
print("Mother's name : ", Mothers_name)
print("class :" , Class )
print(" Marks : ",MArks )
print(" Roll Number : ", Roll_number)

if MArks >= 40 :
    print("result : pass")
else:
    print("result : fail")    

    

