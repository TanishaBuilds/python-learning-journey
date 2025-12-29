student_data = {}

def add_student():
    roll_num = input("Enter Roll No.: ")

    if roll_num in student_data:
        print("Student with this roll number already exists.")
        return

    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    if 0 <= marks <= 100:
        student_data[roll_num] = {
            'name': name,
            'marks': marks
        }
        print("Student added successfully!")
    else:
        print("Invalid marks! Must be between 0 and 100.")


def view_students():
    if not student_data:
        print("No student data available.")
        return

    print("\n--- Student Profiles ---")
    for roll_num, info in student_data.items():
        print(f"Roll No.: {roll_num}")
        print(f"Name: {info['name']}")
        print(f"Marks: {info['marks']}")
        print("-" * 20)


def search_student():
    roll_num = input("Enter Roll No. to search: ")
    if roll_num in student_data:
        info = student_data[roll_num]
        print("Student Found")
        print(f"Name: {info['name']}")
        print(f"Marks: {info['marks']}")
    else:
        print("Student not found.")


# Menu-driven system
while True:
    print("\n--- MENU ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")


    


    


