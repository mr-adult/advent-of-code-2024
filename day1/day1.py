try:
    f = open("PATH TO INPUT", "rt")

    content = f.read()
    lines = content.split("\n")

    list1 = []
    list2 = []
    for line in lines:
        parts = list(filter(lambda piece: piece != "", line.split(" ")))
        if len(parts) != 2:
            raise ValueError("should have 2 items per line")
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))

    list1.sort()
    list2.sort()
    aggregate = 0

    for i in range(len(list1)):
        result = abs(list1[i] - list2[i])
        string = str(list1[i]) + ", " + str(list2[i]) + " -> " + str(result)
        print(string)
        aggregate += result

    print(aggregate)

finally:
    f.close()
