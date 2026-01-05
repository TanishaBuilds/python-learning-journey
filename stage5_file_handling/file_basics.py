
# Task 1: Write Student Name
file = open("intro.txt", "w")
file.write("Name: Tanisha\n")
file.write("course: MSC Computer Science\n")
file.write("stop consuming start creating !")
file.close()

# Task 2: Read File Content
file = open("intro.txt","r")
content = file.read()
print(content)
file.close()

file = open("intro.txt", "a")

file.write("\nLearning Python Day by Day")
file.close()