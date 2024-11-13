password = input()
strok_letters = False
zaglav_letters = False
numbers = False
if len(password) >= 8:
    for s in password:
        if s.islower():
            strok_letters = True
        elif s.isupper():
            zaglav_letters = True
        elif s.isdigit():
            numbers = True
    if strok_letters and zaglav_letters and numbers:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
