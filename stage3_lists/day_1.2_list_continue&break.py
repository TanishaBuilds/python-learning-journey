# # task :1
# marks = [65, 72, 80, 30, 90, 88]

# for m in marks :
#     if m >=35:
#         print(m)
#     else:
#         break
            
# # task:2
# marks = [45, 22, 78, 30, 90, 33, 60]

# for m in marks:
#     if m < 35:
#         continue
#     else:
#         print(m)

# task :3
marks = [90, -5, 76, 150, 60, 88]
marks_count = 0
for m in marks:
    if m > 1:
        marks_count += 1
        print(m)
        
        
print(f"no. of valid marks = {marks_count}")