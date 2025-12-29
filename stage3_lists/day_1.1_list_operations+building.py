marks = [78, 55, 25, 30, 45]

pass_count = 0
fail_count = 0

for m in marks:
    if m >= 35:
        pass_count += 1
    elif m + 5 >= 35:
        pass_count += 1
        print(f"Student passed with grace marks. Original marks: {m}")
    else:
        fail_count += 1


print("pass_count =", pass_count)
print("fail_count =", fail_count)

