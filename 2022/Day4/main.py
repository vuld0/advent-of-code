import fileinput

data = [line.strip() for line in fileinput.input("day4.txt")]
print(data)

list1 = [0, 0, 2, 3, 4]
list2 = [ 2, 3, ]

if list2 in list1:
    print("yes")