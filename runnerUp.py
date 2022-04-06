arr = [2,3,6,6,5]
arr.sort(reverse=True)
highest = arr[0]
result = list(filter(lambda x: x != highest, arr))
runnerUp = result[0]

print(runnerUp)