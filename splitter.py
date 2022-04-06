test = "1 w 2 r 3g"
splitted = test.split(sep=" ")
result = list(map(lambda x: x.capitalize(), splitted))
string = ""

for i in range(0, len(result)):
    string+= str(result[i] + " ")


