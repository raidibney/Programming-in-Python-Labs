def calculate_average(marks):
    average = sum(marks) / len(marks)
    return average

marks = [80, 85, 90, 75, 70]

result = calculate_average(marks)

print("Average marks:", result)