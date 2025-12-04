with open("input.txt") as file:
    map = [[i for i in j.strip()] for j in file.readlines()]


# print(map)

def clamp(start, num, end):
    if num < start:
        return start
    if num > end:
        return end
    return num


def remove_rolls(map):
    res = []
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == ".":
                continue

            count = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if (y - i) < 0 or (y - i) >= len(map):
                        continue
                    if (x - j) < 0 or (x - j) >= len(map[0]):
                        continue
                    if map[y - i][x - j] == "@":
                        count += 1
            

            if count < 5:
                res.append((x, y))


    # print(len(res))
    # print(res)

    return res

count = 0
while 1:
    can_remove = remove_rolls(map)
    if len(can_remove) == 0:
        print(count)
        break

    count += len(can_remove)
    for x, y in can_remove:
        map[y][x] = "."

