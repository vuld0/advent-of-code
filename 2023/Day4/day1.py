import re


def Day3_part1():
    # to get the proper input
    def parseInput():
        getInput = open('input.txt').read()
        regex = 'Card\s+\d+:\s+((?:\d+\s+)+)\|\s+((?:\d+\s+)+)'
        matches = re.findall(regex, getInput)

        SC = []
        for match in matches:
            wn = set(int(x) for x in match[0].split())  # wn: winning numbers
            n = set(int(x) for x in match[1].split())  # n: numbers we have
            SC.append((wn, n))

        return SC

    def calculatePoints(scratchCards):
        totalPoints = 0
        for winningNumbers, numbersYouHave in scratchCards:
            matches = len(winningNumbers.intersection(numbersYouHave))
            totalPoints += int(2 ** (matches - 1))
        return totalPoints

    # SC: scratch cards
    # TP: total points

    SC = parseInput()
    TP = calculatePoints(SC)
    print(f"Total points: {TP}")


Day3_part1()
