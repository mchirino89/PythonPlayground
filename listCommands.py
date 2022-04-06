def operate(input, list):
    instruction, *operations = input.split()
    if instruction == "insert":
        position = int(operations[0])
        value = int(operations[1])
        list.insert(position, value)
    if instruction == "print":
        print(list)
    if instruction == "remove":
        value = int(operations[0])
        list.remove(value)
    if instruction == "append":
        value = int(operations[0])
        list.append(value)
    if instruction == "sort":
        list.sort()
    if instruction == "pop":
        list.pop()
    if instruction == "reverse":
        list.reverse()

    return list

n = 29

commands = [
    "append 1",
    "append 6",
    "append 10",
    "append 8",
    "append 9",
    "append 2",
    "append 12",
    "append 7",
    "append 3",
    "append 5",
    "insert 8 66",
    "insert 1 30",
    "insert 6 75",
    "insert 4 44",
    "insert 9 67",
    "insert 2 44",
    "insert 9 21",
    "insert 8 87",
    "insert 1 75",
    "insert 1 48",
    "print",
    "reverse",
    "print",
    "sort",
    "print",
    "append 2",
    "append 5",
    "remove 2",
    "print"
]

list = []

for i in range(n):
    operate(commands[i], list=list)

