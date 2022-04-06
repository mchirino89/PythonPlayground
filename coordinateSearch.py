def coordinateSum(i, j, k):
    return i + j + k

x = range(2)
y = range(2)
z = range(2)
n = 2

allPermutations = [[i, j, k] for i in x for j in y for k in z 
if coordinateSum(i,j,k) != n]

print(allPermutations)
