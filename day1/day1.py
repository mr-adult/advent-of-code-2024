def get_inputs() -> list[list[int]]:
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
    finally:
        f.close()
    
    return [list1, list2]

# Part 1
[list1, list2] = get_inputs()
list1.sort()
list2.sort()
aggregate = 0

for i in range(len(list1)):
    result = abs(list1[i] - list2[i])
    string = str(list1[i]) + ", " + str(list2[i]) + " -> " + str(result)
    print(string)
    aggregate += result

print(aggregate)

# Part 2
[list1, list2] = get_inputs()

instances_map = {}
for item in list2:
    if item in instances_map:
        instances_map[item] += 1
    else:
        instances_map[item] = 1

aggregate = 0
for item in list1:
    if item in instances_map:
        aggregate += item * instances_map[item]

print(aggregate)
