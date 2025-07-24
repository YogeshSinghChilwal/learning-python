items = ["apple", "banana", "orange", "apple", "mango"]

unique_list = set()

for item in items:
    if(item in unique_list):
        print("Dupicate: ",item)
        break
    unique_list.add(item)