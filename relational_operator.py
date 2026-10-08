"""create a list called big_list, which contains the variables x and y,
    10 times each, by concatenating the two lists you have created"""

numbers = [[1, 2]] * 3
print(numbers)

numbers = [1, 2] * 3
print(numbers)



x = object()
y = object()

# TODO: change this code
x_list = [x]
y_list = [y]
big_list = []

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y)== 10:
    print("Great!")