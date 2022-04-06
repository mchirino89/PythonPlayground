from itertools import permutations

def cleanPrint(x):
    print(",".join(x).replace(",",""))

input = "HACK 2"
inputString, n = input.split(" ")
sortedString = sorted(inputString)

list(map(cleanPrint, list(permutations(sortedString, int(n)))))
