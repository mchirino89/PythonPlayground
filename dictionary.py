from functools import reduce

n = 3

input = ["Krishna 67 68 69", "Arjun 70 98 63", "Malika 52 56 60"]
query_name = "Malika"
student_marks = {}
for i in range(n):
    name, *line = input[i].split()
    print(line)
    scores = list(map(float, line))
    print(scores)
    student_marks[name] = scores

notes = reduce(lambda x, y: x+y, student_marks[query_name]) / len(student_marks[query_name])
print()
print(student_marks)
print(student_marks[query_name])
print("%.2f" % notes)