def display_report(students):
    for student in students:
        print("Student ID:", student["id"])
        print("Name:", student["name"])
        print("Average:", student["average"])
        print("Performance:", classify_performance(student["average"]))
        print("------------------------")


def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


students = [
    {"id": 101, "name": "Rahim", "average": 85},
    {"id": 102, "name": "Karim", "average": 75},
    {"id": 103, "name": "Nila", "average": 55}
]

display_report(students)