# 🎓 Student Grading System

# Taking marks input from user
mark1 = float(input("Enter English marks: "))
mark2 = float(input("Enter Marathi marks: "))
mark3 = float(input("Enter Math marks: "))
mark4 = float(input("Enter Physics marks: "))
mark5 = float(input("Enter Chemistry marks: "))

# Calculating total and percentage
total = mark1 + mark2 + mark3 + mark4 + mark5
percentage = (total / 500) * 100

# Grading logic
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "Fail"

# Final Output
print(f"📊 Total Marks: {total}/500")
print(f"📈 Percentage: {percentage:.2f}%")
print(f"🏅 Grade: {grade}")
