marks = float(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade: A+")
elif marks >= 85:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B+")
elif marks >= 75:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C+")
elif marks >= 65:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D+")
elif marks >= 55:
    print("Grade: D")
elif marks >= 0:
    print("Grade: F")
else:
    print("Invalid marks!")