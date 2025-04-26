# open file, "r" means read mode
file = open("./data.txt", "r", encoding="utf-8")

# read all the content
content1 = file.read()
print(content1)
file.close() # remember to close resource

# use with syntax, no need to close manually
with open("./data.txt", "r", encoding="utf-8") as file2:
    print(file2.readline()) # read one line

    # read all the lines
    for line in file2.readlines():
        print(line)