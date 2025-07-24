color = input("Enter your fruit's color to see if a fruit is ripe, overripe, and unripe: ")

if(color == 'Green'):
    print("Unripe")
elif(color == 'Yellow'):
    print("Ripe")
elif(color == 'Brown'):
    print("Overripe")
else:
    print("Enter color in Green, Yellow, Brown")