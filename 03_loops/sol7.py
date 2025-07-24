number = input("Enter a number: ")
number = int(number)


while not (number > 1 and number < 10) :
    number = input("Enter a number: ")
    number = int(number)

while True:
    number = int(input("Enter value b/w 1 and 10: "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number, try again")