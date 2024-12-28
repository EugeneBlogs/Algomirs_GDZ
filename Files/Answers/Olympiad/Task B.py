str = input()
position_x = 0
position_y = 0
count = 0
direction = "U"
positions = [[0, 0]]
ok = False
for s in str:
    if s == "L":
        if direction == "U":
            direction = "L"
        elif direction == "L":
            direction = "D"
        elif direction == "D":
            direction = "R"
        elif direction == "R":
            direction = "U"
    elif s == "R":
        if direction == "U":
            direction = "R"
        elif direction == "R":
            direction = "D"
        elif direction == "D":
            direction = "L"
        elif direction == "L":
            direction = "U"
    elif s == "S":
        if direction == "U":
            position_y += 1
        elif direction == "R":
            position_x += 1
        elif direction == "D":
            position_y -= 1
        elif direction == "L":
            position_x -= 1
        count += 1
        positions.append([position_x, position_y])
        for el in positions:
            if positions.count(el) > 1:
                print(count)
                ok = True
                break
        if ok:
            break
if ok == False:
    print(-1)
