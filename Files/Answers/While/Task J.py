x = int(input())
delit = 2
result = x
while delit * delit <= x:
    if x % delit == 0:
        result = delit
    delit += 1
print(delit)
