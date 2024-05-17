import re


def day1():
    output = ""
    with open("input.txt", "r") as file:
        content = file.read()

        # converting the content to a list
        content_list = content.split("\n")

        # adding regular expression to remove characters from the string
        no_chars = []
        for i in content_list:
            no_chars.append(re.sub(r"[a-zA-Z\n]", "", i))

        # adding the first and last value we got in no_chars list
        integer_list = []
        for i in no_chars:
            integer_list.append(int(i[0] + i[-1]))

        # adding the values of the integer_list

        output = sum(integer_list)
    return output


def day1_part2():
    output = ""
    with open("input.txt", "r") as file:
        content = file.read()

        # converting the content to a list
        content_list = content.split("\n")

        # adding regular expression to remove characters from the string
        only_numbers = []
        for i in content_list:
            new_str = re.sub(r'one', "1", i)
            new_str = re.sub(r'two', "2", new_str)
            new_str = re.sub(r'three', "3", new_str)
            new_str = re.sub(r'four', "4", new_str)
            new_str = re.sub(r'five', "5", new_str)
            new_str = re.sub(r'six', "6", new_str)
            new_str = re.sub(r'seven', "7", new_str)
            new_str = re.sub(r'eight', "8", new_str)
            new_str = re.sub(r'nine', "9", new_str)
            only_numbers.append(re.sub(r'[a-zA-Z\n]', "", new_str))

        intList = []
        for i in only_numbers:
            intList.append(int(i[0] + i[-1]))
        totalSum = sum(intList)

        return totalSum


if __name__ == "__main__":
    results = day1_part2()
    print(results)
