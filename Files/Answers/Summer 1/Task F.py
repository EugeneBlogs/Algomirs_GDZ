C = input()
if C.isalpha():
    if C.isupper():
        print(C.lower())
    else:
        print(C.upper())
else:
    print(C)
