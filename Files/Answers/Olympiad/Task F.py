a, b, T = map(int, input().split())
pole = []
for i in range(a):
    pole.append([0] * b)
pos_1_x, pos_1_y = map(int, input().split())
pos_2_x, pos_2_y = map(int, input().split())
pos_3_x, pos_3_y = map(int, input().split())
dir_1, dir_2, dir_3 = "U", "U", "U"
for i in range(T):
    if pole[pos_1_x - 1][pos_1_y - 1] == 0:
        pole[pos_1_x - 1][pos_1_y - 1] = 1
        if dir_1 == "U":
            dir_1 = "R"
            if pos_1_y != b:
                pos_1_y += 1
        elif dir_1 == "R":
            dir_1 = "D"
            if pos_1_x != a:
                pos_1_x += 1
        elif dir_1 == "D":
            dir_1 = "L"
            if pos_1_y != 1:
                pos_1_y -= 1
        elif dir_1 == "L":
            dir_1 = "U"
            if pos_1_x != 1:
                pos_1_x -= 1
    else:
        pole[pos_1_x - 1][pos_1_y - 1] = 0
        if dir_1 == "U":
            dir_1 = "L"
            if pos_1_y != 1:
                pos_1_y -= 1
        elif dir_1 == "R":
            dir_1 = "U"
            if pos_1_x != 1:
                pos_1_x -= 1
        elif dir_1 == "D":
            dir_1 = "R"
            if pos_1_y != b:
                pos_1_y += 1
        elif dir_1 == "L":
            dir_1 = "D"
            if pos_1_x != a:
                pos_1_x += 1
    if pole[pos_2_x - 1][pos_2_y - 1] == 0:
        pole[pos_2_x - 1][pos_2_y - 1] = 2
        if dir_2 == "U":
            dir_2 = "R"
            if pos_2_y != b:
                pos_2_y += 1
        elif dir_2 == "R":
            dir_2 = "D"
            if pos_2_x != a:
                pos_2_x += 1
        elif dir_2 == "D":
            dir_2 = "L"
            if pos_2_y != 1:
                pos_2_y -= 1
        elif dir_2 == "L":
            dir_2 = "U"
            if pos_2_x != 1:
                pos_2_x -= 1
    else:
        pole[pos_2_x - 1][pos_2_y - 1] = 0
        if dir_2 == "U":
            dir_2 = "L"
            if pos_2_y != 1:
                pos_2_y -= 1
        elif dir_2 == "R":
            dir_2 = "U"
            if pos_2_x != 1:
                pos_2_x -= 1
        elif dir_2 == "D":
            dir_2 = "R"
            if pos_2_y != b:
                pos_2_y += 1
        elif dir_2 == "L":
            dir_2 = "D"
            if pos_2_x != a:
                pos_2_x += 1
    if pole[pos_3_x - 1][pos_3_y - 1] == 0:
        pole[pos_3_x - 1][pos_3_y - 1] = 3
        if dir_3 == "U":
            dir_3 = "R"
            if pos_3_y != b:
                pos_3_y += 1
        elif dir_3 == "R":
            dir_3 = "D"
            if pos_3_x != a:
                pos_3_x += 1
        elif dir_3 == "D":
            dir_3 = "L"
            if pos_3_y != 1:
                pos_3_y -= 1
        elif dir_3 == "L":
            dir_3 = "U"
            if pos_3_x != 1:
                pos_3_x -= 1
    else:
        pole[pos_3_x - 1][pos_3_y - 1] = 0
        if dir_3 == "U":
            dir_3 = "L"
            if pos_3_y != 1:
                pos_3_y -= 1
        elif dir_3 == "R":
            dir_3 = "U"
            if pos_3_x != 1:
                pos_3_x -= 1
        elif dir_3 == "D":
            dir_3 = "R"
            if pos_3_y != b:
                pos_3_y += 1
        elif dir_3 == "L":
            dir_3 = "D"
            if pos_3_x != a:
                pos_3_x += 1
result = []
for s in pole:
    line = []
    for i in s:
        line.append(f"{i}")
    result.append(line)
for s in result:
    print(" ".join(s))
