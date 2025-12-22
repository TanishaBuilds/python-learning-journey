# #task : 1
# for i in range(2,51,2):
#     print(i)

# #task :2 
# num = input("Enter number : ")
# digit_count = len(num)
# print(f"the number if digits in {num} is : {digit_count}")

# task 3 : 
while True:
    print("----- MENU -----")
    print("1. Table")
    print("2. Sum")
    print("3. Exit")

    choice = input("Enter your choice (just say 1,2,3): ")

    if choice == "1":
        print("Table")
        num = int(input("Enter a number : "))
        for i in range (1,11):
            print(f"{num} X {i} = {num*i}")

    elif choice == "2":
        print("Sum")
        a = int(input("Enter the value of a : "))
        b = int (input("Enter the value of b : "))
        print(f" the sum of {a} and {b} = {a+b}")

    elif choice == "3":
        print("Exit")
        break
    
    else :
        print("wrong choise!")

