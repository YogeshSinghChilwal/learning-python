num = 5

i = 1
total = 1
while i <= num:
    total *= i
    i += 1

print(total)

number = 5
factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1
    factorial *= number
    number -= 1

print("Factorial: ", factorial)