def day2():
    main_points = 0
    with open('day2.txt', 'r') as file:
        content = file.read()
        modified_content = content.split("\n")
        for i in modified_content:
            choices = i.split(" ")
            main_points += stone_paper_scissors_2nd_part(choices[0], choices[1])


        return main_points


def stone_paper_scissors(string1, string2):
    point = 0
    default_points = {"X": 1, "Y": 2, "Z": 3}

    if string2 in default_points:
        point = default_points[string2]

    # checking for tie
    if string1 == "A" and "X" == string2:
        point += 3
    if string1 == "B" and "Y" == string2:
        point += 3
    if string1 == "C" and string2 == "Z":
        point += 3
    # checking for win
    if string2 == "X" and string1 == "C":
        point += 6
    elif string2 == "Y" and string1 == "A":
        point += 6
    elif string2 == "Z" and string1 == "B":
        point += 6

    return point

def stone_paper_scissors_2nd_part(string1, string2):
    point = 0
    round_outcome_X = {"A": 3, "B": 1, "C": 2}
    round_outcome_Y = {"A": 1, "B": 2, "C": 3}
    round_outcome_Z = {"A": 2, "B": 3, "C": 1}


    if(string2 == "X"):
        if string1 in round_outcome_X:
            point += round_outcome_X[string1]

    if (string2 == "Y"):
        if string1 in round_outcome_Y:
            point += round_outcome_Y[string1]
        point += 3

    if (string2 == "Z"):
        if string1 in round_outcome_Z:
            point += round_outcome_Z[string1]
        point += 6

    return point



if __name__ == '__main__':
    points = day2()
    print(points)
