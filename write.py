# read the file and stroe all lines in list
# reverse the list
# write the list back to file


# another way to open a file as it also takes care of automatically closing it
with open('test.txt', 'r') as reader:
    # file opening modes 'r' --> read mode 'w' --> write mode
    content = reader.readlines()
    # reversed(content)

    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
