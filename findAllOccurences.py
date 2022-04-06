import textwrap

def count_substring(string, sub_string):
    found = 0

    for i in range(len(string)):
        if string.find(sub_string, i, i+len(sub_string)) != -1:
            found+=1

    return found

string = "ABCDCDC"
sub_string = "CDC"

count = count_substring(string, sub_string)
print(count)

#### Join wrapped text

def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))

print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))