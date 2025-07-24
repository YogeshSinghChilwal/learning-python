name = "Yogesh"

length = len(name)
revName = ""

for i in  range(0, length):
    revName += name[- (i + 1)]

print(revName)


input_str = "Python"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str
    print(char) 

print(reversed_str)