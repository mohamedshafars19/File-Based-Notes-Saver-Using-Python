input_file = "students.txt"
output_file = "result.txt"

# Function to calculate grade
def calculate_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

students = []

# -------- READ TEXT FILE --------
with open(input_file, "r") as file:
    for line in file:
        data = line.strip().split(",")

        name = data[0]
        math = int(data[1])
        science = int(data[2])
        english = int(data[3])

        # -------- PROCESS --------
        avg = (math + science + english) / 3
        grade = calculate_grade(avg)

        students.append((name, round(avg, 2), grade))

# -------- WRITE TO TEXT FILE --------
with open(output_file, "w") as file:
    file.write("Name\tAverage\tGrade\n")
    
    for student in students:
        file.write(f"{student[0]}\t{student[1]}\t{student[2]}\n")

print("Data processed and saved in result.txt\n")

# -------- DISPLAY RESULT --------
print("----- RESULT -----")
with open(output_file, "r") as file:
    print(file.read())
