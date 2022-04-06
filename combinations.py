from itertools import combinations

def cleanPrint(x):
    print(",".join(x).replace(",",""))

input = "HACK 2"
inputString, n = input.split(" ")
sortedString = sorted(inputString)

for i in range(1, int(n) + 1):
    list(map(cleanPrint, list(combinations(sortedString, i))))
