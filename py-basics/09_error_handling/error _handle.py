# file = open('youtube.txt', 'w')

# try:
#     file.write("part 2")
# finally:
#     file.close()

#* New and better way

with open('youtube.txt', 'w') as file:
    file.write('new syntax')