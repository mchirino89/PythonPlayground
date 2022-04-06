from functools import reduce

array = list(map(int, "161 182 161 154 176 170 167 171 170 174".split()))
print(array)

distinc = set(array)
average = sum(distinc) / len(distinc)
print(average)