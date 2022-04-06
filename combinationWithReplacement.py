from itertools import combinations_with_replacement

def cleanPrint(x):
    print(",".join(x).replace(",",""))

input = "HACK 2"
inputString, n = input.split(" ")
sortedString = sorted(inputString)

list(map(cleanPrint, list(combinations_with_replacement(sortedString, int(n)))))
