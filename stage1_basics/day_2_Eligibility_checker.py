name = input("Enter your name: ")
age = int(input("Enter your age: "))
citizen = input("Citizen of India (yes/no): ").lower()
identity_available = input("ID available (yes/no): ").lower()
gender = input("Enter your gender: ")
state = input("Enter your state: ")

# Eligibility logic
if age < 18:
    status = "Not Eligible"
    reason = "Age below 18"

elif citizen != "yes":
    status = "Not Eligible"
    reason = "Not an Indian citizen"

elif identity_available != "yes":
    status = "Not Eligible"
    reason = "ID not available"

else:
    status = "Eligible"
    reason = "All conditions satisfied"

# Output
print("\n--- Eligibility Report ---")
print("Name:", name)
print("Age:", age)
print("Gender:", gender)
print("State:", state)
print("Citizen:", citizen)
print("ID Available:", identity_available)
print("Status:", status)
print("Reason:", reason)
