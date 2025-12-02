with open("input.txt") as file:
    raw_data = file.read().strip().split(",")

data = [map(int, case.split("-")) for case in raw_data]

# print(data)


def check_validity(id):

    if len(id) % 1:
        return False

    if id[:len(id)//2] == id[len(id)//2:]:
        return True

    return False

    # if length_id % 2: return False
    #
    # for i in range(1, length_id // 2 + 1):
    #     if id[:i] * (length_id // i) == id:
    #         return True
    #
    # return False


# print(check_validity("111"))
# print(check_validity("222"))
# print(check_validity("101"))
# print(check_validity("1212"))
# print(check_validity("1221"))
# print(check_validity("898989898"))
# print(check_validity("89898989"))

res = 0
for start, end in data:
    for i in range(start, end + 1):
        if check_validity(str(i)):
            print(i)
            res += i


print(res)
