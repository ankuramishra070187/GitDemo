file = open('test.txt')

# read the content of file object
# file.read()
# print(file.read())  # print content
# print(file.read(2))  # to read only specific characters or byte

# print(file.readline())  # to read first one line
# print(file.readline())

# print all contents line by line

""" 

line = file.readline()

while line != "":
    print(line)
    line = file.readline() 
    
"""

for items in file.readlines():
    print(items)

file.close()
