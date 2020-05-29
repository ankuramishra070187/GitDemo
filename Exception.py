ItemsInCart = 0

if ItemsInCart != 2:
    pass
    # raise Exception("Product cart not matching count")

assert (ItemsInCart == 0)

# try,except

try:
    with open('1test.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print("There is failure\n", e)

finally:
    print("why do i have to print this all the time?")
