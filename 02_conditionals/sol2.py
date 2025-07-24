from datetime import datetime

today = datetime.today().strftime("%A")  # %A gives full weekday name


adult_price = 12
child_price = 8
discount = 2
# today = "Wednesday"

age = input("Enter your age: ")
age = int(age)

if(today != "Wednesday"):
    if(age >= 18):
        print("Your peice is ", adult_price)
    elif(age < 18):
        print("Your price is ", child_price)
else:
    if(age >= 18):
        print("Your peice is ", adult_price - discount)
    elif(age < 18):
        print("Your price is ", child_price - discount)


age = 26
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    # price = price - 2
    price -= 2

print("Ticket price for you is $",price)