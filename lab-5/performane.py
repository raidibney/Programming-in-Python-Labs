def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


average = float(input("Enter the average marks: "))

result = classify_performance(average)

print("Performance:", result)