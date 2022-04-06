
names = ["harry", "berry", "tina", "bob", "akriti", "harsh"]
grades = [37.21, 37.21, 37.2, 37.2, 41, 39] 
n = len(names)
groupedData = []

for i in range(n):
    groupedData.append([grades[i], names[i]])
groupedData.sort()

print(groupedData)

lowest = groupedData[0]
withoutLowest = list(filter(lambda x: x[0] != lowest[0], groupedData))
runnerUp = withoutLowest[0][0]
secondLowest = list(filter(lambda x: x[0] == runnerUp, withoutLowest))

sortedList = []
for i in range(len(secondLowest)):
    sortedList.append(secondLowest[i][1])

sortedList.sort()
list(map(print,sortedList))
