column_1 = int(input())
row_1 = int(input())
column_2 = int(input())
row_2 = int(input())
if (column_1 + 1 == column_2 and row_1 + 2 == row_2) or (column_1 + 2 == column_2 and row_1 + 1 == row_2) or \
        (column_1 - 1 == column_2 and row_1 + 2 == row_2) or (column_1 - 2 == column_2 and row_1 + 1 == row_2) or \
        (column_1 + 1 == column_2 and row_1 - 2 == row_2) or (column_1 + 2 == column_2 and row_1 - 1 == row_2) or \
        (column_1 - 1 == column_2 and row_1 - 2 == row_2) or (column_1 - 2 == column_2 and row_1 - 1 == row_2):
    print("YES")
else:
    print("NO")
