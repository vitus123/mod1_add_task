grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_score = {}

students = list(students)
students.sort()

for i in range(0, len(students)):
    average = sum(grades[i]) / len(grades[i])
    average_score[students[i]] = average

print(average_score)
