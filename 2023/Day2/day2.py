import re


def Day2():
    content = open("input.txt", "r")
    index_sum = 0

    for index, x in enumerate(content):
        flag = True

        # getting the green values in a string
        for y in re.findall(r'\d+ green', x):
            temp = int(re.sub(r' green', "", y))
            if temp > 13:
                flag = False

        # getting the red values in a string
        for y in re.findall(r'\d+ red', x):
            temp = int(re.sub(r' red', "", y))
            if temp > 12:
                flag = False

        for y in re.findall(r'\d+ blue', x):
            temp = int(re.sub(r' blue', "", y))
            if temp > 14:
                flag = False

        if flag:
            index_sum += index + 1

    return index_sum


def Day2_part2():
    content = open("input.txt", "r")
    power_value = []

    for index, x in enumerate(content):
        green_value = 0
        red_value = 0
        blue_value = 0

        # getting the green values in a string
        for y in re.findall(r'\d+ green', x):
            temp = int(re.sub(r' green', "", y))
            if temp > green_value:
                green_value = temp

        # getting the red values in a string
        for y in re.findall(r'\d+ red', x):
            temp = int(re.sub(r' red', "", y))
            if temp > red_value:
                red_value = temp

        for y in re.findall(r'\d+ blue', x):
            temp = int(re.sub(r' blue', "", y))
            if temp > blue_value:
                blue_value = temp

        power_value.append((red_value * blue_value) * green_value)

    return sum(power_value)


if __name__ == "__main__":
    print(Day2_part2())
