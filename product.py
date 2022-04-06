from itertools import product

def cleanPrint(x):
    print(x, end=" ")

listA = "1,2"
listB = "3,4"

A = map(int,listA.split(","))
B = map(int,listB.split(","))

list(map(cleanPrint, list(product(A, B))))
