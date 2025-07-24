number = input("Enter the number: ")
num = 10
number = int(number)

for i in range(1, num + 1):
    if(i == 5):
        continue
    else:
        print(number, 'x', i, '=', number * i)