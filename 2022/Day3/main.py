def day3():
    # type: () -> object
    with open('day3.txt', 'r') as file:
        pri = 0
        content = file.read()
        content_list = content.split("\n")
        for i in range(0, len(content_list), 3):
            str1 = content_list[i]
            str2 = content_list[i + 1]
            str3 = content_list[i + 2]
            pri += priority_of_compartments(str1, str2, str3)
        print(pri)


def priority_of_compartments(string1, string2):
    common_char = set([char for char in string1 if char in string2]).pop()
    print(common_char)
    priority = get_priority(common_char)
    return priority


def priority_of_compartments(string1, string2, string3):
    common_char = set(set(string1).intersection(set(string2), set(string3))).pop()
    print(common_char)
    priority = get_priority(common_char)
    return priority


def get_priority(char1):
    priority = 0
    priority_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                     'm': 13,
                     'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
                     'y': 25,
                     'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36,
                     'K': 37,
                     'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48,
                     'W': 49,
                     'X': 50, 'Y': 51, 'Z': 52}
    priority = priority_dict[char1]
    return priority


if __name__ == '__main__':
    results = day3()
