def day1():
    with open('day1.txt', 'r') as file:
        content = file.read()
        print(content)
        results = []

        # converting the contents to a list

        contentList = content.split("\n\n")
        for i in contentList:
            tempList = i.split("\n")
            results.append(sum(int(n) for n in tempList))

        return results


if __name__ == "__main__":
    results = day1()
    sum_top_3 = sum(sorted(results, reverse=True)[:3])
    print('top 3 is', sum_top_3)

