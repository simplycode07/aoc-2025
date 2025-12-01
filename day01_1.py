with open("input.txt") as file:
    raw_data = file.readlines()


data = [[data[0], int(data[1:].strip())] for data in raw_data]

# print(data)


current_pos = 50
max_num = 100
res = 0
for dir, num in data:
    if dir == "L":
        current_pos -= num

    else:
        current_pos += num

    current_pos %= max_num
    print(dir, num, current_pos)


    if current_pos == 0: res += 1



print(res)
